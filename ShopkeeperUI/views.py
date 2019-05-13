from django.shortcuts import render,redirect
from django.http import HttpResponse
from ShopkeeperUI import models
from ShopkeeperUI import forms
from django.shortcuts import get_list_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from ShopkeeperUI.models import Shop
# Create your views here.



def home(request):
    if( request.user.is_authenticated ):
        currentProfile = models.Profile.objects.filter(user=request.user)
        
        if( len(currentProfile) and currentProfile[0].shopOwner == True):
            return redirect('/shophome/')
        else:
            return redirect('/userhome/')
    else:
        return render(request, 'homepage.html')

@login_required(redirect_field_name='/accounts/login/')
def userHome(request):
    if( Profile.objects.filter(user=request.user)[0].shopOwner == True ):
        return redirect('/shophome/')
    payload = []
    shops = models.Shop.objects.all()
    for shop in shops:
            payload.append({
                'shop': shop,
            })
    content = {
        'payload': payload,
    }
    return render(request, 'ShopkeeperUI/userhome.html', content)


@login_required(redirect_field_name='/accounts/login/')
def shopHome(request):
    if( Profile.objects.filter(user=request.user)[0].shopOwner == False):
        return redirect('/shophome/userhome/')
    payload=[]
    shops = models.Shop.objects.filter(admin=Profile.objects.get(user=request.user))
    for shop in shops:
            payload.append({
                'shopname': shop,
            })
    
    # data = models.Item.objects.all()
    # payload = []
    # if( request.user.is_authenticated ):
    #     print(request.user)
    #     k = Profile.objects.get(user=request.user)
    # for i in data:
    #     if(i.shopProfile.name=='Kalsi General Store'):
    #         payload.append(i)
    # payload = get_object_or_404(models.Item, shop.name=='Kalsi General Store')
    # payload = get_list_or_404(models.Item, name__contains='Kalsi General Store')

    content = {
        'payload': payload,
    }
    return render(request, 'ShopkeeperUI/home.html', content)

@login_required(redirect_field_name='/accounts/login/')
def addItem(request):
    if( Profile.objects.filter(user=request.user)[0].shopOwner == False):
        return redirect('/userhome/')
    shop = models.Shop.objects.filter(admin=models.Profile.objects.get(user= request.user))
    if(request.method=='POST'):
        form = forms.AddItems(shop, request.POST)
        if( form.is_valid() ):
            if( request.user.is_authenticated ):
                instance = form.save(commit=False)
                shopProfile = Profile.objects.get(user=request.user)
                if(not shopProfile.shopOwner):
                    content = {
                            'message': 'You are Not Registered As Shopkeeper'
                        }
                    return render(request, 'message.html', content)
                if( instance.shopProfile == Shop.objects.filter( admin=shopProfile, name=instance.shopProfile.name)[0] ):
                    instance.save()
                    content = {
                            'message': 'Thank You! Your Item Has Been Added'
                        }
                    return render(request, 'message.html', content)
                else:
                    content = {
                            'message': 'You are Not Authorised To Add Item To This Shop'
                        }
                    return render(request, 'message.html', content)                    
                        
                    # return You are not registered as shopkeeper

    else:

        form = forms.AddItems(yourshop=shop)

    content = {
        'form': form
    }
    return render(request, 'ShopkeeperUI/additem.html', content)


@login_required(redirect_field_name='/accounts/login/')
def addShop(request):
    if( Profile.objects.filter(user=request.user)[0].shopOwner == False):
        return redirect('/userhome/')
    if (request.method == 'POST'):
        form = forms.AddShop(request.POST)
        if( request.user.is_authenticated ):
            if( form.is_valid() ):
                instance, flag = Shop.objects.get_or_create(
                    name = form.cleaned_data['name'],
                    desc = form.cleaned_data['desc'],
                    address = form.cleaned_data['address'],
                    admin = Profile.objects.get(user=request.user)
                )
                instance.save()
                content = {
                            'message': "Thank You! Your Shop Has Been Added. \n Let's Add An Item"
                        }
                return render(request, 'message.html', content)
            # instance.set_Profile()

    else:
        form = forms.AddShop()
    content = {
        'form': form
    }
    return render(request, 'ShopkeeperUI/addshop.html', content)


def shopDetail(request, value):
    shop = Shop.objects.filter(id=value)
    if(len(shop) == 0):
        content = {
            'message': 'Sorry No Shop Available'
        }
        return render(request, 'message.html', content)
    items = models.Item.objects.filter(shopProfile=shop[0])
    content = {
        'shop':shop[0],
        'items':items,
    }
    return render(request, 'ShopkeeperUI/shopdetail.html', content)