#-*- coding: utf-8 -*-

db.define_table('slideshow',
                Field('titulo'),
                Field('imagen','upload'),
                Field('descripcion'),
)
