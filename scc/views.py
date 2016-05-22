from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from scc.models import User_Infomation,uhome_admin,skill_admin
import time
import re

#===========================================================================
#===============    用户注册登入注销      ============


#注册
# noinspection SpellCheckingInspection
def regist(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        passwordre = request.POST['password_confirm']
        sex = request.POST['optionsRadios']
        dict = {}
        if User_Infomation.objects.filter(email__exact=email):
            y = False
            dict['infoE'] = ' (邮箱地址已被使用，自己换一个)'
        else:
            y = True
            dict['infoE'] = ''
        if (password == passwordre)  & y:
                #======================
                skillad = skill_admin()
                skillad.name = name
                skillad.emial = email
                skillad.precent1 = '0'
                skillad.precent2 = '0'
                skillad.precent3 = '0'
                skillad.precent4 = '0'
                skillad.precent5 = '0'
                skillad.precent6 = '0'
                skillad.precent7 = '0'
                skillad.precent8 = '0'
                skillad.skill1 = 'None'
                skillad.skill2 = 'None'
                skillad.skill3 = 'None'
                skillad.skill4 = 'None'
                skillad.skill5 = 'None'
                skillad.skill6 = 'None'
                skillad.skill7 = 'None'
                skillad.skill8 = 'None'
                skillad.study1 = 'None'
                skillad.study2 = 'None'
                skillad.study3 = 'None'
                skillad.study4 = 'None'
                skillad.study5 = 'None'
                skillad.study6 = 'None'
                skillad.study7 = 'None'
                skillad.study8 = 'None'
                #================
                ad = uhome_admin()
                ad.email = email
                ad.name = name
                ad.basicSkill ='skill'
                ad.hobby ='hobby'
                ad.edu ='edu'
                ad.basicInFo ='basicInFo'
                ISOTIMEFORMAT='%Y-%m-%d %X'
                now_time = time.strftime(ISOTIMEFORMAT,time.localtime())
                ad.time = now_time
                #======================
                user = User_Infomation()
                user.password = password
                user.email = email
                user.name = name
                user.sex = sex
                #====user 保持=====
                user.save()
                #====ad 保存=====
                ad.save()
                #===skillad保存====
                skillad.save()
                #返回注册成功页面
                return render(request,'success.html',{'name':name})
        else:
            return render(request, 'regist.html',dict)
    else:
        return render(request, 'regist.html')

#登陆
def login(req):
    if User_Infomation.objects.filter(name__exact=req.session.get('name'),email__exact=req.session.get('email')):
        return HttpResponseRedirect('/uhome/')
    else:
        if req.method == "POST":
            #获取表单用户密码
            #获取的表单数据与数据库进行比较
            name = req.POST["name"]
            email = req.POST['email']
            user = User_Infomation.objects.filter(name__exact=name,email__exact=email)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/uhome/')
                req.session['name'] = name
                req.session['email'] = email
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login/')
        else:
            return render(req, 'login.html')

def login2(req):
    if User_Infomation.objects.filter(name__exact=req.session.get('name'),email__exact=req.session.get('email'),password__exact=req.session.get('password')):
        return HttpResponseRedirect('/userAdmin/')
    else:
        if req.method == "POST":
            #获取表单用户密码
            #获取的表单数据与数据库进行比较
            password = req.POST["password"]
            name = req.POST["name"]
            email = req.POST["email"]
            user = User_Infomation.objects.filter(name__exact=name,password__exact=password,email__exact=email)
            if user:
                #比较成功，跳转index
                req.session['name'] = name
                req.session['email'] = email
                req.session['password'] = password
                response = HttpResponseRedirect('/userAdmin/')
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login2/')
        else:
            return render(req, 'login2.html')
def login3(req):
    if User_Infomation.objects.filter(name__exact=req.session.get('name'),email__exact=req.session.get('email'),password__exact=req.session.get('password')):
        return HttpResponseRedirect('/adminskill/')
    else:
        if req.method == "POST":
            #获取表单用户密码
            #获取的表单数据与数据库进行比较
            password = req.POST["password"]
            name = req.POST["name"]
            email = req.POST["email"]
            user = User_Infomation.objects.filter(name__exact=name,password__exact=password,email__exact=email)
            if user:
                #比较成功，跳转index
                req.session['name'] = name
                req.session['email'] = email
                req.session['password'] = password
                response = HttpResponseRedirect('/adminskill/')
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/login3/')
        else:
            return render(req, 'login2.html')


#========       区别对待登入用户和未登入用户        =========
#可以用装饰器
#@login_required
#def user_only(request):
#   return HttpResponse("<p>This message is for logged in user only.</p>")


#===========      用户账号自主管理       ===========
def user_manage(req):
    user_name = req.user.get_username()#用户名
    user_fullname = req.user.get_full_name()#用户姓名
    user_lastlogin = req.user.last_login#上次登入时间
    user_creativetime = req.user.date_joined#用户创建时间

#============user_admin===============

def user_admin(request):
        if check_login2(request):
            if request.method == "POST":
                name = request.session.get('name')
                email = request.session.get('email')
                user = uhome_admin.objects.get(name__exact=name,email__exact=email)
                if 'basicInFo' in request.POST:
                    basicInFo = request.POST['basicInFo']
                    user.basicInFo = basicInFo
                if 'hobby' in request.POST:
                    hobby = request.POST['hobby']
                    user.hobby = hobby
                if 'edu' in request.POST:
                    edu = request.POST['edu']
                    user.edu = edu
                ISOTIMEFORMAT='%Y-%m-%d %X'
                now_time = time.strftime(ISOTIMEFORMAT,time.localtime())
                user.time = now_time
                user.save()
                return HttpResponseRedirect('/userAdmin/')
            else:
                return render(request,'userAdmin.html',{'us':get(request)})
        else:
            return HttpResponseRedirect('/login2/')

def Myskill_admin(request):
        if check_login2(request):
            if request.method == "POST":
                name = request.session.get('name')
                email = request.session.get('email')
                user = skill_admin.objects.get(name__exact=name,email__exact=email)
                if 'skill 1' in request.POST:
                    user.skill1 = request.POST['skill 1']
                    user.skill2 = request.POST['skill 2']
                    user.skill3 = request.POST['skill 3']
                    user.skill4 = request.POST['skill 4']
                    user.skill5 = request.POST['skill 5']
                    user.skill6 = request.POST['skill 6']
                    user.skill7 = request.POST['skill 7']
                    user.skill8 = request.POST['skill 8']
                    user.precent1 = request.POST['percent 1']
                    user.precent2 = request.POST['percent 2']
                    user.precent3 = request.POST['percent 3']
                    user.precent4 = request.POST['percent 4']
                    user.precent5 = request.POST['percent 5']
                    user.precent6 = request.POST['percent 6']
                    user.precent7 = request.POST['percent 7']
                    user.precent8 = request.POST['percent 8']
                if 'study 1' in request.POST:
                    user.study1 = request.POST['study 1']
                    user.study2 = request.POST['study 2']
                    user.study3 = request.POST['study 3']
                    user.study4 = request.POST['study 4']
                    user.study5 = request.POST['study 5']
                    user.study6 = request.POST['study 6']
                    user.study7 = request.POST['study 7']
                    user.study8 = request.POST['study 8']
                user.save()
                return HttpResponseRedirect('/adminskill/')
            else:
                return render(request,'adminskill.html',{'us':get(request)})
        else:
            return HttpResponseRedirect('/login2/')



#================================layout=============================
def HomePage(request):
    return render(request, 'HomePage.html')
def User_story(request):
    if check_login(request):
        return render(request, 'TheStory.html')
    else:
        return HttpResponseRedirect('/login/')
def uhome(request):
    if check_login(request):
        name = request.session.get('name')
        email = request.session.get('email')
        user = uhome_admin.objects.get(name__exact=name,email__exact=email)
        dict = {}
        dict['basicInFo'] = user.basicInFo
        dict['hobby'] = user.hobby
        dict['edu'] = user.edu
        dict['us'] = name
        return render(request,'user_home.html',dict)
    else:
        return HttpResponseRedirect('/login/')
def skill(request):
    if check_login(request):
        name = request.session.get('name')
        email = request.session.get('email')
        user = skill_admin.objects.get(name__exact=name,email__exact=email)
        dict = {}
        dict['skill1'] = user.skill1
        dict['skill2'] = user.skill2
        dict['skill3'] = user.skill3
        dict['skill4'] = user.skill4
        dict['skill5'] = user.skill5
        dict['skill6'] = user.skill6
        dict['skill7'] = user.skill7
        dict['skill8'] = user.skill8
        dict['us'] = get(request)
        dict['percent1'] = user.precent1
        dict['percent2'] = user.precent2
        dict['percent3'] = user.precent3
        dict['percent4'] = user.precent4
        dict['percent5'] = user.precent5
        dict['percent6'] = user.precent6
        dict['percent7'] = user.precent7
        dict['percent8'] = user.precent8
        dict['study1'] = user.study1
        dict['study2'] = user.study2
        dict['study3'] = user.study3
        dict['study4'] = user.study4
        dict['study5'] = user.study5
        dict['study6'] = user.study6
        dict['study7'] = user.study7
        dict['study8'] = user.study8
        return render(request,'skill.html',dict)
    else:
        return HttpResponseRedirect('/login/')

#=================check & get===========================
def check_login(request):
    name = request.session.get('name')
    if name == None:
        return False
    else:
        return True
def check_login2(request):
    name = request.session.get('name')
    if name == None:
        return False
    else:
        return True

def get(request):
    name = request.session.get('name')
    return name

#=====================================================

def logout(request):
    del request.session['name']
    del request.session['email']
    if 'password' in request.session:
        del request.session['password']
    return render(request,'HomePage.html')
#====================re=======================
def tobr(str):
    pattern = re.compile('\n')
    return re.sub(pattern,'<br>',str)


