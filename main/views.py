from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama': 'Musthofa Joko Anggoro' ,
        'kelas': 'PBP E',
    }

    return render(request, "main.html", context)