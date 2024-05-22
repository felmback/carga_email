import pandas as pd
from jinja2 import Environment, FileSystemLoader
import datetime

df = pd.read_excel('dados.xlsx')

data = datetime.date.today()


pasta_assets = "D:/Python/carga_email/assets"
arquivo_template = "template.jinja"

loader = FileSystemLoader(pasta_assets)
enviroment = Environment(loader=loader)
template = enviroment.get_template(arquivo_template)



# import pandas as pd
# from jinja2 import Environment
# import datetime

# df = pd.read_excel('dados.xlsx')

# data = datetime.date.today()
# txt_html= """
# <h1> Contrele de carga GCP </h1>
# <p> Volume das cargas executada no GCP na data {{data}}</p>

# {{tabela}}
# """

# tbl_html = df.to_html(index=False)

# tamplate = Environment().from_string(txt_html)
# html = tamplate.render(tabela=tbl_html, data=data)
# with open('tabela.html', 'w') as pagina:
    # pagina.write(html)