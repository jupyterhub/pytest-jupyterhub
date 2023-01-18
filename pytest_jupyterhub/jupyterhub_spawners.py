""" 
This plugin module will create a lightweight jupyterhub application that
can be used to test different spawner implementations
"""

import os
import sys
from unittest import mock
from pytest import fixture
from jupyterhub.jupterhub.mocking import MockHub

KEYTAB_PATH = "/home/testuser/testuser.keytab"
HAS_KERBEROS = os.path.exists(KEYTAB_PATH)

@fixture(scope='module')
def ssl_tmpdir(tmpdir_factory):
    return tmpdir_factory.mktemp('ssl')

@fixture(scope='module')
async def app_for_spawners(request, ssl_tmpdir):
    kwargs = dict()
    ssl_enabled = getattr(
        request.module, 'ssl_enabled', os.environ.get('SSL_ENABLED', False)
        )

    if ssl_enabled:
        kwargs.update(dict(internal_ssl=True, internal_certs_location=str(ssl_tmpdir)))

    mocked_app = MockHub.instance(**kwargs)

    await mocked_app.initialize([])
    await mocked_app.start()

    try:
        with mock.patch.dict(
            mocked_app.tornado_settings,
            {'spawner_class': mocked_app.__class__.__name__}
        ):
            if HAS_KERBEROS:
                mocked_app.config.__class__.__name__.principal = 'test_user'
                mocked_app.config.__class__.__name__.keytab = KEYTAB_PATH
            yield mocked_app
    finally:
        mocked_app.log.handlers = []
        MockHub.clear_instance()
        try:
            mocked_app.stop()
        except Exception as e:
            print("Error stopping Hub: %s" % e, file=sys.stderr)
            