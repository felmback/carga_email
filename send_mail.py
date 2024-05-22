import pandas as pd
from jinja2 import Environment
import datetime

df = pd.read_excel('dados.xlsx')

data = datetime.date.today()
txt_html= """
<h1> Contrele de carga GCP </h1>
<p> Volume das cargas executada no GCP na data {{data}}</p>

{{tabela}}
"""

tbl_html = df.to_html(index=False)

tamplate = Environment().from_string(txt_html)
html = tamplate.render(tabela=tbl_html, data=data)
with open('tabela.html', 'w') as pagina:
    pagina.write(html)