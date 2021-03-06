import click
import os
import shutil

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

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

def main():
    create_output_dir()
