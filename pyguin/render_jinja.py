import os
import shutil

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

def create_title_extension_dict(env: Environment) -> dict:
    ''' for a file "name.html". Dictionary k,v pair would be "name":"name.html" '''
    d = {x[:-5]:f'./{x}' for x in env.list_templates() if not x.startswith("_")}
    d.pop('base')
    return d

def default(template_dir, out_dir='./output'):
    try:
        os.mkdir(f'{out_dir}')
        os.mkdir(f'{out_dir}/style')
    except FileExistsError:
        shutil.rmtree(f'{out_dir}')
        os.mkdir(f'{out_dir}')
        os.mkdir(f'{out_dir}/style') 
    
    env = Environment(loader=FileSystemLoader(f'{template_dir}/html_templates'))
    filenames = [x for x in env.list_templates() if "base.html" not in x and not x.startswith("_")]
    nav_links = create_title_extension_dict(env)
    stylesheet_path = f'{template_dir}/css_templates'

    if os.path.exists(stylesheet_path):
        for x in os.listdir(stylesheet_path):
            shutil.copyfile(f'{stylesheet_path}/{x}', f'{out_dir}/style/{x}')
    
    for i in zip(filenames, nav_links):
        f = open(f'./output/{i[0]}', "+w")
        f.write(env.get_template(i[0]).render(title=i[1], nav_links=nav_links))
    
