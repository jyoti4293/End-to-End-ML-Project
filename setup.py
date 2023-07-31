from setuptools import find_packages, setup
from typing import List

def get_requires(file_path:str)->List[str]:
    '''
    This will get us the requirements from requirements.txt as list
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
        
    return requirements

setup(name='end-to-end-ml-project',
version='0.0.1',
description='Implementation of end-to-end ML project',
author='Jyoti Kumari',
author_email="jyotijha3924@gmail.com",
packages= find_packages(),
install_requires=[packages for packages in get_requires('requirements.txt')]
)