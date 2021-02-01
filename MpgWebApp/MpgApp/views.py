from django.shortcuts import render
from django.http import HttpResponse

##from sklearn.externals import joblib
import joblib
# Create your views here.
reloadData = joblib.load('./models/RFModelforMPG.pkl')


def index(request):
    context = {'a': "Helloworld"}
    return render(request, 'index.html', context)
    # return HttpResponse({'a': 1})


def predictMPG(request):
    if request.method == 'POST':
        print(request.POST.dict())
        temp = {}
        temp['cylinderVal'] = request.POST.get('cylinderVal')
        temp['displaceVal'] = request.POST.get('displaceVal')
        temp['horsepwVal'] = request.POST.get('horsepwVal')
        temp['weightVal'] = request.POST.get('weightVal')
        temp['accVal'] = request.POST.get('accVal')
        temp['modelVal'] = request.POST.get('modelVal')
        temp['orginVal'] = request.POST.get('orginVal')
    context = {'a': "New Helloworld"}
    return render(request, 'index.html', context)
