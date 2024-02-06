from django.shortcuts import render


def show_menu_test(request):
    return render(request, 'base.html')
