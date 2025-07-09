from setuptools import find_packages, setup

setup(name="Sam's-bot",
      version="0.0.1",
      author="Samir Saiyed",
      author_email="samirsaiyed256@gmail.com",
      packages=find_packages(),
      install_requires=['langchain-atradb', 'langchain']   
     )