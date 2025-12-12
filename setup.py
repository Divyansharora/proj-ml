from setuptools import find_packages, setup
from typing import List

req_list : List[str] = []
def get_requirements() -> List[str]:
    try:            #return list of requirements
        with open("req.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    req_list.append(requirement)

    except FileNotFoundError:
        print("Requirements file not found.")

    return req_list

print(get_requirements())

setup(
    name="proj-ml",
    version="0.0.1",
    author="Divyansh Arora",
    author_email="aroradivyansh22@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements())



