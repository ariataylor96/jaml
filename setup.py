from setuptools import setup

setup(
    name='jaml',
    version='0.1',
    description='Edit your YAML files as JSON!',
    url='https://github.com/markrawls/jaml',
    author='Mark Rawls',
    author_email='markrawls96@gmail.com',
    license='WTFPL',
    packages=['jaml'],
    zip_safe=False,
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': ['jaml:jaml.main:main'],
    }
)
