from django.http import HttpResponse
from django.template import loader

from .models import Goods


def index(request):
    goods_list = Goods.objects.order_by()
    template = loader.get_template("goods/index.html")
    context = {
        'goods_list': goods_list
    }
    return HttpResponse(template.render(context, request))
