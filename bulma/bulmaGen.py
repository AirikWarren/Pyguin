import os 
import shutil

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

try: 
    os.mkdir('./output')
except FileExistsError:
    shutil.rmtree('./output')
    os.mkdir('./output')

def generate_title_html_dict(env : Environment) -> dict:
    ''' for a file name.html, dictionary k,v pair would be "name":"name.html" '''
    nav_links = {x[:-5]:f'./{x}' for x in env.list_templates() if not x.startswith("_")} # What the fuck? 
    nav_links['Home'] = "./index.html" # Seriously though it's just removing the file extenstion
    nav_links.pop('index')
    nav_links.pop('base')
    return nav_links

if __name__ == '__main__':
    html_template_path = './templates/html_templates' 
    env = Environment(loader=FileSystemLoader('./templates/html_templates'))
    filenames = [x for x in env.list_templates() if "base.html" not in x and not x.startswith("_")]
    nav_links = generate_title_html_dict(env)
    assert len(nav_links) == len(filenames)

    for i in zip(filenames, nav_links):
        f = open(f'./output/{i[0]}', "+w")
        f.write(env.get_template(i[0]).render(title=i[1], nav_links=nav_links))
        f.close()