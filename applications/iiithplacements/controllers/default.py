# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
def company():
    w=db(db.Registered_recruiters).select()
    return locals()

def index():
    response.flash = T("Welcome to IIIT -H Placement Portal !")
    return locals()

def next():
    return locals()

def why():
    return locals()

def info():
    table=db(db.Placements).select()
    return locals()

@auth.requires_login()
def registration1():
    table=db(db.Profile_for_others_to_see).select()
    x=auth.user.email
    table1=db(db.Registered_recruiters).select()
    flag1=0
    for i in table1:
        if x==i.e_mail:
            flag1=1
            break
    flag=0
    for i in table:
        if auth.user.email==i.e_mail and flag1!=1:
            x=i.id
            flag=1
            redirect(URL('particularprofile',vars={'a':x}))
    if flag==0:
        redirect(URL('stud_or_rec'))
    return locals()

def stud_or_rec():
    if auth.has_membership('Students') or auth.has_membership('Recruiters'):
        redirect(URL('index'))
    return locals()

j=0
def registration():
    global j
    x=request.vars.hello
    y=auth.user.id
    if x=='Students':
        z=16
        db.auth_membership.insert(user_id=y,group_id=z)
        redirect(URL('profile1'))
    elif x=='Recruiters':
        z=15
        db.auth_membership.insert(user_id=y,group_id=z)
        redirect(URL('recruiters2'))
    j+=1
    return locals()

def booklet():
    redirect('http://iiit.ac.in/institute/booklet')
    return locals()

def recruiters():
    return locals()

def recruiters1():
    x=request.vars.alphabet
    table=db(db.Recruiters).select()
    return locals()

def recruiters2():
    z=auth.user.email
    table=db(db.Registered_recruiters).select()
    for i in table:
        if z==i.e_mail:
            redirect(URL('seeprofile'))
    x=auth.user.id
    y=db.auth_user(x).email
    db.Registered_recruiters.e_mail.default=y
    db.Registered_recruiters.e_mail.writable=False
    db.Registered_recruiters.e_mail.readable=False
    form=SQLFORM(db.Registered_recruiters).process()
    return locals()

def seeprofile():
    table=db(db.Registered_recruiters).select()
    z=auth.user.email
    for i in table:
        if z==i.e_mail:
            x=i.Name_of_company
            y=i.Total_people_wanted
            z=i.e_mail
            break
    return locals()

def profile1():
    y=0
    table=db(db.Profile_for_others_to_see).select()
    for i in table:
        if auth.user.email==i.e_mail:
            x=i.id
            y=1
            break
    if y==1:
        redirect(URL('particularprofile',vars={'a':x}))
    else:
        redirect(URL('createprofiles'))
    return locals()

def departments():
    return locals()

def total():
    table=db(db.Recruiters).select(orderby=db.Recruiters.name_of_company)
    return locals()

def contactus():
    return locals()

@auth.requires_login()
def profiles():
    flag=0
    y=auth.user.id
    email1=db(db.auth_user).select()[y-1].email
    table=db(db.Profile_for_others_to_see).select()
    for i in table:
        if email1==i.e_mail:
            x=i.id
            flag=1
            break
    if flag==1:
        redirect(URL('particularprofile',vars={'a':x}))
    else:
        redirect(URL('createprofiles'))
    return locals()

def createprofiles():
    x=auth.user.id
    info3=db.auth_user(x).email
    name=auth.user.first_name+" "+auth.user.last_name
    db.Profile_for_others_to_see.e_mail.default=info3
    db.Profile_for_others_to_see.e_mail.writable=False
    db.Profile_for_others_to_see.e_mail.readable=False
    db.Profile_for_others_to_see.student_name.default=name
    db.Profile_for_others_to_see.student_name.writable=False
    form=SQLFORM(db.Profile_for_others_to_see).process()
    return locals()

def particularprofile():
    x=auth.user.first_name+" "+auth.user.last_name
    response.flash=T("Welcome to your profile %s !" %x)
    y=request.vars.a
    info3=db.Profile_for_others_to_see(y)
    return locals()

def particularprofile1():
    y=request.vars.a
    table=db(db.Profile_for_others_to_see).select()
    return locals()

def message_to_student():
    if auth.has_membership('Recruiters'):
        if len(request.args)!=0:
            l=request.args[0]
            name=l.replace('_',' ')
            db.msg_to_stud.name_of_student.default=name
            db.msg_to_stud.name_of_student.writable=False
        table=db(db.Registered_recruiters).select()
        x=auth.user.email
        for i in table:
            if i.e_mail==x:
                y=i.Name_of_company
                break
        msg='Hi, you have been selected for intern at our company.Drop in with you full details for interview.'
        db.msg_to_stud.messaged_by.default=y
        db.msg_to_stud.messaged_by.writable=False
        db.msg_to_stud.message_is.default=msg
        #db.msg_to_stud.message_is.writable=False
        table1=SQLFORM(db.msg_to_stud).process()
    if auth.has_membership('Students'):
        x=auth.user.first_name+" "+auth.user.last_name
        db.msg_to_rec.messaged_by.default=x
        db.msg_to_rec.messaged_by.writable=False
        if len(request.args)!=0:
            l=request.args[0]
            str1=l.replace('_',' ')
            db.msg_to_rec.messaged_to.default=str1
            db.msg_to_rec.messaged_to.writable=False
        table1=SQLFORM(db.msg_to_rec).process()
    return locals()

def show_messages():
    if auth.has_membership('Recruiters'):
        redirect(URL('msg_recruiter'))
    if auth.has_membership('Students'):
        redirect(URL('msg_student'))
    return locals()

def msg_student():
    table=db(db.msg_to_stud).select()
    name=auth.user.first_name+" "+auth.user.last_name
    return locals()

def msg_recruiter():
    table=db(db.msg_to_rec).select()
    table1=db(db.Registered_recruiters).select()
    x=auth.user.first_name+" "+auth.user.last_name
    q=auth.user.email
    return locals()

@auth.requires_login()
def recruiterlogin():
    redirect(URL('recruiterlogin1'))
    return locals()

@auth.requires_membership('Recruiters')
def recruiterlogin1():
    response.flash=T("Welcome Recruiter !!")
    info1=db(db.Profile_for_others_to_see).select(orderby=db.Profile_for_others_to_see.student_name.upper())
    info2=db(db.Placements).select()
    return locals()

def update_profile():
    from gluon.tools import Crud
    crud=Crud(db)
    x=auth.user.email
    table=db(db.Profile_for_others_to_see).select()
    for i in table:
        if x==i.e_mail:
            y=i.id
            break
    name=auth.user.first_name+" "+auth.user.last_name
    db.Profile_for_others_to_see.student_name.default=name
    db.Profile_for_others_to_see.student_name.writable=False
    update=crud.update(db.Profile_for_others_to_see,y)
    return locals()

def user():
    return dict(form=auth())

@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()


@auth.requires_login()
def api():
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
