from trycourier import Courier
from datetime import date
from django.shortcuts import render,redirect
from profiles.models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from profiles.forms import SignupForm
from profiles.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
import requests
import json
import pytz
def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'mob': user.profile.mob})

m = None
pro = None


def signup_view(request):
    captcha_var = None #captcha k maslay  mx
    error_given = None # email k maslay
    global pro
    global m

    pro = request.session.get('ref_profile')
    profile_id = request.session.get('ref_profile')
    form = SignupForm(request.POST or None)
    www = str(form)
    # name= www.find("username value=")
    if request.user.is_authenticated:
        return redirect('main-view')
    elif form.is_valid():
        k = request.POST['g-recaptcha-response']
        sk = "6LfMD0kdAAAAAEMJ87ZvANZH6CbArO9cB2Oe_CA9"
        captcha={
            "secret":sk,
             "response":k
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captcha)
        res = json.loads(r.text)
        veri = res['success']
        if veri == True:
            if profile_id is not None:
                
                recommended_by_profile = Profile.objects.get(id = profile_id) 
                
                ree = Profile.objects.filter(id=profile_id).values()
                x = list(ree[0].values())
                print(x,'sdasdsadasdasdsadsadsadasdasdasdsa')
                a  = str(form)
                emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
                find = a.find('name="email" value=')
                find2 = a.find('required id="id_email"')
                act = str(form)[find+20:find2-2]
                if act in emails:
                    error_given = "Email already Exist"
                else:
                    instance = form.save()
                
                    instance.profile.mob = form.cleaned_data.get('mob')
                    update_user_data(instance)
                    registered_user = User.objects.get(id=instance.id)
                    registered_profile = Profile.objects.get(user=registered_user)
                    registered_profile.recommended_by = recommended_by_profile.user
                    if x[4] is  None:
                        registered_profile.save()
                    else:
                        recommended_by_profile1 = Profile.objects.get(id = x[4])
                        registered_profile.recommended_by1 = recommended_by_profile1.user
                        registered_profile.save()
                    
                    if x[5] is None:
                        pass
                    else:
                        recommended_by_profile2 = Profile.objects.get(id = x[5])
                        registered_profile.recommended_by2 = recommended_by_profile2.user
                        registered_profile.save()
                    if x[6] is None:
                        pass
                    else:
                        recommended_by_profile3 = Profile.objects.get(id = x[6])
                        registered_profile.recommended_by3 = recommended_by_profile3.user
                        registered_profile.save()
                    if x[7] is None:
                        pass
                    else:
                        recommended_by_profile4 = Profile.objects.get(id = x[7])
                        registered_profile.recommended_by4 = recommended_by_profile4.user
                        registered_profile.save()
                    if x[8] is None:
                        pass
                    else:
                        recommended_by_profile5 = Profile.objects.get(id = x[8])
                        registered_profile.recommended_by5 = recommended_by_profile5.user
                        registered_profile.save()
                    if x[9] is None:
                        pass
                    else:
                        recommended_by_profile6 = Profile.objects.get(id = x[9])
                        registered_profile.recommended_by6 = recommended_by_profile6.user
                        registered_profile.save()
                    if x[10] is None:
                        pass
                    else:
                        recommended_by_profile7 = Profile.objects.get(id = x[10])
                        registered_profile.recommended_by7 = recommended_by_profile7.user
                        registered_profile.save()
                    if x[11] is None:
                        pass
                    else:
                        recommended_by_profile8 = Profile.objects.get(id = x[11])
                        registered_profile.recommended_by8 = recommended_by_profile8.user
                        registered_profile.save()
                    if x[12] is None:
                        pass
                    else:
                        recommended_by_profile9 = Profile.objects.get(id = x[12])
                        registered_profile.recommended_by9 = recommended_by_profile9.user
                        registered_profile.save()
                    if x[13] is None:
                        pass
                    else:
                        recommended_by_profile10 = Profile.objects.get(id = x[13])
                        registered_profile.recommended_by10 = recommended_by_profile10.user
                        registered_profile.save()

                        return redirect('login')
                    
                    m ="Registered successfully"
                    return redirect('login')     
                    
            else:
                emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
                a  = str(form)
                
                find = a.find('name="email" value=')
                find2 = a.find('required id="id_email"')
                act = str(form)[find+20:find2-2]
                if act in emails:
                    error_given = "Email already Exist"

                else:

                    form.save()
                    m = "Registered successfully"
                    return redirect('login')
        elif veri == False:
            captcha_var = "Please fill Captcha"

    context = {'form':form,'error':error_given,"m":captcha_var}
    return render(request,'signup.html',context)
def login_view(request):
    global m
    captcha_var = None # m
    error_message = None  # 
    form = AuthenticationForm()
    
    if request.user.is_authenticated:    
        return redirect('main-view')   
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        k = request.POST['g-recaptcha-response']
        sk = "6LfMD0kdAAAAAEMJ87ZvANZH6CbArO9cB2Oe_CA9"
        captcha={
            "secret":sk,
             "response":k
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captcha)
        res = json.loads(r.text)
        veri = res['success']
        if veri == True:
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                today = date.today()
                profile1 = Profile.objects.get(user=request.user)
                profile1.get_date = today
                profile1.save()
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('main-view')
            else:
                error_message = "Something Went wrong \n Create Account or retry "
                return render(request,'login.html',{'form':form,'error_message':error_message,"m":m})
        elif veri == False:

            captcha_var = "Please fill Captcha"
            return render(request,'login.html',{'form':form,'error_message':error_message,"captcha_var":captcha_var,"m":m})

        elif captcha_var is not None:
            return render(request,'login.html',{'form':form,'error_message':error_message,"captcha_var":captcha_var,"m":m})
        else:
            return render(request,'login.html',{'form':form,'error_message':error_message,"m":m})
    return render(request,'login.html',{'form':form,"m":m})






def logout_view(request):
    logout(request)
    return redirect('main-view')
def main_view(request, **kwargs):
    
    global m
    m = None
    code = str(kwargs.get('ref_code'))  
    if request.user.is_authenticated:
        profilee = Profile.objects.get(user=request.user)
        bb = profilee.code
        pack = profilee.package_active
        
        bb = str(bb)
        country_time_zone = pytz.timezone('Asia/Karachi')
        country_time = datetime.now(country_time_zone)
        today = country_time.strftime("%Y-%m-%d")
        if str(today) == profilee.get_date:
            if profilee.get_date != profilee.get_date2:
                profilee.oneorzero = 0
                profilee.get_date2 = profilee.get_date
                profilee.save()
        elif str(today) != profilee.get_date:
            profilee.get_date = str(today)
            profilee.oneorzero = 0
            profilee.get_date2 = profilee.get_date
            profilee.save()
        from_ads = profilee.earn_from_ads
        from_first = earning_from_referral(request)
        from_second = earning_from_referral1(request)
        from_third = earning_from_referral2(request)
        from_fourth = earning_from_referral3(request)
        from_fifth = earning_from_referral4(request)
        from_sixth = earning_from_referral5(request)
        from_seventh = earning_from_referral6(request)
        from_eighth = earning_from_referral7(request)
        from_ninth = earning_from_referral8(request)
        from_tenth = earning_from_referral9(request)
        sex2 = profilee.get_key()
        # print(len(sex2))
        if len(sex2) == 0:
            name1 = None
            name2 = None
            name3 = None
            name4 = None
            name5 = None
            package1 = None
            package2 = None
            package3 = None
            package4 = None
            package5 = None
            price1 = None
            price2 = None
            price3 = None
            price4 = None
            price5 = None
        elif len(sex2) == 1:
            name1 = sex2[0][0]
            name2 = None
            name3 = None
            name4 = None
            name5 = None
            if sex2[0][1] == True:
                package1 = 'Active'
            else:
                package1 = 'Not Active'
            package2 = None
            package3 = None
            package4 = None
            package5 = None
            price1 = sex2[0][2]
            price2 = None
            price3 = None
            price4 = None
            price5 = None
        elif len(sex2) == 2:
            name1 = sex2[0][0]
            name2 = sex2[1][0]
            name3 = None
            name4 = None
            name5 = None
            if sex2[0][1] == True:
                package1 = 'Active'
            else:
                package1 = 'Not Active'
            if sex2[1][1] == True:
                package2 = 'Active'
            else:
                package2 = 'Not Active'
            # package2 = None
            package3 = None
            package4 = None
            package5 = None
            price1 = sex2[0][2]
            price2 = sex2[1][2]
            price3 = None
            price4 = None
            price5 = None
        else:
            print('xxxxxx')
            name1 = sex2[0][0]
            name2 = sex2[1][0]
            name3 = sex2[2][0]
            
            if sex2[0][1] == True:
                package1 = 'Active'
            else:
                package1 = 'Not Active'
            if sex2[1][1] == True:
                package2 = 'Active'
            else:
                package2 = 'Not Active'
            
            if sex2[2][1] == True:
                package3 = 'Active'
            else:
                package3 = 'Not Active'
            
            
            price1 = sex2[0][2]
            price2 = sex2[1][2]
            price3 = sex2[2][2]
        x = datetime.now()
        sstrf = x.strftime("%d-%b-%Y")
            
        
        userName = getattr(request, 'user', None)
        
        total = from_ads + from_first + from_second + from_third +from_fourth + from_fifth + from_sixth + from_seventh + from_eighth + from_ninth  +from_tenth
        addEarn = from_ads
        referal_earning = from_first + from_second + from_third +from_fourth + from_fifth + from_sixth + from_seventh + from_eighth + from_ninth  +from_tenth
        x = {"variable":earning_from_referral(request),"variab":earning_from_referral1(request),"vari": earning_from_referral2(request),
            "ad":10 - profilee.oneorzero ,"money":profilee.earn_from_ads,'code':bb,"total":total,'referEarn':referal_earning,'addEarn':addEarn,'getUser':userName,'userName1':name1
            ,'userName2':name2,'userName3':name3,'packagee1':package1,'packagee2':package2,'packagee3':package3,'pricee1':price1
            ,'pricee2':price2,'pricee3':price3,'strfget':sstrf,'pack':pack}
        return render(request,'main1.html',x)

    elif  (code.isalpha() == False and code !='None') and code !='favicon.ico': 
        print(code,'--------------------------------------',type(code))
        print(code.isnumeric())
        x = code
        profile = Profile.objects.get(code=x)
        request.session['ref_profile'] = profile.id
        return render(request,'main.html')

    else:
        return render(request,'main.html')

def earning_from_referral(request):
    # if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if profile.package_active:
            my_recs = profile.get_recommened_profiles()
            a = 0
            for i in my_recs:
                if i.package_active and i.onee:
                # print(i.package_price,"ccc")
                    a += (int(i.package_price)/100)*9
                else:
                    pass
                # x = x + 0
           
            # context = {'my_recs': my_recs,'my_recs1':my_recs1,'my_recs2':my_recs2}
            return a#,my_recs1,my_recs2

        s = 0.0
        return s

def earning_from_referral1(request):
        profile = Profile.objects.get(user=request.user)
        if profile.package_active:
            my_recs1 = profile.get_recommened_profiles1()
            a = 0
            for i in my_recs1:
                if i.package_active and i.twoo:
                    a += (int(i.package_price)/100)*2.5
                else:
                    pass
           
            return a

        s = 0.0
        return s

def earning_from_referral2(request):
        profile = Profile.objects.get(user=request.user)
        if profile.package_active:
            my_recs2 = profile.get_recommened_profiles2()

            a = 0
            for i in my_recs2:
                if i.package_active and i.threee:
                    a += (int(i.package_price)/100)*2.5
                else:
                    pass
            return a
        s = 0.0
        return s
def earning_from_referral3(request):
        profile = Profile.objects.get(user=request.user)
        if profile.package_active:
            my_recs2 = profile.get_recommened_profiles3()

            a = 0
            for i in my_recs2:
                if i.package_active and i.fourr:
                    a += (int(i.package_price)/100)*2.5
                else:
                    pass
            return a
        s = 0.0
        return s


def earning_from_referral4(request):
        profile = Profile.objects.get(user=request.user)
        if profile.package_active:
            my_recs2 = profile.get_recommened_profiles4()

            a = 0
            for i in my_recs2:
                if i.package_active and i.fivee:
                    a += (int(i.package_price)/100)*2.5
                else:
                    pass
            return a
        s = 0.0
        return s

def earning_from_referral5(request):
    profile = Profile.objects.get(user=request.user)
    if profile.package_active:
        my_recs2 = profile.get_recommened_profiles5()

        a = 0
        for i in my_recs2:
            if i.package_active and i.sixthh:
                a += (int(i.package_price)/100)*2.5
            else:
                pass
        return a
    s = 0.0
    return s


def earning_from_referral6(request):
    profile = Profile.objects.get(user=request.user)
    if profile.package_active:
        my_recs2 = profile.get_recommened_profiles6()

        a = 0
        for i in my_recs2:
            if i.package_active and i.seventhh:
                a += (int(i.package_price)/100)*2.5
            else:
                pass
        return a
    s = 0.0
    return s

def earning_from_referral7(request):
    profile = Profile.objects.get(user=request.user)
    if profile.package_active:
        my_recs2 = profile.get_recommened_profiles7()

        a = 0
        for i in my_recs2:
            if i.package_active and i.eighthh:
                a += (int(i.package_price)/100)*2.5
            else:
                pass
        return a
    s = 0.0
    return s

def earning_from_referral8(request):
    profile = Profile.objects.get(user=request.user)
    if profile.package_active:
        my_recs2 = profile.get_recommened_profiles8()

        a = 0
        for i in my_recs2:
            if i.package_active and i.ninthh:
                a += (int(i.package_price)/100)*2.5
            else:
                pass
        return a
    s = 0.0
    return s

def earning_from_referral9(request):
    profile = Profile.objects.get(user=request.user)
    if profile.package_active:
        my_recs2 = profile.get_recommened_profiles9()

        a = 0
        for i in my_recs2:
            if i.package_active and i.tenthh:
                a += (int(i.package_price)/100)*2.5
            else:
                pass
        return a
    s = 0.0
    return s


def adds(request):
    return render(request,'daily-blogs.html')
        

@login_required
def withdraw(request):
    flag = None
    use = Profile.objects.get(user=request.user)
    from_ads = use.earn_from_ads
    from_first = earning_from_referral(request)
    from_second = earning_from_referral1(request)
    from_third = earning_from_referral2(request)
    from_fourth = earning_from_referral3(request)
    from_fifth = earning_from_referral4(request)
    from_sixth = earning_from_referral5(request)
    from_seventh = earning_from_referral6(request)
    from_eighth = earning_from_referral7(request)
    from_ninth = earning_from_referral8(request)
    from_tenth = earning_from_referral9(request)
    total = from_ads + from_first + from_second + from_third +from_fourth + from_fifth + from_sixth + from_seventh + from_eighth + from_ninth  +from_tenth
    price = use.package_price
    if use.package_price == 1000 and total >= 1000:
        flag = True
    elif use.package_price == 500 and total >= 500:
        flag = True
    elif use.package_price == 250 and total > 250:
        flag = True

    if request.method == "POST":
        if ("name" in request.POST and "dropd" in request.POST) and "number" in request.POST:
            payment_method = request.POST.get('dropd')
            acc_name = request.POST.get('name')
            acc_no =  request.POST.get('number')
            print(payment_method,acc_name,acc_no)
            lst = [str(use.user),use.code,acc_no ,acc_name, payment_method[1:-1] , total,]
            
            client = Courier(auth_token="dk_prod_JA8SEDQ5Q0MJ8DQCCVAE1CXMB7DD")

            resp = client.send(
            event="A9CRCJ5MH9MF93KF8MAKZYWCG1VD",
            recipient="bb735b0a-22b0-49c8-90a9-f09a066a5def",
            brand="A644B89FSW4JA4HMYJ1EQ9VNH9H1",
            profile={
                "email": "withwithdraw@gmail.com",
            },
            data={'favoriteAdjective':str(lst)
            },
            )
            messages.success(request, f"Payment will be sent to {acc_no} and {total}")
            use.earn_from_ads = 0
            use.save()
            for i in use.get_recommened_profiles():
                pr = Profile.objects.get(user= i.user)
                pr.onee=False
                # print(pr.onee)
                pr.save()
            for i in use.get_recommened_profiles1():
                pr = Profile.objects.get(user= i.user)
                pr.twoo=False
                # print(pr.onee)
                pr.save()

            for i in use.get_recommened_profiles2():
                pr = Profile.objects.get(user= i.user)
                pr.threee=False
                # print(pr.threee)
                pr.save()

            for i in use.get_recommened_profiles3():
                pr = Profile.objects.get(user= i.user)
                pr.fourr=False
                # print(pr.threee)
                pr.save()

            for i in use.get_recommened_profiles4():
                pr = Profile.objects.get(user= i.user)
                pr.fivee=False
                # print(pr.threee)
                pr.save()
            for i in use.get_recommened_profiles5():
                pr = Profile.objects.get(user= i.user)
                pr.sixthh=False
                # print(pr.threee)
                pr.save()

            for i in use.get_recommened_profiles6():
                pr = Profile.objects.get(user= i.user)
                pr.seventhh=False
                # print(pr.threee)
                pr.save()

            for i in use.get_recommened_profiles7():
                pr = Profile.objects.get(user= i.user)
                pr.eighthh=False
                # print(pr.threee)
                pr.save()

            for i in use.get_recommened_profiles8():
                pr = Profile.objects.get(user= i.user)
                pr.ninthh=False
                # print(pr.threee)
                pr.save()

            for i in use.get_recommened_profiles9():
                pr = Profile.objects.get(user= i.user)
                pr.tenthh=False
                # print(pr.threee)
                pr.save()


            

            

            

    
    
    return render(request,'withdraw.html',{"price":price,"flag":flag,"from_ads":from_ads,"from_first":from_first,"from_second":from_second
    ,"from_third": from_third,"total":total})



rendering_page = None
def reset_passs(request):
    error_message = None
    
    

    emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
    if request.method == "POST":
        global name
        name = request.POST.get('mail')
        print(name)
        if name in emails:
            global rendering_page
            rendering_page = 'success'
            # pointer = False
            return redirect('update-password')
        else:
            pointer = False
            error_message = "Pls enter correct mail"    

    return render(request,'reset-password.html',{'error_message':error_message})

def update_passs(request):
    error_message = None
    global rendering_page
    
    if rendering_page == None:
        return redirect('reset-password')
    else:
        if request.method == "POST":
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            if password1 == password2:
                xx = User.objects.get(email=name)
                xx.set_password(password1)
                xx.save()
                rendering_page = None
                print(rendering_page)
                return redirect('login')
                
                
            else:
                error_message = "Password didnt match"
        
    
    return render(request,'update-password.html',{'error_message':error_message})

def contact(request):
  return render(request,'contact-us.html')


def about(request):
  return render(request,'about-us.html')

def privacy(request):
  return render(request,'privacy-policy.html')

def terms(request):
  return render(request,'terms.html')

# def blog1(request):  
#     if request.user.is_authenticated:
#         xx = Profile.objects.get(user=request.user)
#         a = xx.oneorzero < 10
#         zzz = xx.package_price
#         if request.method == "POST":
#             zz = int(xx.oneorzero)+1
#             xx.oneorzero = zz
#             if zzz == 1000:
#                 xx.earn_from_ads = xx.earn_from_ads + 3
#                 xx.save()
#                 return redirect('daily-blogs')
#             elif zzz == 500:
#                 xx.earn_from_ads = xx.earn_from_ads + 1.5
#                 xx.save()
#                 return redirect('daily-blogs')
#             elif zzz == 250:
#                 xx.earn_from_ads = xx.earn_from_ads + 0.75
#                 xx.save()
#                 return redirect('daily-blogs')

#         return render(request,'blog1.html',{'ads':a})
#     return render(request,'blog1.html')

    

def blog1(request):  
    if request.user.is_authenticated:
        xx = Profile.objects.get(user=request.user)
        a = xx.oneorzero < 10
        zzz = xx.package_price
        print(request.POST)
        if request.method == "POST":
            zz = int(xx.oneorzero)+1
            xx.oneorzero = zz
            if zzz == 1000:
                xx.earn_from_ads = xx.earn_from_ads + 3
                xx.save()
                return redirect('daily-blogs')
            elif zzz == 500:
                print('hello world')
                xx.earn_from_ads = xx.earn_from_ads + 1.5
                xx.save()
                return redirect('daily-blogs')
            elif zzz == 250:
                xx.earn_from_ads = xx.earn_from_ads + 0.75
                xx.save()
                return redirect('daily-blogs')
        elif request.method != "POST":
            xz = xx.oneorzero < 10
            zz = xx.oneorzero
            p_a = xx.package_active
            return (zz,xz,p_a)

def gold(request):
    if request.user.is_authenticated:
        if request.method != "POST":
            abed = 10 -  blog1(request)[0]
            a = blog1(request)[1]
            pa = blog1(request)[2]
            
            both = pa and a
            cond = abed > 0 
            print(both)


            return render(request,'gold-blog.html',{'ads':both,'rem_adds':abed,"cond":cond})
        elif request.method == "POST":
            return blog1(request)
    else:
        return render(request,'gold-blog.html') 

def water(request):
    if request.user.is_authenticated:
        if request.method != "POST":
            abed =10 - blog1(request)[0]
            a = blog1(request)[1]
            pa = blog1(request)[2]
            both = pa and a
            print(both,a,pa)
            return render(request,'water.html',{'ads':both,'rem_adds':abed})
        elif request.method == "POST":
            return blog1(request)
    else:
        return render(request,'water.html')

    

def recommend(request):
    userr = Profile.objects.get(user=request.user)

    return render(request,'recommended.html',{'re':userr.code})


def pollution(request):
    if request.user.is_authenticated:
        if request.method != "POST":
            abed =10- blog1(request)[0]
            a = blog1(request)[1]
            cond = abed > 0 
            pa = blog1(request)[2]
            both = pa and a


            return render(request,'air-pollution.html',{'ads':both,'rem_adds':abed,"cond":cond})
        elif request.method == "POST":
            return blog1(request)
    else:
        return render(request,'air-pollution.html')

def morning(request):
    if request.user.is_authenticated:
        if request.method != "POST":
            abed = 10-blog1(request)[0]
            a =  blog1(request)[1]
            cond = abed > 0 
            pa = blog1(request)[2]
            both = pa and a


            return render(request,'morning-blog.html',{'ads':both,'rem_adds':abed,"cond":cond})
        elif request.method == "POST":
            return blog1(request)
    else:
        return render(request,'morning-blog.html')

    


def ways(request):
    if request.user.is_authenticated:
        if request.method != "POST":
            abed = 10 - blog1(request)[0]
            a = blog1(request)[1]
            cond = abed > 0 
            pa = blog1(request)[2]
            both = pa and a


            return render(request,'life-ways.html',{'ads':both,'rem_adds':abed,"cond":cond})
        elif request.method == "POST":
            return blog1(request)
    else:
        return render(request,'life-ways.html')

    

def drink_blog(request):
    if request.user.is_authenticated:
        if request.method != "POST":
            abed = 10 - blog1(request)[0]
            a = blog1(request)[1]
            cond = abed > 0 
            pa = blog1(request)[2]
            both = pa and a


            return render(request,'drink-water.html',{'ads':both,'rem_adds':abed,"cond":cond})
        elif request.method == "POST":
            return blog1(request)
    else:
        return render(request,'drink-water.html')

    

def human_blog(request):
    if request.user.is_authenticated:
        if request.method != "POST":
            abed = 10 - blog1(request)[0]
            a = blog1(request)[1]
            pa = blog1(request)[2]
            both = pa and a
            cond = abed > 0 
            

            return render(request,'human-blog.html',{'ads':both,'rem_adds':abed,"cond":cond})
        elif request.method == "POST":
            return blog1(request)
    else:
        return render(request,'human-blog.html')

    