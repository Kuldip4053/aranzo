from posixpath import ismount
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import *
import re
from django.core.paginator import Paginator
import random
# from shop.forms import EmpDetailsForm

# Create your views here.

def home(request):
    return HttpResponse("hello")

def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def reting(request):
    if "email" in request.session:
        if request.POST:
            rate=request.POST['rate']
            name=request.POST['name']
            product_id=request.POST['product_id']
            email=request.POST['email']
            disc=request.POST['disc']
            print(rate,name,product_id,email,disc)
            spid=product.objects.get(id=product_id)
            rateing.objects.create(rate=rate,name=name,email=email,product=spid,disc=disc)
            return redirect(single_product,id=product_id)
        else:
            return redirect(single_product)
    else:
        return render(request,'login.html')



def profile(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        print(uid)
        con={"uid":uid}
        return render(request,'profile.html',con)
    else:
        return render(request,'login.html')

def profileupdate(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        if request.POST:
            username=request.POST['username']
            email=request.POST['email']
            address=request.POST['address']
            phone=request.POST['phone']
            print(username,email,address,phone)
            request.session['email']=email
            uid.username=username
            uid.email=email
            uid.address=address
            uid.phone=phone
            uid.save()
            # messages.success(request, 'update successful')
            return redirect(category)
        else:
            return render(request,"crud.html")
    else:
        return render(request,'login.html')


def cart(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        cid=add_cart.objects.filter(user=uid)
        l1=[]
        for i in cid:
            l1.append(i.t )
        total=sum(l1)      
        con={"cid":cid,"total":total}
        return render(request,'cart.html',con)
    else:
        return render(request,'login.html')

def search(request):
    mid=main_Category.objects.all()
    if request.POST:
        search=request.POST['search']
        print(search)
        if search:
            pid=product.objects.filter(name__contains=search)
        
    con={"pid":pid,"mid":mid}
        
    return render(request,'category.html',con)

def category(request):
    # if "email" in request.session:
        pid=product.objects.all()
        mid=main_Category.objects.all()
        p1=product.objects.all()#[0:1]
        p1=random.choices(p1,k=4)
        print("dfsghdfshjdfsf",p1)
        l1=[]
        if "email" in request.session:
            uid=user.objects.get(email=request.session["email"])
            wid=add_wishlist.objects.filter(user=uid)
            for i in wid:
                l1.append(i.product.id)
        c_id=request.GET.get("c_id")
        lth=request.GET.get("lth")
        htl=request.GET.get("htl")
        atz=request.GET.get("atz")
        zta=request.GET.get("zta")
        if c_id:
            pid=product.objects.filter(category=c_id)
        elif lth:
            pid=product.objects.order_by("price")    
        elif htl:
            pid=product.objects.order_by("-price")    
        elif atz:
            pid=product.objects.order_by("name")    
        elif zta:
            pid=product.objects.order_by("-name")    
        else:
            pid=product.objects.all()

        paginator=Paginator(pid,1)
        page_number=request.GET.get("page",1)   
        pid=paginator.get_page(page_number) 
        elided=paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=1)
        con={"pid":pid,"mid":mid,"l1":l1,"elided":elided}

        return render(request,'category.html',con)
    # else:
    #     return render(request,'login.html')




def billingaddress(request):
    if "email" in request.session:
        if request.POST:
            name=request.POST['name']
            phone=request.POST['phone']
            email=request.POST['email']
            address=request.POST['address']
            # country=request.POST['country']
            zipcode=request.POST['zipcode']
            # con={"email":request.session["email"]}
            print(name,email,phone,address,zipcode)
            billing_address.objects.create(name=name,phone=phone,email=email,address=address,zipcode=zipcode)
            return redirect(check)
        return render(request,'check.html')
    else:
        return render(request,'login.html')



# def checkout(request):
#     uid=user.objects.get(email=request.session["email"])
#     cid=add_cart.objects.filter(user=uid)
#     l1=[]
#     for i in cid:
#         l1.append(i.t )
#     total=sum(l1)      
#     ftotle=total+50
#     con={"cid":cid,"total":total,"ftotle":ftotle}

#     if request.POST:
#         cupancode=request.POST['cupancode']
#         try:
#             ccode=cupan.objects.get(cupan_code=cupancode)
#             c=ccode.discount
#             # print(cupancode)
#             print(c)
            
#         except:
#             # messages.success(request,'invalid password')
#             con.update({"cupan_msg":"invelid cupan"})
#             return render(request,'checkout.html',con)
        
#     return render(request,'checkout.html',con)



def confirmation(request):
    return render(request,'confirmation.html')

def contact(request):
    return render(request,'contact.html')

def elements(request):
    return render(request,'elements.html')

def feature(request):
    return render(request,'feature.html')

# def login(request):
#     if request.POST:
#         email=request.POST['email']
#         password=request.POST['password']
#         print(email,password)
#         con={}
#         uid=user.objects.all()
#         if email!=email:
#             con.update({"email_msg":"email not register"})
#             print(con)
#             return render(request,'login.html',con)

#         else:
#             if email==email and password==password:
#                 con.update({"login_msg":"login successful"})
#                 print(con)
#                 return render(request,'index.html',con)
        
#     return render(request,'login.html')



def login(request):
    if "email" in request.session:
        return redirect("index")
    else:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']
            
            try:
                uid=user.objects.get(email=email)
                if uid.password == password:
                    request.session['email']=email
                    return redirect("index")
                else:
                    messages.success(request,'invalid password')
                    return render(request,'login.html')
            except:
                messages.success(request,'invalid email')
                return render(request,'login.html')

        else:
            return render(request,'login.html')

def logout(request):
    del request.session['email']
    return redirect("login")



def register(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        print(username,email,password)
        con={"username":username,"email":email,"password":password,"c_password":c_password}
        s=0
        for i in username:
            if i.isdigit():
                s+=1

            # username
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if username == "":
            con.update({"user_msg":"username requaird"})
        elif username[0] == " " or username[-1] == " " :
            con.update({"user_msg":"befor or after space not requaird"})
        elif s>=1:
            con.update({"user_msg":"number not velid"})
        elif (regex.search(username) != None):
            con.update({"user_msg":"spesial char not velid"})

            # email
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if email == "": 
            con.update({"email_msg":"email requaird"})
        elif not re.match(regex, email):
            con.update({"email_msg":"email not valid"})

            # password        
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if mat == False : 
            con.update({"password_msg":"password requaird"})
        # reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!#%*?&]{6,20}$"
        # pat = re.compile(reg)
        # mat = re.search(pat, password)
        # if password == "":
        #     con.update({"password_msg":"password requaird"})    
        # if len(password) <= 4 :
        #     con.update({"password_msg":"password requaird"})    
        # elif mat == False:
        #     con.update({"password_msg":"password must be require alphbet and special cherector requaird"})    
        if c_password == "":
            con.update({"c_password_msg":"Confirm password requaird"})    
        elif c_password != password:
            con.update({"c_password_msg":"Password not match"})  

        v=con.keys()
        if len(v) == 4:
            try:
                uid=user.objects.get(email=email)
                messages.success(request,'Email already exist')
                return redirect(register)
            except:
                if password==c_password:
                    user.objects.create(username=username,email=email,password=password)
                    messages.success(request,'register successful')
                    return redirect(login)
                else:
                    messages.success(request,'password and confirm password not match')
        print(con)  
        return render(request,'register.html',con)

    return render(request,'register.html')

def single_blog(request):
    return render(request,'single_blog.html')

def single_product(request,id):
    
    spid=product.objects.get(id=id)
    uid=user.objects.get(email=request.session['email'])
    rat=rateing.objects.filter(product=spid)
    l1=[]
    for i in rat:
        l1.append(i.rate)
    l2=[]    
    for i in range(1,6):
        l2.append(l1.count(i))
    
    a=0 
    try:    
        a=round(sum(l1)/rat.count(),2)
    except:
        pass  
    d1={}  
    for i,n in enumerate(l2):
        d1.update({i+1:n})
    print(d1)    
    contaxt={
        "spid":spid,
        "uid":uid,
        "rat":rat,
        "a":a,
        "d1":d1,
    }
    return render(request,'single_product.html',contaxt)

def tracking(request):
    return render(request,'tracking.html')



def addtocart(request,id):
    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        spid=product.objects.get(id=id)
        print(spid)
        pfid=add_cart.objects.filter(product=spid,user=uid).exists()
        if pfid:
            return redirect(cart)
        else:
            add_cart.objects.create(product=spid,user=uid,name=spid.name,price=spid.price,image=spid.image,qty=1,t=spid.price)
            return redirect(cart)
    else:
        return render(request,'login.html')
    
def wishremove(request,id):
        if "email" in request.session:
            uid=user.objects.get(email=request.session["email"])
            spid=add_wishlist.objects.get(id=id)
            spid.delete()
            return redirect(wish)
        else:
            return render(request,'login.html')
    
def cartremove(request,id):
        if "email" in request.session:
            uid=user.objects.get(email=request.session["email"])
            spid=add_cart.objects.get(id=id)
            spid.delete()
            return redirect(cart)
        else:
            return render(request,'login.html')
    
def addtowishlist(request,id):
    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        spid=product.objects.get(id=id)
        print(spid)
        pfid=add_wishlist.objects.filter(product=spid,user=uid).exists()
        if pfid:
            pfid=add_wishlist.objects.get(product=spid,user=uid)
            pfid.delete()
            return redirect(category)
        else:
            add_wishlist.objects.create(product=spid,user=uid,name=spid.name,price=spid.price,image=spid.image)
            return redirect(wish)
    else:
        return render(request,'login.html')

def wish(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        cid=add_wishlist.objects.filter(user=uid)
        con={"cid":cid}
        return render(request,'wish.html',con)
    else:
        return render(request,'login.html')


def qty_plus(request,id):
    if "email" in request.session:
        aid=add_cart.objects.get(id=id)
        aid.qty+=1
        aid.t=aid.price*aid.qty
        aid.save()  
        return redirect(cart)
    else:
        return render(request,'login.html')


def qty_minus(request,id):
    if "email" in request.session:
        aid=add_cart.objects.get(id=id)
        aid.qty-=1
        aid.t=aid.price*aid.qty
        aid.save()
        if aid.qty == 0:
            aid.delete()
        return redirect(cart)
    else:
        return render(request,'login.html')

def single_cart(request,id):
    if "email" in request.session:
        if request.POST:
            pid=request.POST['pid']
            qty1=request.POST['qty1']
            print(qty1,pid)
            uid=user.objects.get(email=request.session["email"])
            spid=product.objects.get(id=pid)
            total1=spid.price*int(qty1)
            pfid=add_cart.objects.filter(product=spid,user=uid).exists()
            if pfid:
                return redirect(cart)
            else:
                add_cart.objects.create(product=spid,user=uid,name=spid.name,price=spid.price,image=spid.image,qty=qty1,t=total1)

        return redirect(cart)
    else:
        return render(request,'login.html')



import os
def delete_file_in_folder(request):
    folder_path="C:\\Users\\solan\\OneDrive\\Documents\\Desktop\\django project\\myenv\\aranoz\\img\\"
    file_nae="Screenshot_2024-02-10_112133.png"
    xyz=folder_path + file_nae
    print(xyz)
    # file_path = "league_image_media/aus_gohFm4c.jpg"
    # print(file_path)
    # if os.path.exists(file_path):
    os.remove(xyz)
    #     return "ok"
    # else:
    #     return "not ok"
    return HttpResponse()


from django.core.mail import send_mail
import random


def forgot(request):
    if request.POST:
        email=request.POST['email']
        eid=user.objects.filter(email=email).exists()
        con={}
        if eid:
            otp = random.randint(100000,999999)
            eid=user.objects.get(email=email)
            eid.otp=otp
            eid.save()
            send_mail("Password reset in Aranoz",f"your otp is {otp}","kuldipsolanki553@gmail.com",[email])
            con.update({'email':email})
            return render(request,'conform.html',con)

        else:
            con.update({'email_msg':'invalid email'})
            return render(request,'forgot.html',con)

    return render(request,'forgot.html')



def conform(request):
    if request.POST:
        otp=request.POST['otp']
        email=request.POST['email']
        # print(otp)
        # print(email)
        eid=user.objects.get(email=email)
        con={}
        if eid.otp==int(otp):
            con.update({'email':email})
            return render(request,'conf_password.html',con)
        else:
            con.update({'email':email,'email_msg':'invalid otp'})
            return render(request,'conform.html',con)    
    return render(request,'conform.html')


def conf_password(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        con={}
        eid=user.objects.get(email=email)
        if password==c_password:
            eid.password=password
            eid.save()
            messages.success(request,'password update successfuly')
            return redirect(login)
        else:
            con.update({'email':email,'email_msg':'otp does not match'})
            return render(request,'con_password.html',con)
        
    return render(request,'con_password.html',con)




def addressupdate(request,id):
    if "email" in request.session:
        u_id=billing_address.objects.get(id=id)
        if request.POST:
            name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            phone=request.POST['phone']
            zipcode=request.POST['zipcode']
            print(name,email,address,phone)
            u_id.name=name
            u_id.email=email
            u_id.address=address
            u_id.phone=phone
            u_id.zipcode=zipcode
            u_id.save()
        # return render(request,'check.html')
        return redirect(check)
    else:
        return render(request,'login.html')

def addressdelete(request,id):
    if "email" in request.session:
        u_id=billing_address.objects.get(id=id)
        u_id.delete()
        messages.success(request, 'DELETE successful')
        return redirect(check)
    else:
        return render(request,'login.html')

def myorder(request):
    if "email" in request.session:
        if request.POST:
            uid=user.objects.get(email=request.session['email'])
            aid= request.POST['flexRadioDefault']
            code= request.POST['cupancode_c']
            # print(cupan)
            cid=add_cart.objects.filter(user=uid)
            aid=billing_address.objects.get(id=aid)
            print(cid)
            for i in cid:
                order.objects.create(order_id=123,phone=aid.phone,cupan=code,zipcode=aid.zipcode,user=uid,address=aid.address,pname=i.name,qty=i.qty,price=i.price)
                i.delete() 
            if code=="":
                pass
            else:
                cod=cupan.objects.get(cupan_code=code)
                cod.aply=False
                cod.save()
            return redirect(category)
    else:
        return render(request,'login.html')


    
def check(request):
    # if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        cid=add_cart.objects.filter(user=uid)
        adi=billing_address.objects.filter(email=request.session["email"])
        l1=[]
        for i in cid:
            l1.append(i.t )
        total=sum(l1)      
        ftotle=total+50
        discount_amount=0
        con={"uid":uid,"cid":cid,"adi":adi,"email":request.session["email"],"total":total,"ftotle":ftotle,"discount_amount":discount_amount}

        if request.POST:
            cupancode=request.POST['cupancode']
            ccode=cupan.objects.filter(cupan_code=cupancode).exists()
            if ccode :
                ccode=cupan.objects.get(cupan_code=cupancode)
                if ccode.aply==True:
                    ftotle=ftotle-ccode.discount
                    request.session['coupon']=ccode.discount
                    discount_amount=ccode.discount
                    con.update({"ftotle":ftotle,"discount_amount":discount_amount,"cupancode":cupancode })
                    return render(request,'check.html',con)
                else:
                    con.update({"cupan_msg":"cupan alreadhy used"})
                    return render(request,'check.html',con)
            else:
                con.update({"cupan_msg":"invelid cupan"})
                return render(request,'check.html',con)
            
        return render(request,'check.html',con)
    # else:
    #     return render(request,'login.html')

