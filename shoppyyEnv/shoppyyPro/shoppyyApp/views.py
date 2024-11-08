from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import ProductModel

# Create your views here.
def home(request):
    return render(request, "mainHTML/home.html")

def about(request):
    return render(request, "mainHTML/about.html")

def cart(request):
    return render(request, "mainHTML/cart.html")

def checkOut(request):
    return render(request, "mainHTML/checkOut.html")

def contact(request):
    return render(request, "mainHTML/contact.html")

def productDetails(request):
    return render(request, "mainHTML/productDetails.html")

def shop(request):
    all_products = ProductModel.objects.all

    return render(request, "mainHTML/shop.html", {"all_products" : all_products})

def wishlist(request):
    return render(request, "mainHTML/wishlist.html")

def addproduct(request):
    if request.method == "POST":
        product_name = request.POST["product_name"]
        product_price = request.POST["product_price"]
        product_discription = request.POST["product_discription"]
        product_color = request.POST["product_color"]
        product_quantity = request.POST["product_quantity"]
        product_category = request.POST["product_category"]
        product_image = request.FILES.get("product_image")


        if ((not product_name) or (not product_price) or (not product_discription) or (not product_color) or (not product_quantity) or (not product_category) or (not product_image)):
            messages.warning(request, "Fill all the fiels")
        elif ProductModel.objects.filter(product_name=product_name).exists():
            messages.warning(request, "product name is already exists")
        elif (product_image and (product_image.size > 1024 * 1024 or product_image.name.split('.')[-1].lower() not in ['jpg', 'jpeg', 'png'])):
            messages.warning(request, "Image size exceeds 1MB or Invalid image format")
        else:
           
            try:
                product = ProductModel(product_name = product_name, product_price = product_price, product_discription = product_discription, product_color = product_color, product_quantity = product_quantity, product_category = product_category, product_image = product_image)
                product.save()
                messages.success(request, "product added successfully") 
                # return redirect('myAccount') 
            except Exception as e:
            # Handle error during user creation
                messages.warning(request, f'Error: {str(e)}')       

    return render(request, "authHTML/myAccount.html")


