from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
	def get(self,request):
		return render(request,'signup.html')

	def post(self,request):
		post_data=request.POST
		first_name=post_data.get('firstname')
		last_name=post_data.get('lastname')
		phone=post_data.get('Phone')
		email=post_data.get('email')
		password=post_data.get('password')
		values={"first_name":first_name,"last_name":last_name,"phone":phone,"email":email}
			
		customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)

		error_msg=self.validate_customer(customer)
		
			
		if not error_msg:
			print(first_name,last_name,phone,email,password)
			customer.password=make_password(customer.password)
			customer.register()
			return redirect('homepage')
		else:
			data={"error":error_msg,"values":values}
			return render(request,'signup.html',data)



	def validate_customer(self,customer):
		error_msg=None
		if(not customer.first_name):
				error_msg="First name required"

		elif customer.first_name:
			if len(customer.first_name)<4:
					error_msg="First name must be greater than 4"
		elif(not customer.last_name):
				error_msg="last name required"
		elif(not customer.phone):
				error_msg="phone number required"
		elif customer.isExist():
				error_msg="Email Already exist!!"

		return error_msg

