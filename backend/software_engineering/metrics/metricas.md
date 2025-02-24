# Tabla de contenidos 
- [Tabla de contenidos](#tabla-de-contenidos)
- [Evaluacion de calidad del software](#evaluacion-de-calidad-del-software)
- [Soporte para la toma de decisiones en proyectos de software](#soporte-para-la-toma-de-decisiones-en-proyectos-de-software)
- [Tipos de metricas](#tipos-de-metricas)
  - [Metricas de producto](#metricas-de-producto)
  - [Metricas de proceso](#metricas-de-proceso)
  - [Metricas de proyecto](#metricas-de-proyecto)

Medidas cuantitativas que se utilizan para evaluar, analizar y mejorar los procesos, productos y proyectos de software. Permiten tomar decisiones informadas y optimizar el desarrollo de software.

# Evaluacion de calidad del software 
La calidad del software es un factor determinante en su exito. Para garantizar un producto confiable y eficiente, se utilizan metricas que permiten medir aspectos como 
- Correccion: Se mide a traves de la densidad de defectos (Kloc miles de lineas de codigo)
- Mantenibilidad: Evaluada con metricas de complejidad del codigo
- Eficiencia: Tiempo de ejecucion y uso de recursos de software 
- Seguridad: Numero de vulnerabilidades detectadas en auditorias de seguridad. 

# Soporte para la toma de decisiones en proyectos de software 
Las metricas proporcionan datos objetivos que permiten tomar decisiones estrategicas basadas en evidencia. Esto ayuda a:
- Evaluar si el proyecto esta dentro del presupuesto y tiempo estimado 
- Justificar la adopcion de nuevas tecnologias o metodologias 
- Predecir riesgos y ajustar estrategias antes de que impacten en el desarrollo


# Tipos de metricas 
## Metricas de producto
Evaluan las caracteristicas del sofrware desarrollado
- Complejidad del codigo
- Numero de lineas de codigo 
- Densidad de defectos 
- Acoplamiento y cohesion

**Ejemplo**
Densidad de defectos = Numero de defectos detectados / Tamaño del codigo en Klocs

1 Kloc = 1000 lineas de codigo

**Mediciones**
0 -> 0.1 Excelente 
.1 -> 1.0 Aceptable 
1.0 -> 5.0 Defectos alarmantes 
-> Reformular codigo

## Metricas de proceso
Miden la eficiencia y efectividad de los procesos de desarrollo 

- Tiempo medio de resolucion de errores 
- Tiempo de desarrollo por fase 
- Cobertura de pruebas 
- Indice de defectos detectados en cada fase

## Metricas de proyecto 
Ayudan a evaluar la gestion del proyecto y su progreso 

- Esfuerzo y costo estimado (modelo Cocomo)
- Velocidad del equipo (Metodologia)
- Indice de cumplimiento de hitos (tareas terminadas vs planificadas)
- Productividad del equipo (funcionalidad entregada por unidad de tiempo)