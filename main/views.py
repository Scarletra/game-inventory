from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Name': 'World Lock',
        'Amount': '5'
    }

    return render(request, "main.html", context)
