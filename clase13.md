# Clase 13

1. 32 estudiantes
2. -
3. No
4. Bondi
5. No ninguno caminando
6. Hay datos faltantes
7. Sí, estudiante: sí
8. No, calzado, bondi y fecha de nacimiento
9. 12

Por un error en los datos el banco incluyò en el veraz a un hombre inocente
Que son unos pelotudos que no checkearon ni los datos ni la información ni quisieron eascuchar al tipo
Los dos porque si el banco hubiera tenido buenos datos no hubiera tenido que pagar esa suma y él no se hubiera visto inhabilitado a trabajar

Calidad de datos: consistencia, veracidad y completitud de la información recopilada

Consecuencias de datos de mala calidad: toma de malas decisiones, plata perdida, tiempo perdido, gente infeliz, mal manejo de las situaciones

Faltan datos
Grupo_edad_desc no se entienden
El id de grupo_edad ees poco preciso
No podemos identificar caso por caso
Nombres de las columnas estan mal, se mezclan datos semanas epidemiológicas con evento nombre, grupo_edad_id con grupo_edad_desc
Solapados rangos de edad
No hay casos de zika, solo dengue
viene de hacer un join

Medidas: renombrar columnas y poner datos donde corresponden, normalizar la tabla, dividir en más de una tabla, mejorar el manejo de los NULLs, que sean consistentes las formas en las que están escritas las cosas (tildes, mayúsculas, demás, que dos formas de escribir lo mismo se reemplacen por una única), asegurarse que los rangos de edad estén bien


Causas de la mala calidad: unir información no standarizadad de distintas fuentes, malos relevamientos, gente que no sabe lo que hace y tampoco entiende lo que hace, preguntas que admitan más de una posible (infinitas) respuesta, gente que completa mal las cosas (a propósito o inintencionalmente), que se haya caido/perdido la información y su recuperación sea costosa, recopilar datos que pueden repetirse

Características de los datos de buena calidad: ser confiables, ser precisos, verídicos, consistenes, completos, que puestos en una tabla cumplan con las formas normales, unívocos, que respeten el marco legal, relevantes, relacionables

Cuán buena es la calidad de los datos: necesitamos un nivel de medición que es subjetivo al proyecto, es buena la calidad cuando podemos hacer lo propuesto sin muchas dificultades y podemos relacionarlos

Goal: queremos checkear la correctitud de los datos del atributo evento_nombre
Question: ¿Cuántos datos no corresponden al tipo esperado?
Metric: Checkear cuántos datos no corresponden con Dengue y/o zika, cuantos son números, respecto del total 


Goal: queremos checkear la completitud de los datos del atributo departamento_nombre
Question: ¿Cuántos datos estan incompletos?
Metric: Checkear cuántos departamentos no aparecen respecto del total : (depto_nombre == dpto_id + departamento_nombre == null/datos que no estén correctos)/total