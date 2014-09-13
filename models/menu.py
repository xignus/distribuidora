
# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(IMG(_src=URL('static','images/logoclaro2.png'), _class='logo'),_href='http://pypdistribuciones.com.ar')
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Xignus Argentina - www.xignus.com.ar'
response.meta.keywords = 'alco, canale, conservas, salud'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

if not(session.auth):
    last_option = (A(SPAN(_class='fa fa-sign-in')+' Entrar', ((request.controller=='default')&(request.function=='user')), URL('default', 'user/login')))
    
else:
    last_option = (A(SPAN(_class='fa fa-wrench')+' Panel', ((request.controller=='adminweb')&(request.function=='index')), URL('adminweb', 'index')))


#if not(session.auth):
#      last_option=(A(SPAN(_class='fa fa-sign-in')+" Entrar", ((request.controller=='default')&(request.function=='user')), URL('default', 'user/login'))),
# else:
#     last_option=(A(SPAN(_class='fa fa-wrench')+" Panel", ((request.controller=='adminweb')&(request.function=='index')), URL('adminweb', 'index'))),

response.menu = [
    (A(SPAN(_class='fa fa-home')+" Inicio", ((request.controller=='default')&(request.function=='index')), URL('default', 'index'))),
    (A(SPAN(_class='fa fa-building')+" Empresa", ((request.controller=='default')&(request.function=='empresa')), URL('default', 'empresa'))),
    (A(SPAN(_class='fa fa-cubes')+" Productos", ((request.controller=='default')&(request.function=='productos')), URL('default', 'productos'))),
    (A(SPAN(_class='fa fa-envelope')+" Contacto", False, "#myModal", _class="contacto")),
    last_option,
]

response.webmenu = [
    
]
if "auth" in locals(): auth.wikimenu() 
