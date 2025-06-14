from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='mi_proyecto',
    version='1.0',
    description='Un proyecto de ejemplo',
    package_dir={'': 'stringjester'},
    packages=find_packages(where='stringjester'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rubén Rodríguez Tártalo',
    url='https://github.com/RubenDomingo/mi_proyecto',
    license='MIT',
    python_requires='>=3.8',
)