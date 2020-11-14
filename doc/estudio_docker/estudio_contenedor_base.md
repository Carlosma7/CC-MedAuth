## Estudio sobre contenedores base de Docker Hub

---

En este estudio se pretende comprender cada uno de los motivos por los que se ha elegido el contenedor base para desarrollar el proyecto. Para ello inicialmente se han tenido en cuenta las dos opciones disponibles: el contenedor base "oficial" del lenguaje (*Python* en este caso) y los contenedores base oficiales de los principales sistemas operativos, siendo estos *Ubuntu*, *Alpine*, *CentOS*, *Debian* y *Fedora*.

### 1. Definir requisitos

Lo primero es definir aquellos requisitos a evaluar, que definan nuestro interés hacia un determinado contenedor base, para ello se tendrán en cuenta las principales versiones dentro de cada opción a valorar, se analizaran y se escogeran las más adecuadas.

Los requisitos principales a tener en cuenta son:
1. **Tamaño del contenedor base**: Importante ya que queremos optimizar nuestro contenedor, pero no es el único factor en el que fijarse, ya que existen otros factores que determinan la validez para nuestro proyecto. Si únicamente nos centraramos en el tamaño, lo más lógico sería escoger un contenedor base de *Alpine*, pero no es la intención.
2. **Librería [Libc6](https://packages.debian.org/stretch/libc6)**: Contiene las bibliotecas estándar de C y otras librerías estándar necesarias para muchas de las funcionalidades que necesita *Python3*. Puede instalarse perfectamente juntamente a sus dependencias, pero un contenedor base que lo tenga instalado por defecto será considerado de manera más positiva.
3. **Python3.8**: En nuestro proyecto necesitaremos la instalación de Python con versión 3.6+, por lo que obtener dicha instalación por defecto en el contenedor será un factor que se considerará positivo. Un exceso de bibliotecas instaladas que no se van a utilizar se considerará un factor negativo.
4. **Pip3**: Al trabajar con *Python3*, se necesita la gestión e instalación de paquetes *Pip* con la última versión del mismo, por lo que será necesaria su instalación.
5. **LTS**: Sería una solución ilógica desarrollar un proyecto en un sistema obsoleto o que dejará de tener soporte en breves, por lo que se tendrá en cuenta su fecha de finalización de soporte.

También se valorarán por otra parte, características como actualizaciones de seguridad, compatibilidad de bibliotecas, estabilidad y uso excesivo de bibliotecas, ya que queremos un sistema robusto y optimizado.

Además de los principales requisitos descritos, tras hacer una preselección, se seleccionarán aquellas opciones que se consideran mejores para evaluarlas con una instalación completa. Se analizarán en ese momento variables de entorno, usuarios y paquetes, entre otros aspectos.

### 2. Análisis opciones

A continuación se procede a analizar cada una de las opciones en base a los requisitos explicados anteriormente, para ello, se ha utilizado también la herramienta [container-diff](https://github.com/GoogleContainerTools/container-diff).

##### Ubuntu

Uno de los principales sistemas operativos, y uno de los más utilizados a la hora de diseñar un contenedor orientado a un desarrollo en *Python*

| Release | Size   | Libc6 | Python3.8      | Pip3 | LTS  | Comentarios                                                                       |
|---------|--------|-------|----------------|------|------|-----------------------------------------------------------------------------------|
| focal   | 72.9M  | Sí    | No             | No   | TBA  | Versión latest.                                                                   |
| bionic  | 62.4M  | Sí    | No             | No   | 2028 | Más usada en la actualidad. Más ligera con funcionalidad plena.                   |
| xenial  | 83.8M  | Sí    | No             | No   | 2024 | Existen opciones mejores y actualizadas.                                          |
| trusty  | 191.1M | Sí    | No, tiene 3.4  | No   | 2022 | Peor opción. Habría que desinstalar la versión de Python antigua e instalar nueva.|

Tras observar la tabla, podemos observar las diferentes opciones existentes para un contenedor base en *Ubuntu*, queda claro que las mejores opciones son las versiones *focal* y *bionic*, pero entrando en detalle, comparamos dichas versiones (la comparativa con la herramienta *container-diff* se puede ver [aquí]()).

Tras observar, la única diferencia entre ambos sistemas, es la instalación y actualización de determinados paquetes. Si observamos los paquetes existentes en *focal*, podemos observar que son nuevas versiones de los paquetes de *bionic* o paquetes que no afectan al desempeño en nuestro proyecto.

Por otro lado, podemos observar que las versiones de *Libc6* son, respectivamente, *2.31-0ubuntu9.1* y *2.27-3ubuntu1.2*, las cuales soportan nuestra versión deseada de *Python* y poseen un tamaño similar.

Teniendo en cuenta todos estos factores, nos quedaremos como candidato para instalación de *Ubuntu* con **bionic**.

##### Alpine

Uno de los sistemas operativos más ligeros, del que destaca su enorme multitud de versiones, ya que anualmente se lanza una nueva versión del mismo, que será un factor a tener en cuenta de cara al futuro del proyecto.

| Release | Size | Libc6 | Python3.8 | Pip3 | LTS  | Comentarios                         |
|---------|-------|-------|----------|------|------|-------------------------------------|
| edge    | 5.4M  | No    | No       | No   | n/a  | Versión en desarrollo. Inestable.   |
| 3.12    | 5.3M  | No    | No       | No   | 2022 | Última versión estable.             |
| 3.11    | 5.4M  | No    | No       | No   | 2021 |                                     |
| 3.10    | 5.3M  | No    | No       | No   | 2021 |                                     |
| 3.9     | 5.3M  | No    | No       | No   | 2020 | Dejará de estar soportada este año. |

Tras evaluar las distintas opciones, y observar que apenas existen diferencias de cara a nuestro proyecto que sean relevantes, lo lógico sería pensar que es una excelente opción debido a su ligero tamaño y a que carece de bibliotecas instaladas por defecto, pero sin ir más lejos puede tratarse de una de las peores opciones si investigamos un poco.

Alpine no cabe duda que sería la mejor opción tratándose de un desarrollo sencillo y ligero en *Python*, pero si requerimos de algunas dependencias, esto puede ocasionar problemas debido a que *Alpine* no soporta los *wheels* estándar de Linux. *Alpine*, a diferencia de la mayoría de las distribuciones de Linux, utiliza *musl* en lugar de la versión estándar de la librería *glibc*. Por este motivo requeriríamos de compatibilizar *Alpine* con los *wheels* de *PyPI*.

Esta operación es realizable, pero nuevamente encontramos un problema, además de elevar considerablemente el tamaño del contenedor, la construcción del mismo es excesivamente lenta, tal y como se muestra en este [ejemplo](https://pythonspeed.com/articles/alpine-docker-python/) encontrado en [Pythonspeed](https://pythonspeed.com/), la construcción en comparación con una versión de *Ubuntu* es excesivamente lenta.

Cabría destacar como dato interesante que *Alpine* piensa incorporar en su versión *edge* algunas de las librerías más comunes, para poder realizar construcciones más rápidas, pero esto tampoco solucionaría el problema, ya que con el planteamiento de *Alpine* de ser un sistema ligero, no tendría sentido instalar todas las dependencias de *PyPI*.

Por estos motivos se descartan todas las opciones de *Alpine* de cara a ser considerado como contenedor base del contenedor del proyecto.

##### CentOS

*CentOS* es una distribución de **GNU/Linux Red Hat Enterprise Linux RHEL**. Es un sistema estable, de calidad y sobre todo *open source*. Inicialmente se destaca que es un sistema robusto, que utiliza sistema *rpm* y que posee por norma general un tamaño quizás elevado en comparación con otros sistemas operativos.

| Release | Size   | Libc6 | Python3.8                    | Pip3 | LTS  | Comentarios                                                               |
|---------|--------|-------|------------------------------|------|------|---------------------------------------------------------------------------|
| centos8 | 205.1M | No    | No, pero librerías de 3.6 sí | No   | 2029 | Versión latest.                                                           |
| centos7 | 201.3M | No    | No, Python 2.7               | No   | 2024 | Sería necesario desinstalar la versión de Python2.7 e instalar Python3.8. |
| centos6 | 197.5M | No    | No, Python 2.6               | No   | 2020 | Dejará de estar soportada este año.                                       |

Como se indicaba antes de realizar la tabla, las versiones de *CentOS* son considerablemente pesadas en comparación las versiones de otras opciones contempladas, además, cabe destacar que la última versión es la única que no posee alguna version de *Python* antigua, aunque sí posee bibliotecas relativas a *Python3.6*.

*CentOS* sería una opción considerable debido a la comodidad que supondría realizar la construcción de nuestro contenedor, lo sencillo que es su manejo y la enorme comunidad que posee detrás. Sin embargo, existen opciones considerablemente mejores, por lo que realizar una comparativa en la que se tenga en cuenta *CentOS* carece realmente de sentido.
