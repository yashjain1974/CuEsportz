from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, auth
from accounts.models import UserDetail, UserPassword
from . import backends


# Create your views here.
def home(request):
    return HttpResponse("Home Page")

def registration(request):
    return render(request, 'registration.html')

def signIn(request):
    # fetching data from registration form
    if request.method == 'POST':
        user_mob = request.POST.get('user_mob')
        password = request.POST['password']

        # sign in with username
        user = auth.authenticate(username=user_mob, password=password)
        if user is not None:      # log in done
            # auth.login(request, user)

            return render(request, 'join_Host.html')
        else: 
            with open('templates/totaluser.txt', 'r') as file:
                total = file.read()
                total_user = int(total)

            i = 1 
            try:
                # it is a linear search by id but if user is not registerred then exiting the loop before ending the loop
                for i in range(1, total_user + 1):  # only need to fix it
                    try:
                        obj1 = UserDetail.objects.get(id=i)
                    except: pass
                    try:
                        obj2 = UserPassword.objects.get(id=i)
                    except: pass
                    mob_no = str(obj1)
                    password1 = str(obj2)
                    if mob_no == user_mob:
                        if password == password1:
                            return render(request, 'join_Host.html')
                        else: return HttpResponse("password incorrect")
            except: return HttpResponse("iteration failed")

            # signin with mobile number

    return HttpResponse("signed in failed")

def signUp(request):
    if request.method == 'POST':
        # extracting data from registration form
        name = request.POST['name']
        email = request.POST['email']
        mob_no = request.POST['mob']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        ref_code = request.POST['reffral_code']

        # checking password mismatch
        if password2 == password1:
            password = password1
        else: return HttpResponse("password does not match with previous password")

        # generate username
        username = backends.generateUserName(name=name)

        # pushing data in data base using User and UserDetail model
        user = User.objects.create_user(username=username, first_name=name, password=password, email=email)
        user.save()
        user_detatil = UserDetail(user=user, mob_no=mob_no, ref_code=ref_code)
        user_detatil.save()
        user_password = UserPassword(user=user, password=password)
        user_password.save()

        with open('templates/totaluser.txt', 'r') as file:
            total = file.read()
            count = int(total)

        # we are checking here that data is pushed or not
        if user is not None:
            if user_detatil is not None:
                if user_password is not None:
                    count += 1
                    with open('templates/totaluser.txt', 'w') as file:
                        file.write(str(count))
                    return render(request, 'registration.html')
                else: return HttpResponse("Data is not saved in UserPassword model")
            else: return HttpResponse("Data is not saved in data base in UserDetail model")
        else: return HttpResponse("Data is not saved in data base in User Model")

    return HttpResponse("signing up failed")

def joinPage(request):
    return render(request, 'join.html', {})

def walletPage(request):
    return render(request, 'wallet.html', {})
