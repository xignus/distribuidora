#-*- coding: utf-8 -*-

def slideshow():
    nueva=SQLFORM(db.slideshow)
    if nueva.process().accepts:
        pass
    elif nueva.errors:
        response.flash="Errors!"
        
    return dict(nueva=nueva)
