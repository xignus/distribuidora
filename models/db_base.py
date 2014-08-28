#-*- coding: utf-8 -*-

db.define_table('contacto',
                Field('nombre', requires=IS_NOT_EMPTY()),
                Field('email', requires=IS_EMAIL()),
                Field('mensaje', 'text'),
)
