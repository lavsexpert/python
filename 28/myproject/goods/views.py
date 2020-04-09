from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import AddToBasket
from .models import Goods, Basket


def index(request):
    goods_list = Goods.objects.order_by()
    template = loader.get_template("goods/index.html")
    context = {
        'goods_list': goods_list
    }
    return HttpResponse(template.render(context, request))


def basket(request):
    basket_list = Basket.objects.order_by()
    sum = 0
    for item in basket_list:
        item.total = item.count * item.price
        sum += item.total
    template = loader.get_template("goods/basket.html")
    context = {
        'basket_list': basket_list,
        'sum': sum
    }
    return HttpResponse(template.render(context, request))


def result(request):
    template = loader.get_template("goods/result.html")
    context = {}
    return HttpResponse(template.render(context, request))


def add(request):
    if request.method == 'GET':
        form = AddToBasket(request.GET)
        goods = Goods.objects.get(id=form.id)
        goods.count -= form.count
        goods.save()
        return HttpResponseRedirect("/")