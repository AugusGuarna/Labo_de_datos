# Clase 6

Requisitos funcionales = ¿qué aplicación? ¿Qué queremos hacer con estos datos?

Ahora dado un DER vamos a querer mapearlo a un modelo de datos --> va a ser específico del software que vayamos a usar

Oracle, access, sql

cambio en la estructura de datos --> cambiar la programación

cada relación tiene una tabla asociada que está almacenada

nivel interno: cómo se almacenan los datos, estructura, parte del disco, etc

dominio: todos los valores posibles
cada definición de un dominio es una definición lógica
otra forma sería decir nombre de columna y luego atributo

En general, el nombre de una relación como ESTUDIANTE va a indicar el conjunto real de tuplas de
la misma (el estado actual de la relación) mientras que ESTUDIANTE(Nombre, Apellido, . . .) se va a
referir sólo a su esquema

una se refiere al contenido, el otro a la forma

que la clave sea una propiedad del esquema significa que ya viene dado en el contrato. Cuando nos dan la base de datos ya viene

triggers = código
dependencia funcional = X determina Y

entidades fuertes --> 3ra opción es redundante la información

en relación muchos a muchos se ponen las dos claves para permitir combinaciones de las dos claves si fuera una sola entonces un alumno podría estar anotado a una sola materia. recordemos que las keys no pueden repetirse
la clave es código de materia ya que un profesor puede dar varias materias






Cliente(nombre, apellido, _cuil_, email, codigo postal, fecha nac)

Producto(_codigo_, descripción, tamaño)

Factura(_numero_, importe, fecha)

Empleado(nombre, apellido, salario, _cuil_, email, ~nombre departamento~, ~cuil de supervisor~)

departamento(_nombre_, email)

Solicita(~cuil cliente~, ~_codigo producto_~, ~_numero de factura_~)

esRealizadoPor(~_codigo producto_~, ~_cuil empleado_~)








































