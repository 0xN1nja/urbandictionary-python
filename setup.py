from setuptools import setup
import os
VERSION = '0.0.5'
DESCRIPTION = 'Urban Dictionary Python (Unofficial)'
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="urbandictionary_python",
    version=VERSION,
    author="Abhimanyu Sharma",
    author_email="speedcuberabhi@gmail.com",
    description=DESCRIPTION,
    packages=[".","urbandictionary_python"],
    package_data={"urbandictionary_python":["*"]},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=["requests"],
    keywords=['python',"urban_dictionary","requests","api"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)