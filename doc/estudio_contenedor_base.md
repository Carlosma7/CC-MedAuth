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
