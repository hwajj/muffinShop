from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        MUFFIN = ' Muffin'
        COOKIE = ' Cookie'
        CUPCAKE = ' Cupcake'

    product_id = models.AutoField(primary_key=True )
    product_number = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=10, choices=Category.choices)
    product_name = models.CharField(max_length=50, )
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product_name + self.category

    def product_full_name(self):
        return f'{self.product_name} +{self.category}'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=10, null=True)
    user_phone = models.CharField(max_length=15, null=True)
    user_address = models.CharField(max_length=50, null=True)

    # payment = models.
    def __str__(self):
        return str(self.order_id)


class OrderItem(models.Model):
    orderItem_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE,)
    product = models.ForeignKey('Product', on_delete=models.CASCADE,)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.order_id)
        #return f"order: {self.order_id}: {self.product_id} x {self.quantity}"
        # def orderId = ~ 오더아이디클래스에서 order_id 중 가장 가장 큰 수+1 해서 orderId에 집어넣고

# each_price = product.price * cart.quantity

# def totalPrice(self): each_price의 합

# 질문 ...진행 순서상 카트에 먼저 담기는데 카트에 먼저 order_id를 부여하면,
# order_id 를 foreign키로 해야하는지...

