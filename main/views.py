from django.shortcuts import render

def show_home(request):
    context = {
        'nama': 'Valentino Kim Fernando',  
        'kelas': 'PBP F',
        'items': [
            {'name': 'Es Kulkul Uni Bakwan', 'price': 70.000, 'description': 'Es Kulkul Uni Bakwan, es asli dari Uni Bakwan Onde Mande', \
             'image': 'static/images/unibakwan.png'},
            {'name': 'Ayam Goreng Bunda Mewing', 'price': 25.000, 'description': 'Merupakan salah satu ayam goreng langka yang dibuat oleh \
             bunda yang mewing.', 'image': 'static/images/mewing.png'},
            # Add more items as needed
        ],
    }
    return render(request, 'home.html', context)