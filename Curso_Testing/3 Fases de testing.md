# Fases del testing

## Fase 1: Estudio y análisis de requisitos
Es esta fase se estudian las funcionalidades del producto.  
Se estudia toda la documentación, tanto la de los requisitos del cliente como, la documentación de los desarrolladores.  
Lo ideal es que todo el equipo de testing forme parte de este proceso en el que se definen las funcionalidades de software.  

## Fase 2: Análisis y diseño de pruebas
Es una fase de estudio, Los objetivos de esta fase son:  
    - Verificar la funcionalidad del proyecto. Vistazo de lo avanzado que está el proyecto.  
    - Revisar todos los requisitos del proyecto.  
    - Crear una guía del plan del testing (Guideline).  
    - Considerar una guía técnica para la escritura del "Test Plan" (o Test Analysis), que viene siendo el plan de pruebas.  

**Guidelines**: Documento que debe de generarse y presentarse al equipo de pruebas para generar los test case. Los elementos que lo componen tienen que tener nombres muy descriptivos. Se componen normalmente de los siguientes elementos:  
    - Normas generales para la definición del título del "Test Plan".  
    - Indicaciones para la definición de las carpetas del "Test Plan".  
    - Normas generales para la defionición de los títulos de los "Test Cases", cada una de las pruebas que se realizan.  
    - Propuesta para la definición del cuerpo de la prueba.  

**Test Analysis (Test Plan)**: Es básico que todas las conclusiones y análisis que se hagan en esta fase se recojan en uno o varios documentos (Test Analysis) que posteriormente se pasarán al equipo de escritores del "Test Plan". Los elementos del Test Analysis son:  
    - Descripción de las funcionalidades del proyecto.  
    - Análisis de Requisitos.  
    - Herramientas a utilizar para hacer las pruebas. Por ejemplo: Selenia (un web driver).  
    - Estructura del plan posible.  

## Fase 3: Definición de estrategia de pruebas (Test Strategy)
El objetivo de esta fase es definir la estrategia de pruebas y generar un documento que la describa (Test Strategy). Este documento guiará al equipo de testeo para realizar las pruebas en función del contexto de las pruebas. El *Test Strategy* puede constar de los siguientes elemntos:  
    - Descripción de las funcionalidades a probar.  
    - Definir el scope de las pruebas. El Scope es el alcance, definiciendo el alcance de cada prueba.  
    - Tipos de prueba a ejecutar.  
    - Herramientas para testing y gestión.  
    - Calendario de pruebas. Para facilitar el control de los tiempos.  
    - Entorno de pruebas. Puede ser necesario preparar un entorno que emule el sistema de ejecución previstop para la aplicación.  
    - Riesgos del testing. Hay que tener presente siempre los riesgos de cada prueba y, valorar si es necesaria o recomendada otra prueba.  
    - Revisiones y aprobaciones.  
    - Definición de los ciclos de prueba. Hasta dónde hay que llegar con las pruebas y cuando serán sufuciente.  
    - Definición del proceso de incidencias. Se conoce como incidencia, a un proceso negativo no esperado.  
    - Definición de métricas, valores cuantitativos que se utilizan para medir y evaluar diferentes aspectos del proceso de pruebas y la calidad del software que se está probando.  
    - Definición de los criterios de calidad. Criterios para que el software cumple con todos los requisitos.  

## Fase 4: Escritura del plan de pruebas, Test Analysis o Test Plan
Este documento, el tester se va a guíar con este documento y, al mismo tiempo, tambié va a registrar todo lo hecho en él y mejorar la documentación general final del software. En él también se incluye la matriz de trazabilidad, que es técnicamente un mapeo entre las pruebas escritas y los requisitos del cliente que cubre cada prueba.  
Con la matriz de trazabilidad se pretende asegurar que las pruebas cubran que el software cumpla todos los requisitos del cliente, garantizando su funcionalidad.  

## Fase 5: Ejecución del plan de pruebas, Test Analysis o Test Plan
Se recolectan los documentos elaborados y se implementan las pruebas definidas.  
En la fase de ejecución de pruebas, se realizan las siguientes actividades:  
    - Definición y presentación de Guidelines de ejecución.  
    - Presentación del flujo de ejecución de los ciclos.  
    - Personas de referencia en el proyecto. Es importantisimo una buena comunicación entre todos los integrantes.  
    - Seguimiento y reporte de progreso.  

## Fase 6: Evaluación (Testware)
En la fase de evaluación se crea un documento con las conclusiones totales y con los resultados obtenidos.  
El **testware** es el documento con todas las conclusiones e información obtenida en la pruebas, de un test case (prueba única) o el **testware** general con todas las pruebas del proyecto. Los elementos del **testware** son:  
    - Funciones probadas dentro de la App. Para guiarse y registrar las pruebas realizadas.  
    - Equipo de testing. Saber desde quien elaboró la documentación, hasta quién realiza cada test case.  
    - Métricas. Identificación y registrar qué aspectos del proceso de prueba midieron y cómo se hicieron las mediciones.  
    - Conclusión. Registrar los objetivos cumplidos, lo aprendido, las mejoras que se pueden implementar.  

## Fase 7: Cierre y Mantenimiento
Todas las partes involucradas, `Stakeholders` (cliente, desarrolladores, líderes del proyecto,patrocinadores, etc) deben de firmar el cierre del proyecto, formalizando la aceptación del proyecto como completado. La firma marca el final formal del desarrollo del proyecto, entrando en la fase de mantenimiento, que es la fase continua de soporte y mejora del producto ya entregado.  
El mantenimiento debe de ser estipulado, siendo un servicio que se cobra a parte. Por lo que es necesario dejar muy claro las garantías y el mantenimiento posterior al cierre.  
Si el cliente denuncia un defecto, el servicio de mantenimiento debe de analizar si es un defecto, y liberar al cliente de él encontrando una solución.  