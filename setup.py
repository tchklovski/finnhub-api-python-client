from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='finnhub',
    version='0.1.2',
    author='tchklovski from s0h3ck',
    author_email='tchklovski@gmail.com',
    description='Finnhub API Python client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['finnhub'],
    url='https://github.com/tchklovski/finnhub-api-python-client/',
    license='MIT',
    install_requires=['requests'],
    keywords='finnhub api stocks cryptocurrency',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
