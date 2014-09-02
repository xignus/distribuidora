#-*- coding: utf-8 -*-
@auth.requires_membership('adminweb')
def index():
    return dict()

@auth.requires_membership('adminweb')
def slideshow():
    db.slideshow.id.readable=False
    nueva=SQLFORM(db.slideshow)
    if nueva.process().accepts:
        pass
    elif nueva.errors:
        response.flash="Errors!"

    nueva.add_button("Cancel",URL(r=request,f='slideshow'))
    lista=db(db.slideshow.id>0).select()
    return dict(nueva=nueva, lista=lista)

@auth.requires_membership('adminweb')
def productos():
    # nuevo = SQLFORM(db.productos)

    # if nuevo.process().accepts:
    #     session.flash="El producto ha sido agregado"
    # elif nuevo.errors:
    #     response.flash="Por favor revise los datos"
    db.productos.id.readable=False
    lista = SQLFORM.grid(db.productos, ui='jquery-ui', user_signature=False)

    return dict(lista=lista)

@auth.requires_membership('adminweb')
def empresa():
    db.empresa.id.readable=False
    if (db(db.empresa.id>0).select()):
        empresa=SQLFORM(db.empresa, 1)
    else:
        empresa=SQLFORM(db.empresa)

    if empresa.process().accepts:
        session.flash="Se han guardado los datos correctamente"
    elif empresa.errors:
        response.flash="Revise los datos"
    return dict(empresa=empresa)
    
@auth.requires_membership('adminweb')
def servicios():
    listado=db(db.detalles.servicio==db.servicios.id).select()

    nuevo = SQLFORM(db.servicios)

    if nuevo.process().accepted:
        session.flash="Se han guardado los datos correctamente"
        redirect(URL('adminweb','nuevoservicio', args=(nuevo.vars.id)))
    elif nuevo.errors:
        response.flash="Revise los datos"

    return dict(listado=listado, nuevo=nuevo)
    
@auth.requires_membership('adminweb')
def nuevoservicio():
    db.detalles.id.readable=False
    db.detalles.servicio.readable=False
    db.detalles.servicio.writable=False
    db.detalles.servicio.default=int(request.args(0))
    if request.args(1):
        nuevo=SQLFORM(db.detalles, request.args(1))
    else:
        nuevo=SQLFORM(db.detalles)

    if nuevo.process().accepted:
        session.flash="Se han guardado los datos correctamente"
        redirect(URL('adminweb','servicios'))
    elif nuevo.errors:
        response.flash="Revise los datos"
    else:
        response.flash="Por favor complete los datos"

    return dict(nuevo=nuevo)

@auth.requires_membership('adminweb')
def editarservicio():
    return dict()

@auth.requires_membership('adminweb')
def misdatos():
    myid=crud.update(db.auth_user, session.auth.user.id)
    return dict(myid=myid)
