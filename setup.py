from setuptools import setup, find_packages

def read(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        return f.read()

setup(
    name= 'jupyterhub-pytest-plugin',
    version= '0.1.0',
    author= 'Jupyter Development Team',
    author_email= 'jupyter@googlegroups.com',
    license= 'BSD-3',
    description= 'A reusable JupyterHub pytest plugin',
    long_description= read('README.md'),
    packages= find_packages(),
    url= 'https://github.com/jupyterhub/jupyterhub-pytest-plugin',
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0'],
    entry_points={
        'pytest11': [
            'authenticator_plugin = jupyterhub_pytest_plugin.authenticator_plugin',
            'spawner_plugin = jupyterhub_pytest_plugin.spawner_plugin'
        ],
    },
    classifiers= [
        'Framework :: Pytest',
    ],
)