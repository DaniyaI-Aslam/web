from django.shortcuts import render
from .models import Profile
from trycourier import Courier
# Create your views here.
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

@login_required
def my_recommendations_view(request):
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommened_profiles()
    my_recs1 = profile.get_recommened_profiles1()
    my_recs2 = profile.get_recommened_profiles2()
    my_recs3 = profile.get_recommened_profiles3()
    my_recs4 = profile.get_recommened_profiles4()
    my_recs5 = profile.get_recommened_profiles5()
    my_recs6 = profile.get_recommened_profiles6()
    my_recs7 = profile.get_recommened_profiles7()
    my_recs8 = profile.get_recommened_profiles8()
    my_recs9 = profile.get_recommened_profiles9()
    # my_recs10 = profile.get_recommened_profiles10()
    context = {'my_recs': my_recs,'my_recs1':my_recs1,'my_recs2':my_recs2,'my_recs3':my_recs3,'my_recs4':my_recs4,'my_recs5':my_recs5,'my_recs6':my_recs6,'my_recs7':my_recs7,'my_recs8':my_recs8,'my_recs9':my_recs9}
    return render(request, 'profiles/main1.html', context)

@login_required
def makedeposit(request):
    profile = Profile.objects.get(user=request.user)
    a = profile.package_active
    b = profile.package_price 
    error_message = None
    if request.method == "POST":

        if ("tid" in request.POST and "dropd" in request.POST) and "dropdown" in request.POST:
            tid = request.POST.get('tid')
            # print(tid)
            payment_method = request.POST.get('dropd')
            package_amount = request.POST.get('dropdown')
            if len(tid) < 11 or len(tid) > 11:
                
                error_message = "Please Enter correct TID"
            # print(tc)
            # pac = request.POST.get('package-amount')
            # print(pac)
            else:
                answer = request.POST.get('dropdown')
                # print(type(answer),answer)
                regg = Profile.objects.get(user=request.user)
                regg.package_price = answer
                regg.save()
                lst = [str(profile.user),profile.code,tid , payment_method[1:-1] , package_amount,]
                # client = Courier(auth_token="dk_prod_518DW3CESQMV0RMB4B2FYW5JNJP8")
 
                # resp = client.send(
                # event="WEEK74AT3245QEK6J9B1P0Q3900F",
                # recipient="05217c5e-3f34-4cfa-a232-6abd3ad3a723",
                # brand="PAEFHE2E9M4NASQWKETTNFR45EXH",
                # profile={"email": "daniyalaslam54@gmail.com"
                # },
                # data={
                #     "variables": lst,
                # },
                # )
                # Install Courier SDK: pip install trycourier
                from trycourier import Courier

                client = Courier(auth_token="pk_prod_QJA1FX792AM9V7GN775MQTZ6P8XM")

                resp = client.send(
                event="courier-quickstart",
                recipient="trumtrumtrum58@gmail.com",
                data={
                    "favoriteAdjective": lst
                },
                profile={
                    "email": "ddeposit42@gmail.com"
                }
                )
                error_message = "Submitted Succesfully"

        else:
            error_message = "please fill all fields"
            # messages.error(request, "please fill all fields")
    return render(request,'profiles/makedposit.html',{"error_message":error_message,"flag":a,"p":b})

