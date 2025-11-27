from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages




def home(request):
    return render(request ,'home.html')


def about(request):
    return render(request,'about.html')


def products(request):
    return render(request,'products.html')



from .forms import ContactUsForm

# def contact_us(request):
#     if request.method == 'POST':
#         form = ContactUsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,'contact_success.html') 
#     else:
#         form = ContactUsForm()
#     return render(request, 'contact_us.html', {'form': form})
def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()


        # handle POST request
        return render(request,"contact_success.html")
    else:
         form = ContactUsForm()

        # handle GET request
    return render(request, 'contact_us.html',{'form':form})




from .models import SpecialFlower

def SpecialFlower_view(request):
    SpecialFlowers = SpecialFlower.objects.all()
    context = {'SpecialFlowers':SpecialFlowers}
    return render(request,'SpecialFlower.html',context)
    
# from django.shortcuts import render, redirect
# # from django.contrib.auth import login
# # from django.contrib.auth.decorators import login_required
# # from django.contrib.auth.forms import AuthenticationForm
# # from django.contrib import messages

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')  # Redirect to a success page.
#         else:
#             messages.error(request, 'Invalid username or password.')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# @login_required
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request,("you have been logged out...."))
    return redirect('login')

    
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    form = UserCreationForm()
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)



# booking


from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm

# Create a new booking
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

# Read (list) all bookings
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

# Update an existing booking
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'form': form})

# Delete an existing booking
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking_confirm_delete.html', {'booking': booking})




# order

from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})