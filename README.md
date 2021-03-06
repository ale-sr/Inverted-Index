# BASE DE DATOS 

## Profesor 馃

- Heider Sanchez Enriquez

## Introducci贸n :dart:

**_Objetivo:_**  Entender y aplicar los algoritmos de b煤squeda y recuperaci贸n de informaci贸n basado en el contenido. En este proyecto nos enfocaremos en la construcci贸n 贸ptima de un _脥ndice Invertido_. En este caso usaremos un dataset de tweets, que nos permitir谩 encontrar los tweets m谩s relevantes dado un t茅rmino de b煤squeda. 

**_Descripci贸n del dominio:_** Usaremos una colecci贸n  de  aproximadamente [20 mil  tweets  de  Twitter](https://onedrive.live.com/?cid=0c2923df9f1f816f&id=C2923DF9F1F816F%2150804&ithint=folder&authkey=!ANNEKv7tNdlSSQk). En donde el diccionario de t茅rminos se construy贸 usando el contenido del atributo 鈥渢ext鈥?, y el el Id del tweet.  Existen m谩s de 10 mil registros y por cada uno tenemos la siguiente informaci贸n:

- **Id**: N煤mero de identificaci贸n del id.
- **Date**:  Fecha de de publicaci贸n del tweet.
- **Text**: Contenido del tweet.
- **User_id**: Id del usuario que escribi贸 el tweet.
- **User_name**: Nombre de usuario de la persona que tweeteo.
- **Location**: Desde donde fue enviado el tweet.
- **Retweeted** : Valor booleano para para identificar si fue retweeteado o no.
- **RT_text**: Contenido del retweet.
- **RT_user_id**: Id del usuario que retweete贸 el tweet.
- **RT_user_name** : Nombre de usuario de la persona que retweete贸.

- **Ejemplo**:

````json
{"id": 1026814183042686976,"date": "Tue Aug 07 12:55:53 +0000 2018", "text": "RT @de_patty: Asuuuuuuu..  @Renzo_Reggiardo me da mala espina...su pasado fujimor铆sta qu茅 miedo!!!y @luchocastanedap hijo de corrupto que s鈥?", "user_id": 544008122,"user_name": "@CARLOSPUEMAPE1", "location": {}, "retweeted": true,"RT_text": "Asuuuuuuu..  @Renzo_Reggiardo me da mala espina...su pasado fujimor铆sta qu茅 miedo!!!y @luchocastanedap hijo de corrupto que secunda lo del padre NI HABLAR! M谩s comunicore Plop!lideran las preferencias para la alcald铆a de Lima, seg煤n Ipsos | RPP Noticias https://t.co/w5TnU0Dmwq", "RT_user_id": 302995560, "RT_user_name": "@de_patty"}
 
````

**_Resultados esperados:_** 
Probar  el  desempe帽o  del  铆ndice  invertido,  mediante una plataforma web (frontend y backend)  que permita interactuar con las principales operaciones del 铆ndice invertido:  
- Carga e indexaci贸n de documentos en tiempo real. 
- B煤squeda textual relacionado a ciertos temas de inter茅s. 
- Presentaci贸n de resultados de b煤squeda de forma amigable e intuitiva.  

## Comenzando 馃殌

### Pre-requisitos 馃搵
* [Python](https://www.python.org/downloads/) 
#### Librer铆as
* [Json](https://docs.python.org/3/library/json.html)
* [flask](https://flask.palletsprojects.com/en/2.0.x/)
* [nltk](https://www.nltk.org/)
* [collections](https://docs.python.org/3/library/collections.html)
* [emoji](https://pypi.org/project/emoji/)
* [math](https://docs.python.org/3/library/math.html)
* [re](https://docs.python.org/3/library/re.html)


### Despliegue 馃摝

**1.** Clonar el repositorio del proyecto.

**2.** Realizar el Build del proyecto en su IDE de preferencia.

**3.** Ejecutar el programa


## Descripci贸n de las t茅cnicas 

- **Preprocesamiento:** 
  - Tokenization 
  - Filtrar Stopwords 
  - Reducci贸n de palabras (Stemming) 
- **Construcci贸n del 脥ndice**
  - Estructurar el 铆ndice invertido para guardar los pesos TF-IDF.  
  - Calcular  una  sola  vez  la  longitud  de  cada  documento  (norma)  y  guardarlo  para  ser 
  utilizado al momento de aplicar la similitud de coseno. 
  - Construcci贸n del 铆ndice en memoria secundaria para grandes colecciones de datos.   
- **Consulta** 
  - La consulta es una frase en lenguaje natural.  
  - El scoring se obtiene aplicando la similitud de coseno sobre el 铆ndice invertido en 
  memoria secundaria. 
  - La funci贸n de recuperac
  i贸n debe retornar una lista ordenada de documentos que se 
  aproximen a la consulta. 


###  脥NDICE INVERTIDO  馃挴

**_脥ndice Invertido_**: En este m茅todo organizamos los registros de acuerdo a un valor de sus campos, para este caso usaremos el campo **Id** como key.

- **Construcci贸n del 铆ndice invertido:**

  1.  Recorremos los archivos con la data y los leemos como diccionarios.
  2.  Para cada tweet sacamos las palabras y las llevamos a su forma ra铆z, pero antes se eliminan los signos de puntuaci贸n y emojis. Despu茅s, devolvemos una lista que contiene a cada palabra con el n煤mero de veces que aparece(tf-term frequency).
  3.  Posteriormente, calculamos el score tfidf para cada palabra, 
  4.  Finalmente escribimos un 铆ndice invertido en memoria secundaria cada 5 documentos. 
  ```
  def json_tweets_to_dic():
    tf = []
    for filename in archivos:
        lista = []
        if filename.endswith(".json") :
            with open(input_directory + '\\' + filename, 'r', encoding='utf-8') as all_tweets:
                all_tweets_dictionary = json.load(all_tweets)
                for tweet in all_tweets_dictionary:
                    temp = readFile(all_tweets_dictionary[tweet])
                    lista.append(temp)
                tf.append(merge(lista))
    tfidf(tf)
    ```
- **Manejo de memoria secundaria**
  1. Para leer los archivos con tweets, necesitamos leer todos los documentos que los contengan.
  2. Al haber gran cantidad de informaci贸n necesitamos almacenar esta en distintos bloques por lo que escribimos un 铆ndice invertido para 5 documentos como m谩ximo.
  3. Al momento de buscar, necesitamos leer la infomraci贸n que tenemos en los 铆ndices por lo que toca ir a帽adiendolos a memoria principal.
  ```
  def tfidf(tf):
    lista = {}
    it = 0
    for i in tf:
        for k in i:
            wtfidf = math.log(1 + i[k]) * math.log(len(tf)/df(k, tf))
            if k in lista:
                lista[k] = str(lista[k]) + ";" + str(archivos[it]) + "," + str(wtfidf)             
            else:
                lista[k] = str(archivos[it]) + "," + str(wtfidf)
        it += 1            
        if(it % 5 == 0):
            writeblock(lista, it/5)
            lista = {}
    
    writeblock(lista, math.ceil(it/5))

  def writeblock(lista, c):
    nombre = "index" + str(int(c)) + ".txt"
    with open(nombre, 'a', encoding='utf-8') as data:
        for k in lista:
            data.write(k + ':'+ lista[k] + '\n')
    ```
  
- **Consultas**
  1. Para realizar una consulta lo primero que hacemos es tokenizar la query.
  2. Calculamos los scores para cada palabra.
  3. Despu茅s de procesar la query, vamos sacando la similitud de coseno entre esta y la informaci贸n que vamos leyendo de los 铆ndices invertidos guardados en memoria secundaria.
  4. Ordenamos los resultados de acuerdo al score obtenido por cada documento.
  5. Devolvemos los k resultados m谩s relevantes a la consulta.
  ```
  def search(query, k):
    tf = readFile(query)
    dic = {}
    inverted = readInverted()
    scores = {}
    lenght1 = {}
    for i in archivos:
        scores[i] = 0
        lenght1[i] = 0
    lenght2 = 0
    for i in tf:
        wtfidf = math.log(1 + tf[i]) * math.log(len(archivos)/df_ind(i, inverted))
        dic[i] = wtfidf
        lenght2 = lenght2 + wtfidf**2
        values = inverted[i].split(';')
        for j in values:
            j = j.split(',')
            lenght1[j[0]] = lenght1[j[0]] + float(j[1])**2
            scores[j[0]] = scores[j[0]] + float(j[1])*wtfidf
    lenght2 = lenght2**0.5
    for i in lenght1:
        if lenght1[i] != 0:
            lenght1[i] = lenght1[i]**0.5
    for i in scores:
        if lenght1[i] != 0:
            scores[i] = scores[i]/(lenght1[i]*lenght2)
    orderedDic = sorted(scores.items(), key=lambda it: it[1], reverse=True)
    return orderedDic[:k]
    ```

###  Vistas de plataforma web 
**Buscador**
<figure class="image" align="center">
  <img src="images/buscador .png" width="70%" height="60%" style="text-align:center;">
</figure>

**Resultados**
<figure class="image" align="center">
  <img src="images/resultados.png" width="70%" height="60%" style="text-align:center;">
</figure>

## Evidencias 馃殌

* [Video](https://drive.google.com/drive/folders/120QQzzBZWRGeH2MJdfYNc15avekUYLPz?usp=sharing) 

## Licencia 馃搫
Universidad de Ingenieria y Tecnolog铆a - UTEC
  
