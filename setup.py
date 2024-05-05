from setuptools import setup, find_packages

setup(
    name='treenode',
    version='1.1.0',
    packages=find_packages(),
    license='MIT',
    description='TreeNode is a Python library that provides functionality to create and manipulate tree structures.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Syra',
    author_email='horriblebuba@gmail.com',
    url='https://github.com/PivoSteve/treenode-py',
    project_urls={
        'Repository': 'https://github.com/PivoSteve/treenode-py',
        'Source': 'https://github.com/PivoSteve/treenode-py',
    },
    keywords='tree directory file system node structures structure',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
