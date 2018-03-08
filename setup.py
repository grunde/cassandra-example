from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession
import os

def read_requirements():
    '''parses requirements from requirements.txt'''
    reqs_path = os.path.join(os.getcwd(), 'requirements.txt')
    install_reqs = parse_requirements(reqs_path, session=PipSession())
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs

setup(install_requires=read_requirements())