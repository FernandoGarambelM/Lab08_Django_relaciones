from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import get_template
from django.shortcuts import render
from xhtml2pdf import pisa
from .models import Lenguage, Framework, Movie, Character
from django.core.mail import EmailMessage
from io import BytesIO

def index(request):
    return HttpResponse("Hello, world!")

def generar_pdf(request):
    template_path = 'plantilla_pdf.html'
    context = {
        'lenguages': Lenguage.objects.all(),
        'frameworks': Framework.objects.all(),
        'movies': Movie.objects.all(),
        'characters': Character.objects.all()
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="datos_modelos.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF: %s' % pisa_status.err)
    return response

def enviar_correo(request):
    context = {
        'lenguages': Lenguage.objects.all(),
        'frameworks': Framework.objects.all(),
        'movies': Movie.objects.all(),
        'characters': Character.objects.all()
    }

    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        destinatario = request.POST['destinatario']
        remitente = 'tu_correo@gmail.com'  # Cambia esto por tu correo

        if 'send_plain' in request.POST:
            try:
                send_mail(asunto, mensaje, remitente, [destinatario])
                return HttpResponse('Correo enviado exitosamente')
            except Exception as e:
                return HttpResponse(f'Error al enviar el correo: {str(e)}')

        elif 'send_pdf' in request.POST:
            template_path = 'plantilla_pdf.html'
            template = get_template(template_path)
            html = template.render(context)

            result = BytesIO()
            pisa_status = pisa.CreatePDF(html, dest=result)

            if pisa_status.err:
                return HttpResponse('Hubo un error al generar el PDF: %s' % pisa_status.err)

            email = EmailMessage(
                asunto,
                mensaje,
                remitente,
                [destinatario]
            )

            email.attach('datos_modelos.pdf', result.getvalue(), 'application/pdf')
            email.send()

            return HttpResponse('Correo con PDF enviado exitosamente')

    return render(request, 'enviar_correo.html', context)

def enviar_pdf_por_correo(request):
    template_path = 'plantilla_pdf.html'
    context = {
        'lenguages': Lenguage.objects.all(),
        'frameworks': Framework.objects.all(),
        'movies': Movie.objects.all(),
        'characters': Character.objects.all()
    }

    template = get_template(template_path)
    html = template.render(context)
    
    result = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=result)
    
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF: %s' % pisa_status.err)
    
    email = EmailMessage(
        'Datos de Modelos',
        'Adjunto encontrarás el PDF con los datos de los modelos.',
        'tu_correo@gmail.com',
        ['destinatario@gmail.com']
    )
    
    email.attach('datos_modelos.pdf', result.getvalue(), 'application/pdf')
    email.send()
    
    return HttpResponse('Correo enviado exitosamente')