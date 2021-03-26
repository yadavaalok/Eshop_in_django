from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
class Checkout(View):
	def post(self,request):
		address=request.POST.get('address')
		phone=request.POST.get('phone')
		customer=request.session.get('customer')
		cart=request.session.get('cart')
		products=Product.get_products_by_id(list(cart.keys()))
		print(address,phone,customer,cart,products)
		if customer:
			for p in products:
				order=Order(product=p,customer=Customer(id=customer),price=p.price,address=address,phone=phone,quantity=cart.get(str(p.id)))
				order.place_order()
			request.session['cart']={}
			return redirect('cart')
		else:
			return redirect('login')