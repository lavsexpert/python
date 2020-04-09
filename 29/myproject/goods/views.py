from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

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
    Basket.objects.all().delete()
    template = loader.get_template("goods/result.html")
    context = {}
    return HttpResponse(template.render(context, request))

def cancel(request):
    baskets = Basket.objects.all()
    for basket in baskets:
        try:
            goods = Goods.objects.get(name=basket.name)
        except Goods.DoesNotExist:
            goods = Goods()

        goods.name = basket.name
        goods.price = basket.price
        if goods.count == None:
            goods.count = basket.count
        else:
            goods.count += basket.count
        goods.save()

    baskets.delete()
    template = loader.get_template("goods/cancel.html")
    context = {}
    return HttpResponse(template.render(context, request))


def add(request):
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        count = int(request.POST.get('count'))

        goods = Goods.objects.get(id=id)
        goods.count -= count
        goods.save()

        try:
            basket = Basket.objects.get(goods_id=goods)
        except Basket.DoesNotExist:
            basket = Basket()

        basket.name = goods.name
        basket.goods_id = goods
        basket.price = goods.price
        if basket.count == None:
            basket.count = count
        else:
            basket.count += count
        basket.total = basket.count * basket.price
        basket.save()

    return HttpResponseRedirect("../goods")
