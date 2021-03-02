import os 
import shutil

import jinja2
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

try:
    os.mkdir('./output')
    os.mkdir('./output/style')
except FileExistsError:
    shutil.rmtree('./output')
    os.mkdir('./output')
    os.mkdir('./output/style')

def generate_title_html_dict(env : Environment) -> dict:
    ''' for a file name.html, dictionary k,v pair would be "name":"name.html" '''
    nav_links = {x[:-5]:f'./{x}' for x in env.list_templates()}
    nav_links['Home'] = "./index.html"
    nav_links.pop('index')
    nav_links.pop('base')
    return nav_links

if __name__ == '__main__':
    env = jinja2.Environment(loader=FileSystemLoader('./templates/html_templates'))
    filenames = [x for x in env.list_templates() if "base.html" not in x]
    nav_links = generate_title_html_dict(env)

    for x in os.listdir('./templates/css_templates'):
        shutil.copyfile(f'./templates/css_templates/{x}', f'./output/style/{x}')

    for i in zip(filenames, nav_links):
        f = open(f'./output/{i[0]}', "+w")
        f.write(env.get_template(i[0]).render(title=i[1], nav_links=nav_links))
        f.close()