#-*- coding: utf-8 -*-

db.define_table('slideshow',
                Field('titulo', requires=IS_NOT_EMPTY()),
                Field('imagen','upload'),
                Field('descripcion','text',requires=IS_NOT_EMPTY()),
                Field('activo','boolean',comment='Define si la imagen se mostrara o no en la portada')
)
