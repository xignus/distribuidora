# -*- coding: utf-8 -*-

db.define_table('portada',
                Field('titulo','string'),
                Field('descripcion','text'),
                Field('imagen','upload'),
                Field('fecha','date', default=request.now)
                
)

db.define_table('empresa',
                Field('titulo'),
                Field('info', 'text')
)

