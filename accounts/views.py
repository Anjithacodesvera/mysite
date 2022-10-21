from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from accounts.forms import UserAdminCreationForm
# from accounts.forms import UserAdminCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from .models import  CustomUser
from django.views import generic, View
from .forms import SignupForm
from .models import  Signup
from django.contrib.auth.hashers import  make_password
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
# def register(req):
#     form =UserAdminCreationForm()
#     if req.method == 'POST':
#         form = UserAdminCreationForm(req.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('register')
#     return render(req, 'accounts/register.html', {'form': form})

# def login_page(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect('')
#         else:
#             messages.info(request, 'Try again! username or password is incorrect')
#
#     context = {}
#     return render(request, 'login.html', context)
# from django.contrib.auth.forms import AuthenticationForm
# def Login(request):
#     if request.method == 'POST':
#         print("<------------->")
#         # AuthenticationForm_can_also_be_used__
#
#         email= request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         print(user,'......>>>>>>')
#         user1 = CustomUser.objects.get(email=email)
#
#         print("<==============>",user)
#         if user is not None:
#             print("#################")
#             return redirect('/page/')
#         else:
#             print("not found")
        # try:
        #     user = CustomUser.objects.get(email=email,password=password)
        #     Login(request, user)
        #     messages.success(request, f' welcome {email} !!')
        #     print("!!!!!!!!!!!!!!!!!!!!!!!")
        #     return redirect('page')
        # except:
        #     messages.info(request, f'account done not exit plz sign in')
        # if user is not None:
        #     form = login(request, user)
        #     messages.success(request, f' welcome {email} !!')
        #     return redirect('index')
        # else:
        #     messages.info(request, f'account done not exit plz sign in')
    # form = AuthenticationForm()
    # return render(request, 'registration/login.html', {'form': form, 'title': 'log in'})
def function_r(request):
    return render(request,'registration/page.html')


def methods(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if form.is_valid():
            print("<#########################>")
            user = form.save()
            Signup.objects.create(Users = user, phone_number=phone_number, address=address)
            user.set_password(request.POST.get('password'))
            user.save()
            return redirect('/login/')
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.",form.errors)
            context = {
                "form": form
            }
            return render(request, 'registration/signup.html', context)



            #phone_number= request.POST.get('phone_number')
            #address= request.POST.get('address')
            # first_name=request.POST.get('first_name')
            # last_name=request.POST.get('last_name')
            # email= request.POST.get('email')
            # password = request.POST.get('password')
            # password2= request.POST.get('password2')
            # username= request.POST.get('username')
            # if password!=password2:
            #     messages.info(request, "password not taken")

            # user = User.objects.create_user(password=password2, email=email, first_name=first_name,username=username, e,
            #                                 last_name=last_name)
            # Signup.objects.create(Users=user, phone_number=phone_number, address=address)
            # user.set_password(request.POST.get('password'))

            # return redirect('/login/')


        # else:
        #     print("<--------------->", SignupForm.errors)
        #     return HttpResponse
        #     Response("not valid")
        #     context = {
        #         "form" : form
        #     }
        #     return render(request,'registration/signup.html', context)
    context = {}
    context['form'] = SignupForm()
    return render(request,'registration/signup.html',context)

class Login(View):
    def get(self,request):
          return render(request, 'registration/login.html')
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect('/page/')
            else:
                print("not found")
                return redirect('/login/')
        except:
            print("not founddddddddddd")
        form = AuthenticationForm()

        return render(request, 'login.html', {'form': form, 'title': 'log in'})



from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import  Question

def home(request):
    return HttpResponse("i am anjitha")

def ajaxhome(request):
    return render(request, 'account/index.html')

class ajaxcall(View):
     def post(self, request):
        question = request.POST.get('question')

        Question.objects.create(question=question)
        qs= Question.objects.all()
        li=[]
        for i in qs:
            li.append(i.question)
        return JsonResponse({"qs": li})







