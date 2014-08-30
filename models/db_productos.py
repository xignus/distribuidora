#-*- coding: utf-8 -*-

db.define_table('categorias',
                Field('nombre'),
                format="%(nombre)s"
)

db.define_table('productos',
                Field('nombre'),
                Field('presentacion'),
                Field('categoria', db.categorias),
                Field('marca'),
                Field('imagen','upload')
)
