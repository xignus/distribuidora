# -*- coding: utf-8 -*-

def index():
    return dict()

def portada():
    nueva=SQLFORM(db.portada)

    if nueva.process().accepts:
        response.flash="La imagen ha sido agregada"
    elif nueva.errors:
        response.flash="Revise los datos"

    imagenes=db(db.portada.id>0).select()

    return dict(nueva=nueva, imagenes=imagenes)
