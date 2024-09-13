from django.shortcuts import render

def show_home(request):
    context = {
        'nama': 'Valentino Kim Fernando',  
        'kelas': 'PBP F',
        'items': [
            {'name': 'Es Kulkul Uni Bakwan', 'price': 70, 'description': 'Es Kulkul Uni Bakwan, es asli dari Uni Bakwan Onde Mande', \
             'image': 'https://i.pinimg.com/736x/42/b1/22/42b12243ca70053a7c6f22241787f271.jpg'},
            {'name': 'Ayam Goreng Bunda Mewing', 'price': 25, 'description': 'Merupakan salah satu ayam goreng langka yang dibuat oleh \
             bunda yang mewing.', 'image': 'https://steamuserimages-a.akamaihd.net/ugc/2270441744978599352/3A97A06E3670819C1E5A4525DED7FBF4DAC5DE21/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false'},
            {'name': 'Odading ', 'price': 25, 'description': 'Merupakan salah satu ayam goreng langka yang dibuat oleh \
             bunda yang mewing.', 'image': 'https://steamuserimages-a.akamaihd.net/ugc/2270441744978599352/3A97A06E3670819C1E5A4525DED7FBF4DAC5DE21/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false'},
            
        ],
    }
    return render(request, 'home.html', context)