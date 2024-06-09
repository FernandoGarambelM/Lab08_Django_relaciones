from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import get_template
from django.shortcuts import render
from xhtml2pdf import pisa

def index(request):
    return HttpResponse("Hello, world!")

def generar_pdf(request):
    # Obtener la plantilla HTML
    template_path = 'plantilla_pdf.html'
    context = {'some_data': 'Este es un ejemplo'}

    # Renderizar la plantilla con el contexto
    template = get_template(template_path)
    html = template.render(context)

    # Crear una respuesta HTTP con el content_type como 'application/pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Convertir el HTML a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Verificar si hubo algún error durante la conversión
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF', status=500)

    return response

def enviar_correo(request):
    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        destinatario = request.POST['destinatario']
        remitente = 'tu_correo@gmail.com'  # Cambia esto por tu correo

        try:
            send_mail(asunto, mensaje, remitente, [destinatario])
            return HttpResponse('Correo enviado exitosamente')
        except Exception as e:
            return HttpResponse(f'Error al enviar el correo: {str(e)}')
    
    return render(request, 'enviar_correo.html')