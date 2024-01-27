from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(req):
    items = Tovar.objects.all()
    data = {'tovari': items}
    return render(req, 'index.html', data)


def toCart(req):
    items = Cart.objects.filter(user=req.user)
    forma = OrderForm()
    total = 0
    for i in items:
        total += i.calcSumma()
    total = round(total, 2)

    if req.POST:
        forma = OrderForm(req.POST)
        k1 = req.POST.get('adres')
        k2 = req.POST.get('tel')
        k3 = req.POST.get('email')
        print(k1, k2, k3)
        if forma.is_valid():
            k1 = forma.cleaned_data.get('adres')
            k2 = forma.cleaned_data.get('tel')
            k3 = forma.cleaned_data.get('email')
            print(k1, k2, k3)
            myzakaz = ''
            for one in items:
                myzakaz += one.tovar.name + ' '
                myzakaz += 'Кол-во: ' + str(one.count) + ' шт. '
                myzakaz += 'Сумма: ' + str(one.summa) + ' р. '
                myzakaz += 'Скидка: ' + str(one.tovar.discount) + ' % '
            Order.objects.create(
                adres=k1,
                tel=k2,
                emil=k3,
                total=total,
                myzakaz=myzakaz,
                user=req.user
            )
            items.delete()
            return render(req, 'sps.html')
    data = {'tovari': items, 'total': total, 'formaorder': forma}
    return render(req, 'cart.html', data)


def buy(req, id):
    item = Tovar.objects.get(id=id)
    curuser = req.user
    if Cart.objects.filter(tovar=item, user=curuser):
        getTovar = Cart.objects.get(tovar_id=id)
        getTovar.count += 1
        getTovar.summa = getTovar.calcSumma()
        getTovar.save()
    else:
        Cart.objects.create(tovar=item, count=1, user=curuser, summa=item.price)
    data = {}
    return redirect('home')


def delete(req, id):
    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('tocart')


def cartCount(req, num, id):
    num = int(num)
    item = Cart.objects.get(id=id)
    item.count += num
    if item.count < 0:
        item.count = 0
    item.summa = item.calcSumma()
    item.save()
    return redirect('tocart')
