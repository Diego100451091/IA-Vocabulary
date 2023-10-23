import random
import os
import getpass
import sys
import unicodedata


def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


DICTIONARY = [
    {
        "concept": "Adaline",
        "definition": "Red neuronal de una sola capa con múltiples nodos donde cada nodo acepta múltiples entradas y genera una salida."
    },
    {
        "concept": "ADAS (Advanced Driver-Assistant System)",
        "definition": "Conjunto de sistemas electrónicos diseñados para ayudar a conductores en la conducción, generalmente resultando en aumento de la seguridad."
    },
    {
        "concept": "Adecuación",
        "definition": "Capacidad que tiene un individuo para reproducirse, es decir, la probabilidad de trasnferir su material genético a la siguiente generación"
    },
    {
        "concept": "Agente inteligente",
        "definition": "Sistema perceptivo capaz de interpretar y procesar la información que recibe de su entorno, actuando en consecuencia de acuerdo a los datos que recoge y procesa. La forma de actuar de esta entidad es lógica y racional basándose en las reacciones del comportamiento normal de un sistema en concreto. Utiliza sensores para recibir información y actuadores para ejercer sus funciones."
    },
    {
        "concept": "Agrupamiento",
        "definition": "Tarea de Text Mining usada para la extracción del conocimiento. Consiste en un proceso para agrupar documentos de texto similares en conjuntos. El objetivo principal en Text Mining es identificar patrones y relaciones dentro de una colección de documentos de texto sin la necesidad de etiquetas predefinidas o categorías."
    },
    {
        "concept": "Agrupamiento / Clustering Jerarquizado",
        "definition": "Tipo de algoritmo de clustering en el que genera jerarquía en los datos agrupados como dendogramas."
    },
    {
        "concept": "Algoritmo",
        "definition": "Conjunto ordenado y finito de operaciones que permite hallar la solución de un problema."
    },
    {
        "concept": "Algoritmo Genético",
        "definition": "Método adaptativo que puede usarse para resolver problemas de búsqueda y optimización. Están basados en el proceso genético de los organismos vivos. Estos métodos son capaces de ir creando soluciones para problemas del mundo real. La evolucion de dichas soluciones hacia valores óptimos del problema depende en buena medida de una adecuada codificación de las mismas."
    },
    {
        "concept": "Aprendizaje no supervisado",
        "definition": "Tipo de algoritmo de aprendizaje que infieren patrones de un conjunto de datos sin referencia a resultados conocidos o etiquetados."
    },
    {
        "concept": "Aprendizaje por refuerzo",
        "definition": "Es el área de la inteligencia artificial que está centrada en descubrir qué acciones se deben tomar para maximizar la señal de recomensa. En otras palabras, se centra en cómo mapear situaciones a acciones que se centren en encontrar dicha recompensa."
    },
    {
        "concept": "Árbol de decisión",
        "definition": "Tipo de modelo de aprendizaje supervisado utilizado para clasificación y regresión. Está compuesto por nodos (hojas), que representan los valores/clases y conexiones (ramas), que representan los resultados de las acciones. Este modelo puede ser una representación visual de las consecuencias de las diferentes acciones. ID3 o M5 son ejemplos de este tipo de modelo."
    },
    {
        "concept": "Asociaciones",
        "definition": "Es uno de los tipos de patrones que busca identificar la minería de datos. Representan las relaciones concurrentes más comunes en las cosas."
    },
    {
        "concept": "Autoridad de página",
        "definition": "Métrica que mide la credibilidad, autoridad y calidad de las páginas de un sitio web."
    },
    {
        "concept": "Backpropagation",
        "definition": "Algoritmo de aprendizaje supervisado utilizado para entrenar redes de neuronas. Se comienza en la capa de salida y se arrastran los errores entre las salidas reales y las deseadas, utilizándolos para corregir los pesos de las conexiones de la capa anterior."
    },
    {
        "concept": "Bag-of-words",
        "definition": "Colección simplificada o reducida de palabras que son extraídas de un documento sin considerar la gramática o el orden en que estas van apareciendo. Útil para tareas como la detección de spam en el correo electrónico."
    },
    {
        "concept": "Base de conocimiento",
        "definition": "Se trata de una colección de hechos, reglas y procedimientos esquematizados. Contiene toda la información y conocimiento sobre un campo específico."
    },
    {
        "concept": "Capa Oculta",
        "definition": "Relativa a una red neuronal artificial. Es una capa situada entre las capas de entrada y de salida que sirve de comunicación entre ambas. Se encarga de realizar el procesamiento de la información, tomando un conjunto de entradas ponderadas y produciendo una salida a través de una función de activación. Esto es, realizan el procesamiento no lineal de los patrones recibidos. "
    },
    {
        "concept": "Ciclo Evolutivo",
        "definition": "Esquema que se sigue para actualizar una población o generar una nueva. Consta de los siguientes operadores genéticos; selección, sobrecruzamiento, mutación y reemplazo."
    },
    {
        "concept": "Clasificación",
        "definition": "Es una tarea de minería de datos muy común, que consiste en analizar los datos históricos y crear o construir un modelo que pueda predecir la clase de una nueva instancia."
    },
    {
        "concept": "ClickStream Analysis",
        "definition": "El análisis de la secuencia de clicks (recorrido) que realiza un determinado usuario en la web."
    },
    {
        "concept": "Clústeres",
        "definition": "Representan las agrupaciones naturales de las cosas en función de sus características."
    },
    {
        "concept": "Clustering",
        "definition": "Consiste en encontrar el agrupamiento natural de los ejemplos no etiquetados, de esta manera se crean clústeres o grupos a partir de los atributos de los datos. Cuando se reciba una instancia por proximidad a los clústeres se determina cuál pertenece."
    },
    {
        "concept": "Computación Afectiva",
        "definition": "Estudio y desarrollo de sistemas y dispositivos que pueden reconocer, interpretar, procesar y estimular las emociones humanas. Es un campo interdisciplinario que abarca la ciencia, la psicología y la ciencia cognitiva de la computación."
    },
    {
        "concept": "Computación evolutiva",
        "definition": "Es una rama de la Inteligencia Artificial que se basa en la teoría de síntesis evolutiva moderna. Integra tres conceptos básicos de la evolución biológica: la selección, la herencia y la variación. Estos tres conceptos dan lugar a un algoritmo que realiza un proceso de búsqueda."
    },
    {
        "concept": "Concepto",
        "definition": "Características o aspectos clave generados de una colección de documentos utilizando algún tipo de método. Comparándose con un término, podemos decir que es un mayor nivel de abstracción."
    },
    {
        "concept": "Corpus",
        "definition": "Es un conjunto lo mas extenso y ordenado de datos o textos científicos, literarios, etc., que se usan como fuente de datos para análisis o como base de una investigación. Un corpus puede ser una colección de documentos de texto, transcripciones de conversaciones, artículos de noticias, libros, sitios web o cualquier otra fuente de datos que contenga texto."
    },
    {
        "concept": "Cromosoma",
        "definition": "Conjunto de los valores de los parámetros que intentan dar solución al problema a resolver, cuyo diseño es específico de cada problema. Los valores de los parámetros que definen al individuo o solución se pueden representar de diversas formas."
    },
    {
        "concept": "Curva ROC",
        "definition": "El análisis de este tipo de curva constituye un método estadístico para determinar la exactitud diagnóstica de las pruebas, siendo utilizadas con tres propósitos específicos: determinar el punto de corte de una escala continua en el que se alcanza la sensibilidad y especificidad más alta, evaluar la capacidad discriminativa del test diagnóstico, es decir, su capacidad de diferenciar sujetos sanos versus enfermos."
    },
    {
        "concept": "Dashboard",
        "definition": "Presentación visual de datos críticos para que los ejecutivos los vean. Permite a los ejecutivos ver los puntos más relevantes y explorar la situación."
    },
    {
        "concept": "Data Fishing / Dredging",
        "definition": "Práctica de minería de datos creada en el año 1960 que consiste en la aplicación a ciegas de métodos de minería de datos que pueden conducir al descubrimiento de patrones no válidos y sin sentido."
    },
    {
        "concept": "Dato",
        "definition": "Información sobre algo concreto que permite su conocimiento exacto o sirve para deducir las consecuencias derivadas de un hecho"
    },
    {
        "concept": "Dato categórico",
        "definition": "Tipo de dato que representa etiquetas de varias clases utilizadas para dividir en grupos específicos."
    },
    {
        "concept": "Dato continuo",
        "definition": "Tipo de dato no categórico que representan los valores numéricos de variables específicas. Ejemplos de este tipo de datos son el salario bruto, el número de hijos o la temperatura en grados. Este tipo de dato implica que la variable contiene medidas en una escalada determinada; que permite la inserción de datos entre medias. Este tipo de datos, a su vez, se pueden clasificar como de intervalo o de ratio o razón."
    },
    {
        "concept": "Dato discreto",
        "definition": "Tipo de dato no numérico denominado así por representar un número finito de valores, sin valores continuos en medio. Este tipo de dato generalmente representa las etiquetas de varias clases, utilizadas para dividir una variable en grupos específicos. Ejemplos de este tipo de datos pueden ser las variables raza, sexo, o el color preferido."
    },
    {
        "concept": "Elitismo",
        "definition": "En el contexto de Algoritmos Genéticos, consiste en forzar la selección de las mejores soluciones para evolucionar a través de las generaciones."
    },
    {
        "concept": "Entropía",
        "definition": "Métrica que mide el grado de incertidumbre o aleatoriedad en un conjunto de datos. Si todos los datos de un subconjunto pertenecen a la misma clase, entonces no hay incertidumbre o aleatoriedad en ese conjunto de datos, y por lo tanto el valor de esta métrica es cero."
    },
    {
        "concept": "Evolución",
        "definition": "Serie de transformaciones continuas que va experimentando la naturaleza y los seres que la componen."
    },
    {
        "concept": "Experto",
        "definition": "Persona con alto nivel de habilidades que la capacitan para realizar juicios en su área."
    },
    {
        "concept": "Explosión de Datos",
        "definition": "Fenómeno referente al masivo y rápido crecimiento en el volumen y la disponibilidad de datos, tanto estructurados como no estructurados, generados a través de diversas fuentes digitales y tecnológicas."
    },
    {
        "concept": "Función de Activación F",
        "definition": "Una de las características más importantes de las redes neuronales que permite que, independientemente de la arquitectura que tenga, sea capaz de aprender relaciones no lineales entre los datos. Transforma la correspondencia lineal en no lineal. Las funciones más usadas son de tipo sigmoide, pero también se puede utilizar la función escalón. "
    },
    {
        "concept": "Función de adecuación/fitness",
        "definition": "Es un tipo de función que evalúa la calidad de una solución candidata en relación con los objetivos específicos de un problema."
    },
    {
        "concept": "Gen",
        "definition": "En el ámbito de los algoritmos evolutivos, se define como la unidad de información más pequeña dentro de un cromosoma. Esta unidad es sobre la que algunos operadores genéticos actúan; de modo que modifican el valor de dicha unidad o cortan un cromosoma justo por donde empieza o terminan."
    },
    {
        "concept": "GRAFO WEB",
        "definition": "Tipo de diagrama que está formado por nodos (Páginas web), y enlaces dirigidos de un nodo a otros (hiperenlaces que referencian una web)."
    },
    {
        "concept": "Herencia",
        "definition": "Proceso por el cual la descendencia de una célula u organismo adquiere o está predispuesta a adquirir las características de sus progenitores. Este concepto se aplica en computación evolutiva."
    },
    {
        "concept": "Heurística",
        "definition": "Conocimiento informal y juicioso de un área de aplicación que constituye las reglas del buen juicio en ese campo. También abarca el conocimiento de cómo resolver problemas de manera eficiente y eficaz, cómo planificar pasos para resolver un problema complejo, cómo mejorar el rendimiento, etc."
    },
    {
        "concept": "Hipervínculo",
        "definition": "Se trata de un enlace a un espacio electrónico, típicamente en la web, que puede hacer referencia a otras secciones dentro del propio espacio."
    },
    {
        "concept": "HUB",
        "definition": "Son consideradas así aquellas páginas web que enlazan a webs de la misma temática a su vez autoridades en esa particular temática."
    },
    {
        "concept": "Incertidumbre",
        "definition": "En los sistemas expertos, se trata de un valor que no se puede calcular con una consulta. Muchos sistemas expertos pueden adaptarse a este valor, permiten al usuario indicar si no sabe la respuesta."
    },
    {
        "concept": "Industria 4.0",
        "definition": "Término que se refiere a la integración de las nuevas tecnologías (IA, IoT, análisis de datos, etc.) y la digitalización en los procesos de fabricación y producción para conseguir una mayor flexibilidad e individualización en los procesos productivos."
    },
    {
        "concept": "Inferencia",
        "definition": "Proceso de deducción a partir del encadenamiento (hacia delante o hacia atrás) de reglas basadas en la información disponible con objetivo de generar conclusiones."
    },
    {
        "concept": "Inteligencia",
        "definition": "Un grado de razonamiento y comportamiento aprendido, generalmente orientado a tareas o resolución de problemas"
    },
    {
        "concept": "Inteligencia Artificial",
        "definition": "Tecngología que intenta imiter las capacidades del ser humano, típicamente: aprendiendo, llegando a sus propias conclusiones, aparentando comprender contenido complejo, participando en diálogos naturales con personas, reemplazando a los humanos en trabajos repetitivos, .... Ejemplo de esto son los filtros anti-spam, Siri, Google Maps, ..."
    },
    {
        "concept": "KDD",
        "definition": "Proceso no trivial que identifica patrones válidos, previamente desconocidos, potencialmente útiles y fundamentalmente entendibels en los datos. Se define también como un proceso de descubrimiento de conocimiento de bases de datos."
    },
    {
        "concept": "Metadata",
        "definition": "Datos sobre datos. En un alamcén de datos, los metadatos describen el contenido de un almacén de datos y su manera de uso"
    },
    {
        "concept": "Mineria de Datos",
        "definition": "Proceso de descubrimiento de conocimientos para generar nuevo conocimiento y soportar el proceso de toma de decisiones"
    },
    {
        "concept": "Minería de Opinión",
        "definition": "También conocido como análisis de sentimiento. Dentro del procesamiento de lenguaje natural, se trata de una técnica para captar el tono emocional que expresan un conjunto de palabras y detectar así opiniones o emociones."
    },
    {
        "concept": "Modelo",
        "definition": "Representación matemática que identifica los patrones entre los atributos de los objetos en un conjunto de datos dado"
    },
    {
        "concept": "Mutación",
        "definition": "Operador que realiza pequeñas modificaciones en el cromosoma. Esto permite prevenir la saturación de la población con cromosomas similares, pudiendo obtener soluciones inalcanzables que con el operador de sobrecruzamiento."
    },
    {
        "concept": "Neurona",
        "definition": "Unidad de proceso de una o varias entradas en una o varias salidas."
    },
    {
        "concept": "n-grama",
        "definition": "Compuesto de N palabras."
    },
    {
        "concept": "Nodo",
        "definition": "En un esquema o representación gráfica en forma de árbol, cada uno de los puntos de origen de las distintas ramificaciones. En el caso del Web Mining de Estructura, cada uno de estos elementos del grafo de web es una página web"
    },
    {
        "concept": "Normalizar",
        "definition": "Técnica que se aplica a un conjunto de datos para reducir su redundancia."
    },
    {
        "concept": "Operador genético",
        "definition": "En el ámbito de la computación evolutiva, son las acciones que permiten llevar a cabo el proceso de búsqueda. Estos operadores implementan saltos dentro del espacio de búsqueda; es decir, determinan los siguientes puntos a visitar en la búsqueda."
    },
    {
        "concept": "Ordinal",
        "definition": "Tipo de datos que contienen códigos asignables a objetos como etiquetas que representan un orden de rangos entre ellos."
    },
    {
        "concept": "overfitting",
        "definition": "Ocurre cuando un modelo de machine learning es demasiado complejo y se ajusta demasiado a los datos de entrenamiento, periendo su capacidad de generalizar a nuevos datos. ESto puede resultar en un mal rendimiento en datos que no formaron parte del entrenamiento."
    },
    {
        "concept": "PageRank",
        "definition": "Es una familia de algoritmos utilizados para asignar de forma numérica la relevancia de los documentos o páginas web, indexados por un motor de búsqueda en función de la importancia o relevancia de una determinada página web."
    },
    {
        "concept": "Patrón",
        "definition": "Relación matemática, numérica y/o simbólica entre los elementos de los datos."
    },
    {
        "concept": "Patrones predictivos",
        "definition": "Tipo de patron que predice el valor futuro de un atributo."
    },
    {
        "concept": "Población",
        "definition": "Conjunto de posibles soluciones o individuos que se someten a procesos de evolución y selección para resolver un problema o encontrar una solución óptima."
    },
    {
        "concept": "POS tagging",
        "definition": "También conocido como etiquetado gramatical, es el proceso de asignar o etiquetar a cada una de las palabras de un texto su categoría gramatical (sustantivo, verbo, adjetivo, etc.)."
    },
    {
        "concept": "Procesamiento del lenguaje natural",
        "definition": "Una sub-rama de la inteligencia artificial utilizada en computación lingüística. Su función es extraer información significativa de textos de lenguaje humano para que pueda posteriormente analizarse, por lo que son una herramienta muy útil en el contexto de Text Mining."
    },
    {
        "concept": "Random Forest",
        "definition": "Combinación de árboles de decisión donde cada uno depende de los valores de un vector aleatorio. Durante la predicción, el bosque combina las predicciones individuales para producir un resultado más preciso."
    },
    {
        "concept": "Realidad Mixta",
        "definition": "Se trata de una combinación de realidad virtual y realidad aumentada. Esta combinación permite crear nuevos espacios en los que interactúan tanto objetos reales como virtuales."
    },
    {
        "concept": "Red de Neuronas",
        "definition": "Método de la inteligencia artificial que enseña a las computadoras a procesar datos de una manera que está inspirada en la forma en que lo hace el cerebro humano"
    },
    {
        "concept": "Red Generativa Adversarial (GAN)",
        "definition": "Modelo de inteligencia artificial que consta de dos redes, un generador y un discriminador. El generador crea datos falsos, y el discriminador evalúa la autenticidad de los datos. Ambas redes se entrenan de manera adversarial hasta que el generador es capaz de generar datos que son indistinguibles de los datos reales para el discriminador."
    },
    {
        "concept": "Red Social",
        "definition": "Aplicación web con el objetivo de compartir experiencias personales con otras personas, ya sea mediante textos o archivos multimedia (imágenes, vídeos o audios). Estas pueden ser una fuente extensa de datos en procesos de data mining."
    },
    {
        "concept": "Reglas de Producción",
        "definition": "Declaraciones lógicas que describen el conocimiento y las pautas que el sistema experto utiliza para llegar a conclusiones o recomendaciones. Son secuencias del tipo SI (condición) ENTONCES (acción)."
    },
    {
        "concept": "Selección",
        "definition": "Operador que se aplica para elegir los cromosomas que se van a reproducir, con los que se generarán los próximos cromosomas. Para ello, seleccionará con mayor probabilidad aquellos cromosomas con un buen valor de adecuación."
    },
    {
        "concept": "Selección natural",
        "definition": "En el contexto de la computación evolutiva, se denomina así al proceso continuo de búsqueda de la solución óptima a partir de las mejores soluciones hasta el momento. Este proceso no se trata de desestimar estas otras soluciones que no son buenas, pero la probabilidad de realizar saltos a partir de esas soluciones no tan buenas debe ser menor. En la naturaleza encontramos también este tipo de proceso cuando se produce el crecimiento y reproducción de aquellos individuos mejor adaptados al entorno."
    },
    {
        "concept": "SEMMA",
        "definition": "Acrónimo de 'Sample, Explore, Modify, Model and Assess', el cual se refiere a un proceso alternativo para proyectos de minería de datos propuesto por el instituto SAS."
    },
    {
        "concept": "Sentimiento",
        "definition": "Positividad o negatividad, opinión o emoción apreciable en un fragmento de lenguaje que pueden ser detectadas por un algoritmo de Procesamiento del Lenguaje Natural."
    },
    {
        "concept": "Shell",
        "definition": "Componente de un sistema experto el cual contiene todos los elementos esenciales de dicho sistema, exceptuando el conocimiento específico del dominio."
    },
    {
        "concept": "Sinapsis",
        "definition": "Proceso de conexión entre neuronas que permite la transmisión de información entre ellas. En las redes de neuronas artificales, representan el aprendizaje de dicha red mediante la asignación de pesos."
    },
    {
        "concept": "Sistema Ciber-Físico",
        "definition": "Todo aquel dispositivo que integra capacidades de computación, almacenamiento y comunicación para controlar e interactuar con un proceso físico. Estos dispositivos están, normalmente, conectados entre sí y a su vez conectados con el mundo virtual y las redes digitales globales."
    },
    {
        "concept": "Sistemas Expertos",
        "definition": "Programas de ordenador que simulan el comportamiento característico de los expertos de un dominio en específico."
    },
    {
        "concept": "Sistemas Inteligentes",
        "definition": "Tipo de sistema que permite descubrir relaciones y encontrar patrones entre grandes cantidades de datos."
    },
    {
        "concept": "Sobrecruzamiento",
        "definition": "Operador de los algoritmos evolutivos que combina el material genético de dos individuos (padres) para generar nuevos individuos (hijos). A este operador también se le suele llamar recombinación."
    },
    {
        "concept": "Sobremuestreo",
        "definition": "Técnica que consiste en agregar más ejemplos de la clase minoritaria en un conjunto de datos desequilibrado para equilibrar las clases y mejorar el rendimiento de los modelos de aprendizaje automático en la detección de patrones y toma de decisiones."
    },
    {
        "concept": "Stemming",
        "definition": "Proceso de reducir una palabra a su raíz. Este proceso es utilizado en text mining. En español, equivale al concepto de derivación."
    },
    {
        "concept": "Stop Words",
        "definition": "Palabras que ya están previamente filtradas tanto antes como después del proceso de datos del lenguaje natural. No hay una lista universal de ellas, pero la mayoría están relacionadas con artículos, verbos auxiliares o palabras específicas del contexto que no tienen un valor útil."
    },
    {
        "concept": "Subsistema de explicación",
        "definition": "Parte de los sistemas expertos la cual muestra el razonamiento seguido por el sistema experto para llegar a un resultado."
    },
    {
        "concept": "Tecnologías Wearables",
        "definition": "Tecnologías que se llevan puestas como accesorios o ropa y están diseñados para interactuar con el usuario y recopilar información. Estos dispositivos suelen estar equipados con sensores, conectividad inalámbrica y capacidades de procesamiento de datos. Ejemplos: Smart ring, Smart Glasses, Smart Watch o Smart Belt."
    },
    {
        "concept": "Término",
        "definition": "Palabra o conjunto de palabras extraido directamente de un corpus por medios de procesado de lenguaje natural."
    },
    {
        "concept": "Test de Turing",
        "definition": "Test para evaluar la capacidad de una máquina para exhibir un comportamiento inteligente similar al de un ser humano o indistinguible de este."
    },
    {
        "concept": "Text Mining",
        "definition": "Proceso semi-automático de extracción de patrones de grandes fuentes de datos no estructuradas. Comprende las actividades de la recuperación de información de documentos o textos adecuados; la extracción de dicha información (búsqueda de datos claves y relaciones entre ellos); y el posterior análisis para extraer asociaciones entre los datos extraídos, mediante minería de datos o minería de web."
    },
    {
        "concept": "TF-IDF",
        "definition": "Una de las técnicas más comunes para medir cómo de relevante es un término en un documento de una colección. Se trata del producto entre dos métricas, la frecuencia con la que una palabra aparece en un determinado documento; y el inverso de lo común que es una palabra en toda la colección de documentos. Por lo tanto, las palabras que son frecuentes en un documento pero raras en toda la colección obtienen una alta puntuación, lo que sugiere que son términos importantes para ese documento en particular."
    },
    {
        "concept": "Token",
        "definition": "Bloque de texto categorizado en una sentencia, donde esta categoría está relacionada con la función que dicho bloque de texto representa."
    },
    {
        "concept": "Tokenizing",
        "definition": "Proceso de descomponer secuencias de texto, sean oraciones o documentos enteros, en unidades más pequeñas llamadas token (unidades únicas y significativas de texto, como pueden ser palabras)."
    },
    {
        "concept": "Topic tracking",
        "definition": "Tarea de text mining que consiste en poder predecir documentos de interés de un usuario basándose en los documentos que este ve."
    },
    {
        "concept": "Tracking Cookie",
        "definition": "Fichero de texto guardado en el navegador de un usuario para recoger datos sobre él en materia de búsqueda."
    },
    {
        "concept": "Validación Cruzada",
        "definition": "Tecnica utilizada en el aprendizaje automático y la estadística para evaluar el rendimiento de un modelo. Implica dividir los datos en un conjunto de entrenamiento, que se utiliza para entrenar el modelo, y un conjunto de pruebas, que se utiliza para evaluar su rendimiento. La validación cruzada k-fold es una de las variantes más comunes, implica dividir los datos en k subconjuntos. En ella el modelo se entrena y evalúa k veces, utilizando cada subconjunto como conjunto de pruebas en una iteración y los demás subconjuntos como conjunto de entrenamiento. Los resultados se promedian para obtener una medida general del rendimiento del modelo."
    },
    {
        "concept": "Valor umbral",
        "definition": "Cantidad más reducida de una señal que tiene que existir para que sea advertida por un sistema."
    },
    {
        "concept": "Vector de Pesos",
        "definition": "Conjunto de valores numéricos asociados a una capa de una Red de Neuronas. Se emplea para determinar los valores de salida de las neuronas y por ende, el comportamiento de la red. Este conjunto de valores es ajustado durante el entrenamiento de la RNA."
    },
    {
        "concept": "Vector de términos",
        "definition": "Array de términos extraídos del corpus; que contiene cuantas veces aparace cada uno."
    },
    {
        "concept": "Web Crawler",
        "definition": "Mecanismo del navegador que se desplaza por Internet a través de los hipervínculos que aparecen en los sitios web existentes con el fin de evaluar palabras clave, hashtags; indexar el contenido y los URL de cada sitio web; copiar páginas web y abrir todos o solo algunos de los URL que encuentran para analizar nuevos sitios web."
    },
    {
        "concept": "Web Mining",
        "definition": "Proceso de descubrir relaciones intrínsecas de los datos web, los cuáles son expresados en forma de texto, enlaces o uso de la información."
    },
    {
        "concept": "Web Mining de Contenido",
        "definition": "Proceso de extracción de información útil del contenido de páginas web, tanto texto, imágenes, vídeo, audio, listas o tablas. En este campo podemos encontrar técnicas como son la Recuperación de Información (IR) o el Procesado de Lenguaje Natural (NLP)."
    },
    {
        "concept": "Web Mining de Estructura",
        "definition": "Estudio de las relaciones entre páginas web a través de los enlaces. Se dedica a analizar cómo está interconectada la red de páginas web de tal manera que estas se entienden como nodos y a su vez los enlaces se entienden como nexos de un nodo a otro, como si de un grafo se tratara. Gracias a esta estructura de grafo, pueden aplicarse algoritmos como Dijkstra para hallar el camino más rápido de una web a otra."
    },
    {
        "concept": "Web Mining de Utilización",
        "definition": "Estudio de técnicas que pueden predecir el comportamiento del usuario cuando éste interacciona con la web."
    },
    {
        "concept": "World Wide Web",
        "definition": "Gigantesco repositorio de datos donde hay información sobre cualquier tema. Podría considerarse como el repositorio de datos y texto más grande del mundo y además crece en grandes dimensiones cada día."
    }
]

COLORS = {
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[1;34m",
    "purple": "\033[1;35m",
    "cyan": "\033[1;36m",
    "white": "\033[1;37m",
    "reset": "\033[0;0m"
}


def main():

    while True:
        clear_terminal()
        print(
            f"{COLORS['purple']}==========| MODO DE JUEGO |=========={COLORS['reset']}")
        print("Seleccione el modo de juego: ")
        print("1. Definición")
        print("2. Adivinanza")
        print("3. Salir")
        option = input("\nOpcion: ")
        if (option == "1"):
            definition_mode(DICTIONARY)
        elif (option == "2"):
            guess_mode(DICTIONARY)
        elif (option == "3"):
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
            getpass.getpass("Pulsa ENTER para continuar.");


def definition_mode(dictionary):
    remaining_words = dictionary.copy()
    while True:
        clear_terminal()
        print(
            f"{COLORS['purple']}==========| MODO DEFINICIÓN |=========={COLORS['reset']}");

        if (len(remaining_words) == 0):
            print("Ya se han mostrado todas las palabras");
            break;

        word = remaining_words.pop(random.randrange(len(remaining_words)));
        print("CONCEPTO:    ", word["concept"]);
        print("DEFINICION:  ", word["definition"]);

        if get_exit():
            break;


def guess_mode(dictionary):
    remaining_words = dictionary.copy()
    total_dictionary_lenght = len(dictionary);
    status_vector = []
    wrong_words = []
    for i in range(total_dictionary_lenght):
        status_vector.append("clear")
    status_index = 0

    while True:
        clear_terminal();
        print(
            f"{COLORS['purple']}==========| MODO ADIVINANZA |=========={COLORS['reset']}");

        print_progress(status_vector, status_index, total_dictionary_lenght);

        if (len(remaining_words) == 0):
            print("Ya se han mostrado todas las palabras");
            break;

        word = remaining_words.pop(random.randrange(len(remaining_words)));
        print("DEFINICION:  ", word["definition"]);
        print("CONCEPTO:     ");
        word_concept = strip_accents(word['concept']).lower();

        while True:
            wordSchema = get_schema(word["concept"]);
            guessedWord = strip_accents(input(wordSchema).lower());
            if (len(guessedWord) == len(word_concept)):
                break;
            # Go one line up and remove the line
            sys.stdout.write("\033[F");
            sys.stdout.write("\033[K");
            sys.stdout.flush()

        if (guessedWord == word_concept):
            print(f"{COLORS['green']}¡Correcto!{COLORS['reset']}");
            status_vector[status_index] = "correct";
        else:
            print(
                f"{COLORS['red']}Incorrecto{COLORS['reset']} - La palabra era: ", word["concept"]);
            status_vector[status_index] = "incorrect";
            wrong_words.append(word);

        status_index += 1;

        if get_exit():
            break;

    print("\nPalabras falladas:")
    for word in wrong_words:
        print("\nCONCEPTO: ", word["concept"]);
        print("DEFINICIÓN: ", word["definition"]);

    get_exit();


def print_progress(status_vector, status_index, total_lenght):
    print("Progreso: ", end="");
    for status in status_vector:
        if status == "clear":
            print("■", end="");
        elif status == "correct":
            print(f"{COLORS['green']}■{COLORS['reset']}", end="");
        elif status == "incorrect":
            print(f"{COLORS['red']}■{COLORS['reset']}", end="");
    print(f" {status_index}/{total_lenght}\n");

def get_schema(word):
    schema = "";
    for letter in word:
        if letter in ["/", "-", "_", " ", "(", ")"]:
            schema += letter;
        else:
            schema += "#";
    schema+= "\r"
    return schema;

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_exit():
    text = input("\nPresiona ENTER para continuar o 'exit' para salir del modo\n");
    if text == "exit":
        return True;
    else:
        return False;

if __name__ == "__main__":
    main()
