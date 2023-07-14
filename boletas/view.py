from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

import datetime

def transformar(request):
    if request.method == "POST":
        n_boleta = request.POST.get('n_boleta')
        cantidad1 = request.POST.get('cantidad1')
        cantidad2 = request.POST.get('cantidad2')  if request.POST.get('cantidad2') else 0
        cantidad3 = request.POST.get('cantidad3')  if request.POST.get('cantidad3') else 0
        cantidad4 = request.POST.get('cantidad4')  if request.POST.get('cantidad4') else 0
        cantidad5 = request.POST.get('cantidad5')  if request.POST.get('cantidad5') else 0
        cantidad6 = request.POST.get('cantidad6')  if request.POST.get('cantidad6') else 0
        cantidad7 = request.POST.get('cantidad7')  if request.POST.get('cantidad7') else 0
        producto1 = request.POST.get('producto1')
        producto2 = request.POST.get('producto2')
        producto3 = request.POST.get('producto3')
        producto4 = request.POST.get('producto4')
        producto5 = request.POST.get('producto5')
        producto6 = request.POST.get('producto6')
        producto7 = request.POST.get('producto7')
        unit1 = request.POST.get('unit1')
        unit2 = request.POST.get('unit2') if request.POST.get('unit2') else 0
        unit3 = request.POST.get('unit3') if request.POST.get('unit3') else 0
        unit4 = request.POST.get('unit4') if request.POST.get('unit4') else 0
        unit5 = request.POST.get('unit5') if request.POST.get('unit5') else 0
        unit6 = request.POST.get('unit6') if request.POST.get('unit6') else 0
        unit7 = request.POST.get('unit6') if request.POST.get('unit7') else 0
        importe1 = int(cantidad1)*int(unit1)
        importe2 = int(cantidad2)*int(unit2)
        importe3 = int(cantidad3)*int(unit3)
        importe4 = int(cantidad4)*int(unit4)
        importe5 = int(cantidad5)*int(unit5)
        importe6 = int(cantidad6)*int(unit6)
        importe7 = int(cantidad7)*int(unit7)
        total = importe1+importe2+importe3+importe4+importe5+importe6+importe7
        if cantidad2==0:
            cantidad2=' '
            unit2=' '
            importe2=' '
        if cantidad3==0:
            cantidad3=' '
            unit3=' '
            importe3=' '
        if cantidad4==0:
            cantidad4=' '
            unit4=' '
            importe4=' '
        if cantidad5==0:
            cantidad5=' '
            unit5=' '
            importe5=' '
        if cantidad6==0:
            cantidad6=' '
            unit6=' '
            importe6=' '
        if cantidad7==0:
            cantidad7=' '
            unit7=' '
            importe7=' '
        agregado = request.POST.get('agregado')
        fecha = datetime.date.today()

        context = {
            'n_boleta': n_boleta,
            'fecha':fecha,
            'cantidad1':cantidad1,
            'cantidad2':cantidad2,
            'cantidad3':cantidad3,
            'cantidad4':cantidad4,
            'cantidad5':cantidad5,
            'producto1':producto1,
            'producto2':producto2,
            'producto3':producto3,
            'producto4':producto4,
            'producto5':producto5,
            'unit1':unit1,
            'unit2':unit2,
            'unit3':unit3,
            'unit4':unit4,
            'unit5':unit5,
            'importe1':importe1,
            'importe2':importe2,
            'importe3':importe3,
            'importe4':importe4,
            'importe5':importe5,
            'total':total,
        }

        html = render_to_string("transformado.html", context)

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = "inline; report.pdf"

        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)

        return response

    return render(request, "boleta.html")

def inicio(request):

    return render(request, "boleta.html")