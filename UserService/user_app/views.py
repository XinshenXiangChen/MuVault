from django.shortcuts import render

def test_login(request):
    print()
    return render(request, 'user_app/test_login.html')
