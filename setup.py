from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='jaml-edit',
    version='1.0.1',
    description='Edit your YAML files as JSON - and vice versa!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/markrawls/jaml',
    author='Mark Rawls',
    author_email='markrawls96@gmail.com',
    license='WTFPL',
    packages=['jaml'],
    zip_safe=False,
    install_requires=[
        'PyYAML>=5.1.0',
    ],
    entry_points={
        'console_scripts': ['jaml=jaml.main:main'],
    }
)
