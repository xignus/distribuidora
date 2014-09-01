#-*- coding: utf-8 -*-

def index():
    return dict()

def slideshow():
    nueva=SQLFORM(db.slideshow)
    if nueva.process().accepts:
        pass
    elif nueva.errors:
        response.flash="Errors!"
    lista=db(db.slideshow.id>0).select()
    return dict(nueva=nueva, lista=lista)

def productos():
    # nuevo = SQLFORM(db.productos)

    # if nuevo.process().accepts:
    #     session.flash="El producto ha sido agregado"
    # elif nuevo.errors:
    #     response.flash="Por favor revise los datos"
    db.productos.id.readable=False
    lista = SQLFORM.grid(db.productos, ui='jquery-ui', user_signature=False)

    return dict(lista=lista)

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

def servicios():
    listado=db((db.servicios.id>0)&(db.detalles.servicio==db.servicios.id)&(db.detalles.publicar==True)).select()

    nuevo = SQLFORM(db.servicios)

    if nuevo.process().accepted:
        session.flash="Se han guardado los datos correctamente"
        redirect(URL('adminweb','nuevoservicio', args=(nuevo.vars.id)))
    elif nuevo.errors:
        response.flash="Revise los datos"

    return dict(listado=listado, nuevo=nuevo)

def nuevoservicio():
    db.detalles.id.readable=False
    db.detalles.servicio.readable=False
    db.detalles.servicio.writable=False
    db.detalles.servicio.default=int(request.args(0))
        
    nuevo=SQLFORM(db.detalles)

    if nuevo.process().accepts:
        session.flash="Se han guardado los datos correctamente"
    elif nuevo.errors:
        response.flash="Revise los datos"
    else:
        response.flash="Por favor complete los datos"

    return dict(nuevo=nuevo)

def editarservicio():
    return dict()
