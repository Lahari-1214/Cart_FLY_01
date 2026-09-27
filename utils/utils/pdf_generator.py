from xhtml2pdf import pisa
from io import BytesIO

def generate_pdf(template_html):
    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(template_html, dest=pdf)

    if pisa_status.err:
        return None
    return pdf
