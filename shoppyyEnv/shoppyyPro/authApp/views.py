from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from shoppyyApp.models import ProductModel


# Create your views here.


# Registration function
def registration(request):
   
    if request.method == "POST":
        # name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        conformPassword = request.POST["conformPassword"]
        # mobileno = request.POST["mobileno"]
        # image = request.FILES.get("image")

      

       # 1. check tha all fields
        if ((not email) or (not password) or (not conformPassword)):
            messages.warning(request, "Fill all the fiels")
           # print("Fill all the fiels")
        elif User.objects.filter(username=email).exists():
            messages.warning(request, "Email already exists")
            # print("Email already exists")
        elif (password != conformPassword):
            messages.warning(request, "password mismatch") 
            # print("new user created")
        # elif (image and (image.size > 1024 * 1024 or image.name.split('.')[-1].lower() not in ['jpg', 'jpeg', 'png'])):
        #     messages.warning(request, "Image size exceeds 1MB or Invalid image format")
        # elif (len(mobileno) != 10):
        #     messages.warning(request, "Mobile Number Must be 10 digits")
        else:
            # try:
            #     salt = bcrypt.gensalt()
            #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            # except Exception as e:
            #     messages.warning(request, str(e))


            try:
                user = User.objects.create_user(email,email,password)    
                user.save()

                # messages.success(request, "Your registration successfully") 
                return redirect('login') 
            except Exception as e:
            # Handle error during user creation
                messages.warning(request, f'Error: {str(e)}')       


    return render(request, "authHTML/registration.html")


# login function
def login_user(request):


    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]


        if ((not email) or (not password)):
            messages.warning(request, "please fill the fiels")

        else:
            myuser = authenticate(username = email, password = password)
   
            if myuser is not None:
                login(request,myuser)
                messages.success(request,"Login Success")
                return redirect('/')

            else:
                messages.error(request,"Invalid Credentials")
                return redirect('login')


   
    return render(request, "authHTML/login.html")



def logout_view(request):
    logout(request)
    # Add success message and redirect to login page
    messages.success(request, 'You have been logged out!')
    return redirect('login')  # Replace 'login' with your login URL pattern name


def myAccount(request):
    all_products = ProductModel.objects.all
    return render(request, "authHTML/myAccount.html", {"all_products_variable" : all_products})

def password_changing(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]

        if (not password) or (not confirmpassword):
            messages.warning(request, "Enter the password")
        elif (password != confirmpassword):
            messages.warning(request, "password mismatch")  
        else:
            update = User.objects.get(username=email)
            update.set_password(password)
            update.save()
            messages.success(request, "Password updated successfully!")
            logout(request)
            return redirect('login')

            # user = authenticate(username=email, password=request.user.password)

            # if user is not None:
            #     # Update password securely using update_password
            #     update_password(user, password)
            #     messages.success(request, "Password updated successfully!")
            #     logout(request)
            #     return redirect('login')  # Replace with your URL
            # else:
            #     messages.warning(request, "Incorrect current password")

    return render(request, "authHTML/myAccount.html")


