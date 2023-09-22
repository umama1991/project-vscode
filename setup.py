from setuptools import setup,find_packages 

def get_requirements(file_path):
    requirements=[]
    with open(file_path,"r") as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","")for req in requirements]
    return requirements
# to remove \n from requirements. which is showing in results due to line change


setup(
name= "MLproject",
version="0.0.1",
description="this is a test project of ml pipelines",
author="umama1991",
author_email="siddiquiumama@gmail.com",
packages=find_packages(),
install_requirements=get_requirements("requirements.txt")
)