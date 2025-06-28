from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("tasks:index")
    else:
        form = UserCreationForm()

    return render(request, "users/signup.html", {
        "form": form
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tasks:index')
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username or password"
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect('users:login')
