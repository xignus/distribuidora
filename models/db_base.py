#-*- coding: utf-8 -*-

db.define_table('contacto',
                Field('nombre', requires=IS_NOT_EMPTY()),
                Field('email', requires=IS_EMAIL()),
                Field('mensaje', 'text'),
)

db.define_table('empresa',
                Field('descripcion_empresa','text', widget=ckeditor.widget)
                
)

db.define_table('servicios',
                Field('nombre'),
                formar="%(nombre)s"
)

db.define_table('detalles',
                Field('servicio', db.servicios),
                Field('descripcion','text', widget=ckeditor.widget),
                Field('publicar','boolean')
)
