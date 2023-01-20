""" 
This plugin module will create a lightweight jupyterhub application that
can be used to test different spawner implementations
"""

import asyncio
import sys

import pytest
from jupyterhub.jupyterhub.mocking import MockHub


@pytest.fixture
def app_for_spawners(request):
    mocked_app = MockHub()

    async def make_app():
        await mocked_app.initialize([])
        await mocked_app.start()

    def fin():
        mocked_app.log.handlers = []
        MockHub.clear_instance()
        try:
            mocked_app.stop()
        except Exception as e:
            print("Error stopping Hub: %s" % e, file=sys.stderr)

    request.addfinalizer(fin)
    asyncio.run(make_app())
    return mocked_app
