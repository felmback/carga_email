from jinja2 import Environment, FileSystemLoader
from extract_dados import dados
from weasyprint import HTML

def generate_pdf(dataframe):
    # Carregando o template Jinja
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("template.html")

    # Renderizando o template com os dados do DataFrame
    rendered_html = template.render(data=dataframe)

    # Convertendo HTML renderizado em PDF usando WeasyPrint
    pdf = HTML(string=rendered_html).write_pdf()

    return pdf

# Exemplo de uso
if __name__ == "__main__":
    # Supondo que você tenha um DataFrame chamado df
    

    # Gerando o PDF
    pdf_output = generate_pdf(dados())

    # Salvando o PDF
    with open("output.pdf", "wb") as f:
        f.write(pdf_output)
