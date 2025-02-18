# Tabla de contenidos
- [Tabla de contenidos](#tabla-de-contenidos)
- [Modelo GQM](#modelo-gqm)
- [Plantilla para obtener informacion en modelo GQM](#plantilla-para-obtener-informacion-en-modelo-gqm)
- [Ejemplo](#ejemplo)

# Modelo GQM 
Goal - Question - Metric 

- Se deben tener objetivos medibles
- Un objetivo debe valuarse por metricas 


- Goal: Tener en cuenta un objetivo
- Question: Hacer preguntas en base a la medicion para poder responderla con una metrica
- Metric: Las mediciones para poder evaluar un objeto.


# Plantilla para obtener informacion en modelo GQM 
- **Analizar**: El objeto bajo medicion
- **Con el proposito de**: Entender, controlar o mejorar el objeto
- **Con respecto a**: El enfoque de calidad del objeto en que se centra la medicion 
- **Desde el punto de vista de**: Las personas que miden el objeto 
- **En el contexto de**: El ambiente en el cual la medicion tiene lugar 


# Ejemplo 
Medir la complejidad de una BD a partir de un modelo de diseño relacional para el desarrollo de un sistema de informacion, con el fin de asegurar el facil mantenimiento de la BD 

**Preguntas**:
- Cuantas tablas existen? 
- Cuantos atributos tiene? 
- Cuantas llaves foraneas existen? 
- Cuantas tablas relacionan una llave primaria? 

**Metricas**:
- *num_tablas*
- *num_atributos_totales*
- *num_llaves_foraneas_totales*
- *num_tablas_por_pk*