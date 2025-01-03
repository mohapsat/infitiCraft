from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from icapp.models import Btn

def home(request):
    btns = Btn.objects.all()
    print(btns)
    context = {
        "btns": btns,
    }
    return render(request, 'home.html', context=context)

@csrf_exempt
def refreshBtnItems(request):
    data = dict()
    if request.method == 'POST':
        btns = Btn.objects.all()
        context = {
            "btns": btns,
        }
        data['btns_html'] = render_to_string(
            template_name='includes/btnItems.html',
            context=context,
        )
    else:
        data = {"status": "it's working!"}

    return JsonResponse(data)