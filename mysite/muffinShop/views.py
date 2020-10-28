from datetime import datetime

from django.forms import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django import forms

from .forms import InputForm, NumberForm, OrderForm
from .models import OrderItem, Order, Product


#
class IndexView(generic.ListView):
    template_name = 'muffinShop/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return


def index(request):
    lists = Product.objects.order_by('product_number')[0:]
   # lists2 = Product.objects.all()도 가능
    form = InputForm()
    context = {
        'product_lists': lists,
        'form': form,
    }
    return render(request, 'muffinShop/index.html', context)


# order_item 종류와 개수 1개만
def new_order(request):
    form = InputForm(request.POST)  # index에서 넘어온 값을 form에 담는다
    if form.is_valid():  # form 이 유효하다면
        print('form is valid')
        quantity = form.clean()['quantity']  # 넘어온 quantity,product_number를 변수에 담고
        product_number = int(request.POST['product_number'])  # 어느방법이 맞는지 질문해야지;ㅅ;
        product = Product.objects.get(product_number=product_number)
        orderform = OrderForm()  # 새로운 폼을 보여주는데
        if request.method == "POST":
            print('request POST')  # 만약 요청받은 POST메소드가 있으면
            order = orderform.save(commit=False)  # 아직 저장하지말고
            order.order_date = datetime.now()  # order객체의 시간 설정하고
            order.save()
            print(order.order_id)
            orderitem = OrderItem.objects.create(
                product_id=product.product_id,
                order_id=order.order_id,
                quantity=quantity
            )
            total_price = product.price * quantity
            order_form = OrderForm()
            context = {
                'quantity': quantity,
                'product': product,
                'total_price': total_price,
                'order_form': order_form,
                'order': order
            }
            orderitem.save()
            print(f'orderitem.order {orderitem.order}')
            return render(request, 'muffinShop/order.html', context)
        else:
            print('else')
            context = {'form': form, 'orderform': orderform}
            return render(request, 'muffinShop/order.html', context)

    else:
        lists = Product.objects.all()
        form = InputForm()
        context = {
            'product_lists': lists,
            'form': form,
            'error_message': '입력양식이 잘못되어 처음으로 돌아옵니다.'
        }
        return render(request, "muffinShop/index.html", context)


def order_confirm(request):
    form = OrderForm(request.POST)
    print('order confirm')
    if form.is_valid():
        order = Order.objects.last()
        order.user_name = form.cleaned_data['user_name']
        order.user_phone = form.cleaned_data['user_phone']
        order.user_address = form.cleaned_data['user_address']
        orderitem = OrderItem.objects.filter(order=order.order_id)
        order.save()
        print(order.order_id)
        print('get orderitem')
        print(orderitem)
        list = []
        total_price = 0
        for item in orderitem:
            product = Product.objects.get(product_id=item.product_id)
            product_name = product.product_name
            price = product.price
            qt = item.quantity
            item_price = price * qt
            total_price += item_price
            str = f"{product_name}{product.category}({price}) X {qt} = {item_price}\n"
            list.append(str)
        order.total_price = total_price
        order.save()
        context = {'order': order, 'orderitem': orderitem, 'list': list}
        return render(request, 'muffinShop/confirm.html', context)
    else:
        lists = Product.objects.all()
        form = InputForm()
        context = {
            'product_lists': lists,
            'form': form,
            'error_message': '입력양식이 잘못되어 처음으로 돌아옵니다.'
        }
        return render(request, "muffinShop/index.html", context)

def order(request):
    form = InputForm(request.POST)  # 받아온 inputform
    if form.is_valid():
        # .is_valid() 를 통해서 검증에 통과한 값은 cleaned_data 변수명으로 사전타입 으로 제공된다.
        quantity = form.cleaned_data['quantity']
        product_number = form.cleaned_data['product_number']
        product = Product.objects.get(product_id=product_number)
        total_price = product.price * quantity
        if request.method == "POST":
            order_form = OrderForm()
            context = {
                'quantity': quantity,
                'product_id': product_number,
                'product': product,
                'total_price': total_price,
                'order_form': order_form,

            }
            if order_form.is_valid():
                return render(request, 'muffinShop/order/confirm.html', context)
            else:
                del context['order_form']
                context['order_form'] = OrderForm()
                return render(request, 'muffinShop/order.html', context)
    else:
        # cleaned_data는 메타클래스 꺼,,,
        return render(request, 'muffinShop/confirm.html')


def check(request):
    form = NumberForm()
    return render(request, 'muffinShop/check.html', {'form': form})


def check_order(request):
    form = NumberForm(request.POST)
    if form.is_valid():
        number = form.cleaned_data['number']
        order_info = Order.objects.filter(user_phone=number)
        list = []
        for order in order_info:
            order_id = order.order_id
            orderItem_info = OrderItem.objects.filter(order_id=order_id)
            list.append(f"\n{order.user_name}님의 주문내역\n 주문일 {order.order_date} \n "
                        f"지불비용 {order.total_price}\n"
                        f" 전화번호 {order.user_phone} \n 주소 {order.user_address} \n")
            for item in orderItem_info:
                product = Product.objects.get(product_id=item.product_id)
                product_name = product.product_name
                price = product.price
                qt = item.quantity
                item_price = price * qt
                str = f"{product_name}{product.category}({price}) X {qt} = {item_price}\n"
                list.append(str)
        context = {
            'orderInfo': order_info,
            'orderItem_info': orderItem_info,
            'list': list,
        }
        return render(request, 'muffinShop/check_phone.html', context)
    else:
        return render(request, 'muffinShop/check.html', {'form': form})


def test(request):
    return HttpResponse('<h1>hello</h1>')
