# Parcial-Calidad-de-Software - Investigacion sobre nektos/act
-Que es y Que hace?:

Act es una herramienta que ejecuta tus Github actions localmente usando Docker,
lee en tus acciones de Github y determina el conjunto de acciones que hay que ejecutar. Utiliza la API de Docker para extraer o construir las imágenes necesarias, tal como se definen en tus archivos de flujo de trabajo, y finalmente determina la ruta de ejecución en función de las dependencias definidas. 

-Requisitos

Act depende (exactamente de la API de Docker Engine) para ejecutar flujos de trabajo en contenedores.

-Comando para ejecutar el workflow de manera local

por defecto es : 
act -W '.github/workflows/'

ruta mas especifica es : 
act -W '.github/workflows/checks.yml'
