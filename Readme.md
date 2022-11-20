- [**Predicción de Dengue en Colombia**](#predicción-de-dengue-en-colombia)
  - [**Introducción**](#introducción)
  - [**Datos**](#datos)
  - [Bibliografía](#bibliografía)
# **Predicción de Dengue en Colombia**
## **Introducción**
El Dengue es una problemática de salud de gran relevancia en Colombia, ya que dado su clima tropical es una enfermadad endémica en este país y el vector que lo transmite (*Aedes aegypti*) está presente en el 90% del territorio nacional. Además, en el periodo entre 1999 y 2016 la tasa de letalidad por dengue pasó de 1.3% a 19% [1], en contraste con lo sugerido por la Organización Mundial de la Salud (OMS), que la letalidad por dengue no debe superar el 2% [2]. Por lo tanto, es crucial la vigilancia y prevención del dengue en Colombia, sin embargo, esta tarea equivale a un reto para el sistema de salud Colombiano, debido a la dificultad de las tareas de monitoreo, a la necesidad de información actualizada y disponible para los distintos actores, situación que emperora en las zonas de dificil acceso. 

Por esta razón,  nace la pregunta **¿Es posible construir un sistema de predicción de casos de dengue en Colombia a partir de variables sociodemográficas y medioambientales?** Además de responder la anterior pregunta, este proyecto busca: 

- Identificar y describir las principales variables sociodemográficas y/o medioambientales que influyen en la propagación de dengue en Colombia.
- Implementar un algoritmo de predicción de casos de dengue en Colombia con el fin de facilitar actividades de vigilancia y monitoreo.
- Construir indicadores de alerta para identificar zonas en riesgo de brote de dengue que permitan la toma de acciones preventivas oportunamente
- Clasificar la situación de dengue a nivel nacional a lo largo del tiempo con el fin de poder evaluar la evolución del dengue en el país. 

## **Datos**
Los datos empleados corresponden al reto de Kaggle [Dengue Tabular Data and Satellite Images](https://www.kaggle.com/datasets/davidrestrepo/dengue) enmarcado en el evento *MakeHealth LATAM 2022* y corresponden a las archivos en la carpeta *data* (la fuente puede contener más datos ya que solo se agregan los datos relevantes para el desarrollo del proyecto).

Los datos se particionaron en 3 espacios o zonas: raw, trusted y refined, siguiendo un esquema de DataLake con el fin de garantizar la seguridad y fiabilidad de los datos, así como también matener un ambiente escalable y facilmente administrable.
 
- Raw: se almacenan los datos fuente sin modificaciones. 
- Trusted: se almacenan los datos luego de transformarlos según las necesidades de negocio. En este caso, se agregan los datos disminuyendo su granularidad. 
- Refined: se almacenan los resultados o los datos utlizados en producción. Aquí se almacenan las predicciones realizadas por el modelo. 

A continuación, se ejemplifica el esquema utlizado: 
```
├── Readme.md
├── requirements.txt
├── code
|        ├── preprocessing.py     
├── data
|        ├── raw
|        |   ├── Dengue_Dataset(Medellin).csv
|        |   ├── dengue_data_all_municipalities.csv    
|        ├── refined
|        ├── trusted
|            ├── dengue_data.csv         
└── notebooks
|        ├── Data_Wrangling.ipynb
|        ├── EDA1.ipynb
|        ├── Model_Implementation.ipynb
|        ├── preprocessing.ipynb

```

En la carpeta *notebooks* se almacenan los jupyter notebooks empleados para el desarrollo del proyecto, el flujo de ejecución determinado es *preprocessing.ipynb* -> *Data_Wrangling.ipynb* -> *Model_Implementation.ipynb*, ya que de esta manera se realizó el trabajo del proyecto, no obstante, pueden correrse en el orden deseado. 

## Bibliografía
[1] Ochoa-Ortega MR, Casanova-Moreno M de la C, DíazDominguez M de los Á. Análisis sobre el dengue, su agente transmisor y estrategias de prevención y control. Rev Arch Médico Camagüey [Internet]. 2015 [citado el 31 de enero de 2022];19(2):189–202. Disponible en: http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S1025-02552015000200013&lng=es&nrm=iso&tlng=es

[2] J. Quintero Espinosa, «Dengue en Colombia: epidemiología de la reemergencia a la hiperendemia», Rev. salud. bosque., vol. 5, n.º 1, pp. 81–83, sep. 2015.