#-*- coding: utf-8 -*-

def slideshow():
    nueva=SQLFORM(db.slideshow)
    if nueva.process().accepts:
        pass
    elif nueva.errors:
        response.flash="Errors!"
        
    return dict(nueva=nueva)

def productos():
    # nuevo = SQLFORM(db.productos)

    # if nuevo.process().accepts:
    #     session.flash="El producto ha sido agregado"
    # elif nuevo.errors:
    #     response.flash="Por favor revise los datos"
    db.productos.id.readable=False
    lista = SQLFORM.grid(db.productos, ui='jquery-ui', user_signature=False)

    return dict(lista=lista)
