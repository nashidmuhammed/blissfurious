from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from bliss.models import *
from django.contrib.auth.forms import UserCreationForm
from .froms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    prof = profile.objects.get(prof_name='Nashid Muhammed')
    art = article.objects.all()

    return render(request, 'index.html', {'prof':prof, 'art':art})


def travel(request):
    art = article.objects.filter(category='Travel')
    car = Carousel.objects.get(category='Travel')
    return render(request, 'travel.html', {'art':art, 'car':car})


def tech(request):
    art = article.objects.filter(category='Technology')
    car = Carousel.objects.get(category='Technology')
    return render(request, 'tech.html', {'art':art, 'car':car})


def photography(request):
    art = article.objects.all()
    car = Carousel.objects.get(category='Photography')
    return render(request, 'photography.html', {'art':art, 'car':car})


def single(request, id=None):
    art = article.objects.get(art_id=id)
    com = comment.objects.filter(art_id=art.art_id)
    return render(request, 'single.html', {'art': art, 'com': com})


def about(request):
    prof = profile.objects.get(prof_name='Nashid Muhammed')
    return render(request, 'about.html', {'prof':prof})


def contact(request):
    if request.method == 'POST':
        con = contacts(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'],
                       message=request.POST['message'])
        con.save()
        messages.info(request, 'Your message was send!')
        return redirect('.')
    pro = profile.objects.get(prof_name='Nashid Muhammed')
    return render(request, 'contact.html', {'pro':pro})


def comments(request):
    if request.method == 'POST':
        iid = request.POST['id']
        com = comment(art_id=request.POST['id'], name=request.POST['name'], email=request.POST['email'], message=request.POST['comment'])
        com.save()
        messages.info(request, 'Your comment posted successfully!')
    return single(request,iid)


# ADMIN PART
@login_required(login_url='adm_login')
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('adm_login')

    context = {'form':form}
    return render(request, 'register.html', context)


def adm_login(request):
    if request.user.is_authenticated:
        return redirect('adm')
    else:
        if request.method == 'POST':
            admin_id = request.POST.get('admin_id')
            password = request.POST.get('password')
            user = authenticate(request, username=admin_id, password=password)
            if user is not None:
                login(request, user)
                return redirect('adm')
            else:
                messages.info(request, 'AdminId OR password is incorrect')
        context = {}
        return render(request, 'adm_login.html', context)


def adm_logout(request):
    logout(request)
    return redirect('adm_login')


@login_required(login_url='adm_login')
def adm(request):
    prof = profile.objects.get(prof_name='Nashid Muhammed')
    return render(request, 'admin_panel.html', {'prof':prof})


@login_required(login_url='adm_login')
def prof(request):
    try:
        pro = profile.objects.get(prof_name='Nashid Muhammed')
        try:
            prof_img = request.FILES['prof_img']
            pro.prof_img = prof_img
            pro.save()
            print("Success img")
            return adm(request)
        
        except KeyError:
            pro.description = request.POST['desc']
            pro.save()
            print("Success desc")
            return adm(request)
    except KeyError:
        print("except error")
        return adm(request)


@login_required(login_url='adm_login')
def cover(request):
    pro = profile.objects.get(prof_name='Nashid Muhammed')
    try:
        cov_img = request.FILES['cov_img']
        pro.cov_img = cov_img
        pro.save()
        return adm(request)
    except KeyError:
        pro.about = request.POST['about']
        pro.save()
        return adm(request)


@login_required(login_url='adm_login')
def cont_edit(request):
    try:
        pro = profile.objects.get(prof_name='Nashid Muhammed')
        pro.email = request.POST['email']
        pro.phone = request.POST['phone']
        pro.address = request.POST['address']
        pro.save()
        return adm(request)
    except KeyError:
        return adm(request)


@login_required(login_url='adm_login')
def adm_post(request):
    try:
        if request.method == 'POST':
            art = article(auther=request.POST['auther'], date=request.POST['date'], category=request.POST['category'], caption=request.POST['hd'],
                          description=request.POST['bd'], cover_img=request.FILES['img'])
            art.save()
            messages.success(request, 'Successfully posted')
        return render(request, 'adm_post.html')
    except KeyError:
        return adm(request)


@login_required(login_url='adm_login')
def adm_update(request):
    try:
        if request.method == 'POST':
            art_id = request.POST['id']
            art = article.objects.get(art_id=art_id)
            art.auther = request.POST['auther']
            art.date = request.POST['date']
            art.category = request.POST['cat']
            art.caption = request.POST['cap']
            art.description = request.POST['desc']
            art.cover_img = request.FILES['cov_img']
            art.save()
            messages.success(request, 'Successfully updated')
        return render(request, 'adm_update.html')
    except KeyError:
        return adm(request)


@login_required(login_url='adm_login')
def update_sub(request):
    try:
        v = request.GET['v']
        art = article.objects.get(art_id=v)
        data = {'res':1, 'auther':art.auther, 'date':art.date, 'cat':art.category, 'cap':art.caption,
                'desc':art.description, 'img': art.cover_img.url}
        return JsonResponse(data)
    except article.DoesNotExist:
        res = 0
        data = {'res': res, 'value':'&nbsp;Incorrect Id - The id is does not exist'}
        return JsonResponse(data)


@login_required(login_url='adm_login')
def adm_delete(request):
    try:
        if request.method == 'POST':
            art_id = request.POST['id']
            print("art_idddd = ",art_id)
            art = article.objects.get(art_id=art_id)
            try:
                com =comment.objects.filter(art_id=art_id)
                com.delete()
            except comment.DoesNotExist:
                print("maaaaaaaasss")
                pass
            art.delete()
            messages.success(request, 'Successfully deletedddd ',art_id)
        return render(request, 'adm_delete.html')
    except KeyError:
        return adm(request)


@login_required(login_url='adm_login')
def adm_delete_sub(request):
    try:
        if request.method == 'GET':
            v = request.GET['v']
            art = article.objects.get(art_id=v)
            data = {'res': 1, 'auther': art.auther, 'date': art.date, 'cat': art.category, 'cap': art.caption,
                    'desc': art.description, 'img': art.cover_img.url}
            return JsonResponse(data)
        return render(request, 'adm_delete.html')
    except article.DoesNotExist:
        res = 0
        data = {'res': res, 'value': '&nbsp;Incorrect Id - The id is does not exist'}
        return JsonResponse(data)


@login_required(login_url='adm_login')
def adm_view(request):
    art = article.objects.all()
    return render(request, 'adm_view.html', {'art': art})


@login_required(login_url='adm_login')
def adm_view_del(request, id=None):
    ids = str(id)
    art_del = article.objects.get(art_id=id)
    try:
        com = comment.objects.filter(art_id=art_del.art_id)
        com.delete()
        print("deleted form view")
    except comment.DoesNotExist:
        print("passsss")
        pass
    art_del.delete()
    messages.info(request, 'Successfully deleted Article : '+ids)
    return redirect('adm_view')


@login_required(login_url='adm_login')
def adm_message(request):
    msg = contacts.objects.all()
    return render(request, 'adm_message.html', {'msg':msg})


@login_required(login_url='adm_login')
def adm_comment(request):
    com = comment.objects.all()
    return render(request, 'adm_comment.html', {'com': com})


@login_required(login_url='adm_login')
def adm_carousel(request):
    try:
        if request.method == 'GET':
            print("innerrrrrrrrr")
            cats = request.GET['cats']
            print("Cat = ",cats)
            try:
                car = Carousel.objects.get(category=cats)
                data = {'img1':car.car_img1.url, 'img2':car.car_img2.url, 'img3':car.car_img3.url,
                        'h1':car.h_1,'h2':car.h_2,'h3':car.h_3,
                        'p1':car.p_1,'p2':car.p_2,'p3':car.p_3}
                print("data = ",data)
                return JsonResponse(data)
            except Carousel.DoesNotExist:
                print("not exist")
                data={'h1':0}
                return JsonResponse(data)
    except:
        print("Except")
        return render(request, 'adm_carousel.html')


@login_required(login_url='adm_login')
def adm_carousel_img1(request):
    if request.method == 'POST':
        car = Carousel.objects.get(category=request.POST['id'])
        car.car_img1 = request.FILES['img1']
        car.h_1 = request.POST['h1']
        car.p_1 = request.POST['p1']
        car.save()
        print("saveddddd")
        messages.success(request, 'Successfully updated')
        return redirect('adm_carousel')
    return render(request, 'adm_carousel.html')


@login_required(login_url='adm_login')
def adm_carousel_img2(request):
    if request.method == 'POST':
        car = Carousel.objects.get(category=request.POST['id'])
        car.car_img2 = request.FILES['img2']
        car.h_2 = request.POST['h2']
        car.p_2 = request.POST['p2']
        car.save()
        print("saveddddd")
        messages.success(request, 'Successfully updated')
        return redirect('adm_carousel')
    return render(request, 'adm_carousel.html')


@login_required(login_url='adm_login')
def adm_carousel_img3(request):
    if request.method == 'POST':
        car = Carousel.objects.get(category=request.POST['id'])
        car.car_img3 = request.FILES['img3']
        car.h_3 = request.POST['h3']
        car.p_3 = request.POST['p3']
        car.save()
        print("saveddddd")
        messages.success(request, 'Successfully updated')
        return redirect('adm_carousel')
    return render(request, 'adm_carousel.html')

def about_me(request):
    pro = profile.objects.get(prof_name='Nashid Muhammed')
    return render(request, 'about_me.html', {'pro':pro})
