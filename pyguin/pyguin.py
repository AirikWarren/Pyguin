import click
import os
import shutil
import zipfile

from jinja2.environment import Environment, TemplateModule
from jinja2.loaders import FileSystemLoader

import requests

@click.group()
def main():
    ...

@click.command()
@click.option('--output', default='./output', help='Directory path to output stuff to')
def create_output_dir(output):
    '''I ate a piece of cheese. I love how you can eat food'''
    try:
        os.mkdir(f'{output}')
        os.mkdir(f'{output}/style')
    except FileExistsError:
        shutil.rmtree(f'{output}')
        os.mkdir(f'{output}')
        os.mkdir(f'{output}/style')

@click.command()
@click.option('--templates_dir', default='./templates', help= "Directory to download the boilerplate to")
def boilerplate(templates_dir):
    #try:
    #    os.chdir(templates_dir)
    #except FileNotFoundError:
    #    os.mkdir(templates_dir)
    #    os.chdir(templates_dir)
    
    r = requests.get('https://github.com/AirikWarren/Pyguin/archive/Templates.zip', stream=True)
    with open('templates.zip', 'wb') as fd:
     for chunk in r.iter_content(chunk_size=128):
             fd.write(chunk)
    
    with zipfile.ZipFile('templates.zip', 'r') as zip_ref:
        zip_ref.extractall()


main.add_command(boilerplate)
main.add_command(create_output_dir)