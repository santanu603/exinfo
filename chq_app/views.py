from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .models import master, order, replacement
from .forms import chq_form, order_form, replace_form
from django.db.models.functions import Concat
from django.db.models import Value




# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')
        

        if password!=confirm_password:
            try:

                messages.info(request, 'Password and confirm password are not same')
            except:
                print("An exception occurred")
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This user id is already exist')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect('login')
                
    else:


        return render(request, 'register.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('home')

def entry(request):
    
    form=chq_form()
    if request.method == 'POST':
        form=chq_form(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Details submitted successfully')
            return redirect('entry')
            



    context={'form':form}


    return render(request, 'entry.html', context)


def view_update(request):
    
    
    if request.method == 'POST':
        chq=request.POST['chq']
        details = master.objects.all()

        if chq:
            details=details.filter(chq__icontains = chq)

        context={'details':details}

        
        return render(request, 'view_update.html', context)
        
    
    elif request.method == 'GET':
        return render(request, 'view_update.html')
    else:
        return HttpResponse('An Exception Occured')



def edit(request, id):
    if request.method == 'POST':
        chq_id=master.objects.get(pk=id)
        form = chq_form(request.POST, instance=chq_id)
        if form.is_valid():
            form.save()
            messages.info(request, 'Details Updated successfully')
            return render(request, 'edit.html', {
                'form':form,
                'success':True
            })
    else:
        chq_id=master.objects.get(pk=id)
        form=chq_form(instance=chq_id)
        return render(request, 'edit.html',{
            'form':form
        })


def filter_chq(request):
    if request.method == 'POST':
        agent=request.POST['agent']
        status=request.POST['status']
        filter_details=master.objects.all()

        if agent:
            filter_details=filter_details.filter(agent=agent)
        if status:
            filter_details=filter_details.filter(status=status)
        
        context={
            'filter_details':filter_details
        }

        return render(request, 'filter_chq.html', context)
    
    elif request.method =='GET':
        return render(request, 'filter_chq.html')
    else:
        return HttpResponse('An Exception Occureed')

def delete(request, id):
    if request.method == 'POST':
        details = master.objects.get(pk=id)
        details.delete()
        return HttpResponseRedirect(reverse('view_update'))


def delivery_main(request):
    form2=order_form()
    if request.method == 'POST':
        form2=order_form(request.POST)
        if form2.is_valid():
            form2.save()
            messages.info(request,'Details submitted successfully')
            return redirect('delivery_main')

    context={'form2':form2}

    return render(request,'order_main.html',context)



def filter_delivery(request):
    if request.method =='POST':
        date=request.POST['date']
        invoice=request.POST['invoice']
        agent=request.POST['agent']
        deliverysts=request.POST['deliverysts']
        deliveryagt=request.POST['deliveryagt']
        paymentsts=request.POST['paymentsts']

        dlvry=order.objects.all()

        if date:
            dlvry=dlvry.filter(date__icontains =date)
        if invoice:
            dlvry=dlvry.filter(invoice__icontains =invoice)
        if agent:
            dlvry=dlvry.filter(agent=agent)
        if deliverysts:
            dlvry=dlvry.filter(deliverysts=deliverysts)
        if deliveryagt:
            dlvry=dlvry.filter(deliveryagt=deliveryagt)
        if paymentsts:
            dlvry=dlvry.filter(paymentsts=paymentsts)

        context={
            'dlvry':dlvry
        }
        return render(request,'filter_order.html',context)
    
    elif request.method =='GET':
        return render(request, 'filter_order.html')
    else:
        return HttpResponse('An Exception Occureed')


def edit_delivery(request, id):
    if request.method == 'POST':
        delv_id=order.objects.get(pk=id)
        delv_form=order_form(request.POST, instance=delv_id)

        if delv_form.is_valid():
            delv_form.save()
            messages.info(request, 'Details Updated successfully')
            return render(request, 'delv_edit.html',{
                'delv_form':delv_form,
                'success':True
            })
    else:
        delv_id=order.objects.get(pk=id)
        delv_form=order_form(instance=delv_id)
        return render(request, 'delv_edit.html',{
            'delv_form':delv_form
        })


def replacement_main(request):
    form_repl=replace_form()
    if request.method == 'POST':
        form_repl=replace_form(request.POST)
        if form_repl.is_valid():
            form_repl.save()
            messages.info(request,'Details submitted successfully')
            return redirect('replacement_main')
    
    context={'form_repl':form_repl}

    return render(request, 'replacement.html',context)



def filter_replacement(request):
    if request.method =='POST':
        date=request.POST['date']
        recv_challan=request.POST['recv_challan']
        client=request.POST['client']
        item=request.POST['item']
        agent=request.POST['agent']
        status=request.POST['status']
        delv_doc=request.POST['delv_doc']
        delv_date=request.POST['delv_date']

        repl=replacement.objects.all()

        if date:
            repl=repl.filter(date__icontains =date)
        if recv_challan:
            repl=repl.filter(recv_challan__icontains =recv_challan)
        if client:
            repl=repl.filter(client__icontains =client)
        if item:
            repl=repl.filter(item__icontains =item)
        if agent:
            repl=repl.filter(agent=agent)
        if status:
            repl=repl.filter(status=status)
        if delv_doc:
            repl=repl.filter(delv_doc__icontains =delv_doc)
        if delv_date:
           repl=repl.filter(delv_date__icontains =delv_date) 
        
        context={
            'repl':repl
        }
        return render(request, 'replacement_filter.html',context)
    elif request.method =='GET':
        return render(request, 'replacement_filter.html')
    else:
        return HttpResponse('An Exception Occureed')


def edit_replacement(request,id):
    if request.method == 'POST':
        repl_id=replacement.objects.get(pk=id)
        repl_form=replace_form(request.POST, instance=repl_id)

        if repl_form.is_valid():
            repl_form.save()
            messages.info(request, 'Details Updated successfully')
            
            return render(request,'replacement_edit.html',{
                'repl_form':repl_form,
                'success':True
            })

    else:
        repl_id=replacement.objects.get(pk=id)
        repl_form=replace_form(instance=repl_id)
        return render(request, 'replacement_edit.html',{
            'repl_form':repl_form
        })

def delete_delivery(request, id):
    if request.method == 'POST':
        dlvry = order.objects.get(pk=id)
        dlvry.delete()
        return HttpResponseRedirect(reverse('filter_delivery'))

def delete_replacement(request, id):
    if request.method == 'POST':
        repl= replacement.objects.get(pk=id)
        repl.delete()
        return HttpResponseRedirect(reverse('filter_replacement'))