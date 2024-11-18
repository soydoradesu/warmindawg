import datetime
from itertools import chain
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Item
from .forms import MenuForm
import json

@login_required(login_url='/login')
def show_home(request):
    default_items = [
        {
            'user': {
                'username': 'Valen (default)'
            },
            'name': 'Es Kulkul Uni Bakwan', 
            'price': 70, 
            'description': 'Es Kulkul Uni Bakwan, es asli dari Uni Bakwan Onde Mande',
            'image': 'https://i.pinimg.com/736x/42/b1/22/42b12243ca70053a7c6f22241787f271.jpg'
        },
        {
            'user': {
                'username': 'Valen (default)'
            },
            'name': 'Ayam Goreng Bunda Mewing', 
            'price': 25, 
            'description': 'Merupakan salah satu ayam goreng langka yang dibuat oleh bunda yang mewing.',
            'image': 'https://steamuserimages-a.akamaihd.net/ugc/2270441744978599352/3A97A06E3670819C1E5A4525DED7FBF4DAC5DE21/?imw=512&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false'
        },
        {
            'user': {
                'username': 'Valen (default)'
            },
            'name': 'Mie Keriting', 
            'price': 16, 
            'description': 'Mie keriting! AWAS bisa membuatmu giting...',
            'image': 'https://i.ytimg.com/vi/-7uwIsEe1jY/maxresdefault.jpg'
        }
    ]

    # Fetching items from the database
    db_items = Item.objects.all()

    # Combining default items with database items
    all_items = list(chain(default_items, db_items))

    # my_entry = Item.objects.filter(user=request.user)

    context = {
        'nama': 'Valentino Kim Fernando',
        'kelas': 'PBP F',
        'items': all_items,
        # 'my_items': my_entry,
        'logo' : 'https://i.imgur.com/qm2xL9P.png',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'home.html', context)

def add_menu_item(request):
    form = MenuForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item_entry = form.save(commit=False)
        item_entry.user = request.user
        item_entry.save()
        return redirect('/')
    
    return render(request, 'add_menu.html', {'form': form})

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('home:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("home:show_home"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      
      else:
            messages.error(request, 'Username atau password kamu salah!')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('home:login'))
    response.delete_cookie('last_login')
    return response

def menu_list_json(request):
    # data = serializers.serialize('json', Item.objects.all())
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def menu_list_xml(request):
    # data = serializers.serialize('xml', Item.objects.all())
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def menu_detail_json(request, pk):
    data = serializers.serialize('json', [Item.objects.get(pk=pk)])
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def menu_detail_xml(request, pk):
    data = serializers.serialize('xml', [Item.objects.get(pk=pk)])
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def edit_menu(request, pk):
    # Get mood entry berdasarkan id
    menu = Item.objects.get(pk=pk)

    # Set mood entry sebagai instance dari form
    form = MenuForm(request.POST or None, instance=menu)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('home:show_home'))

    context = {'form': form}
    return render(request, "edit_menu.html", context)

def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('home:show_home'))

@csrf_exempt
@require_POST
def add_menu_item_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    image = request.POST.get("image")
    user = request.user
    username = user

    new_food = Item(name=name, price=price,
                    description=description, image=image, 
                    user=user, username=username)
    new_food.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_menu_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            image_data = data.get('image_url', '') 
            
            new_product = Item.objects.create(
                user=request.user,
                name=data['nama'], 
                price=int(data['harga']),
                description=data['deskripsi'],
                quantity=int(data['stok']),
                image=image_data  
            )
            
            return JsonResponse({
                "status": "success",
                "message": "Product berhasil ditambahkan!"
            }, status=200)
            
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=400)
            
    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    }, status=401)