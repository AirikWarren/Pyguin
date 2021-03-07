import click
import os
import zipfile

from http.server import HTTPServer, SimpleHTTPRequestHandler

import requests

from . import render_jinja

@click.group()
def main():
    pass

@click.command()
def download_templates():
    '''Downloads the example templates from Github'''

    r = requests.get('https://github.com/AirikWarren/Pyguin/archive/Templates.zip', stream=True)
    with open('templates.zip', 'wb') as fd:
     for chunk in r.iter_content(chunk_size=128):
             fd.write(chunk)
    
    with zipfile.ZipFile('templates.zip', 'r') as zip_ref:
        zip_ref.extractall()
    
    os.remove('templates.zip')

@click.command()
@click.argument('template_dir', type=click.Path(exists=True))
@click.option('--output', default='./output', help='Output director for static site')
def render_template(template_dir, output):
    '''Renders a Pyguin template into a static site'''
    render_jinja.default(template_dir, output)

@click.command()
@click.option('--bind', default="127.0.0.1")
@click.option('--port', default=8000)
def run(bind, port):
    '''starts a local development only server'''
    print(f'Starting a development server at http://{bind}:{port}')
    httpd = HTTPServer((bind, int(port)), SimpleHTTPRequestHandler)
    httpd.serve_forever()


main.add_command(download_templates)
main.add_command(render_template)
main.add_command(run)