from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Kopi Hitam w/ Ampas' ,
        'amount': 99 ,
        'description': 'Kopi hitam nikmat yang membantu Anda untuk menjalani seluruh kegiatan ' \
                       'sehari-hari ditambah ampas-nya untuk membantu pencernaan',
        'price': 4000 ,
    }

    return render(request, "main.html", context)