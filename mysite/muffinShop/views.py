from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from .forms import InputForm, NumberForm, OrderForm
from .models import OrderItem, Order, Product


def index(request):
    if request.method == 'GET':
        products = Product.objects.all()
        form = InputForm()
        print('inputform()')
        context = {
            'products': products,
            'form': form,
        }
        return render(request, 'muffinShop/index.html', context)
    else:
        context = {
            'error_message': '현재 준비중인 상품이 없습니다',
        }
        return render(request, 'muffinShop/index.html', context)


def order(request):
    if request.method == 'POST':
        quantity = request.POST['quantity']
        product_number = request.POST['product_number']
        product = Product.objects.get(product_number=product_number)
        print(quantity)
        print(product_number)
        total_price = int(quantity) * int(product.price)  # 받아온 값은 str,형변환 필요
        order_form = OrderForm()
        context = {
            'quantity': quantity,
            'product': product,
            'order_form': order_form,
            'total_price': total_price
        }
        return render(request, 'muffinShop/order.html', context)
    else:
        products = Product.objects.all()
        form = InputForm()
        context = {
            'products': products,
            'form': form,
            'error_message': '다시 골라주세요',
        }
        return render(request, 'muffinShop/index.html', context)


def confirm(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            quantity = request.POST['quantity']
            product_id = request.POST['product_id']
            product = Product.objects.get(product_id=product_id)
            print(product_id)
            print(quantity)
            order = order_form.save()
            order.total_price = int(product.price) * int(quantity)
            order.order_date = datetime.now().strftime("%Y-%m-%d %H:%M")
            order.save()
            orderitem = OrderItem.objects.create(
                order_id=order.order_id,
                product_id=product_id,
                quantity=quantity,
            )
            orderitem.save()
            context = {
                'order': order,
                'orderitem' : orderitem,
                'product':product,
            }
            return render(request, 'muffinShop/confirm.html', context)
        else:
            products = Product.objects.all()
            form = InputForm()
            context = {
                'products': products,
                'form': form,
                'error_message': '입력양식이 잘못되어 처음으로 돌아옵니다.',
            }
            return render(request, 'muffinShop/index.html', context)
    else:
        products = Product.objects.all()
        form = InputForm()
        context = {
            'products': products,
            'form': form,
            'error_message': '입력양식이 잘못되어 처음으로 돌아옵니다.',
        }
        return render(request, 'muffinShop/index.html', context)



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
            orderitem_info = OrderItem.objects.filter(order_id=order_id)
            order_date = order.order_date.strftime("%Y-%m-%d")
            list.append(f"\n{order.user_name}님의 주문내역\n 주문일 {order_date} \n "
                        f"지불비용 {order.total_price}\n"
                        f" 전화번호 {order.user_phone} \n 주소 {order.user_address} \n")
            for item in orderitem_info:
                product = Product.objects.get(product_id=item.product_id)
                product_name = product.product_name
                price = product.price
                qt = item.quantity
                item_price = price * qt
                str = f"{product_name}{product.category}({price}) X {qt} = {item_price}\n"
                list.append(str)
        context = {
            'order_info': order_info,
            'orderitem_info': orderitem_info,
            'list': list,
        }
        return render(request, 'muffinShop/check_phone.html', context)
    else:
        return render(request, 'muffinShop/check.html', {'form': form})


def test(request):
    return HttpResponse('<h1>hello</h1>')
