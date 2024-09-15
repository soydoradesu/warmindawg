from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.core import serializers
from .forms import MenuForm

def show_home(request):
    default_items = [
        {
            'name': 'Es Kulkul Uni Bakwan', 
            'price': 70, 
            'description': 'Es Kulkul Uni Bakwan, es asli dari Uni Bakwan Onde Mande',
            'image': 'https://i.pinimg.com/736x/42/b1/22/42b12243ca70053a7c6f22241787f271.jpg'
        },
        {
            'name': 'Ayam Goreng Bunda Mewing', 
            'price': 25, 
            'description': 'Merupakan salah satu ayam goreng langka yang dibuat oleh bunda yang mewing.',
            'image': 'https://steamuserimages-a.akamaihd.net/ugc/2270441744978599352/3A97A06E3670819C1E5A4525DED7FBF4DAC5DE21/?imw=512&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false'
        },
        {
            'name': 'Mie Keriting', 
            'price': 16, 
            'description': 'Mie keriting! AWAS bisa membuatmu giting...',
            'image': 'https://i.ytimg.com/vi/-7uwIsEe1jY/maxresdefault.jpg'
        }
    ]

    # Fetching items from the database
    db_items = Item.objects.all()

    # Converting QuerySet to list of dicts to unify with default items format
    items_from_db = [{'name': item.name, 'price': item.price, 'description': item.description, 'image': item.image} for item in db_items]

    # Combining default items with database items
    all_items = default_items + items_from_db

    context = {
        'nama': 'Valentino Kim Fernando',
        'kelas': 'PBP F',
        'items': all_items,
    }

    return render(request, 'home.html', context)

def add_menu_item(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MenuForm()
    return render(request, 'add_menu.html', {'form': form})

def menu_list_json(request):
    data = serializers.serialize('json', Item.objects.all())
    return HttpResponse(data, content_type='application/json')

def menu_list_xml(request):
    data = serializers.serialize('xml', Item.objects.all())
    return HttpResponse(data, content_type='application/xml')

def menu_detail_json(request, pk):
    data = serializers.serialize('json', [Item.objects.get(pk=pk)])
    return HttpResponse(data, content_type='application/json')

def menu_detail_xml(request, pk):
    data = serializers.serialize('xml', [Item.objects.get(pk=pk)])
    return HttpResponse(data, content_type='application/xml')

def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect('/')