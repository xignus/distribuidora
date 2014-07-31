# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(IMG(_src=URL('static','images/logosolo.png'), _alt="P&P distribuciones", _width=""), _href=URL('default','index'), _class="brand")
response.title = "P & P Distribuciones"
response.subtitle = H4("Distribuciones en Salta y Jujuy", _class="span4")

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

if not(session.auth):
    last_option = (T('Entrar'), ((request.controller=='default')&(request.function=='user')), URL('default', 'user/login'), [])
else:
    last_option = (T('Panel'), ((request.controller=='default')&(request.function=='user')), URL('default', 'user/profile'), [])

response.menu = [
    (T('Inicio'), ((request.controller=='default')&(request.function=='index')), URL('default', 'index'), []),
    (T('Empresa'), ((request.controller=='default')&(request.function=='servicios')), URL('default', 'servicios'), []),
    (T('Productos'), ((request.controller=='default')&(request.function=='about')), URL('default', 'about'), []),
    (T('Servicios'), (request.controller=='blog'), URL('blog', 'index'), []),
    (A(I(_class='icon icon-envelope icon-white'), False, "#myModal", _class="contact")),
    last_option
]
