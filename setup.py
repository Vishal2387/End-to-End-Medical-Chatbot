## To install src as our local package

from setuptools import find_packages, setup

setup(
    name= "medical-chatbot",
    version= "0.1.0",
    author= "Vishal S",
    author_email= "vishalselvakumar@gmail.com",
    packages= find_packages(),
    install_requires=[]
)