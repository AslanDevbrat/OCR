import jinja2
import os
from jinja2 import Template
import os
import yaml

with open("affidavit_data.yaml") as file:
    data = yaml.load(file , Loader = yaml.FullLoader)
    print(data)


latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
    variable_start_string = '\VAR{',
	variable_end_string = '}',
    comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
    trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)


template  = latex_jinja_env.get_template('affidavit_latex.tex.jinja')

output = template.render(data)
with open('affidavit_latex.tex','w') as f:
    f.write(output)

os.system("xelatex affidavit_latex.tex")
