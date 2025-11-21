# Respuestas sobre el parcial:
-Parte 1 - Estrategia: 

1. Diferencia entre CI y CD:

La CI (integración continua) es la práctica de integrar cambios de código en un repositorio múltiples veces al día. La CD tiene dos significados: la entrega continua automatiza las integraciones de código, mientras que la implementación continua entrega automáticamente las versiones finales a los usuarios finales.

2. Lenguaje y Herramientas:

El lengua usado fue python(3.11) junto a ruff para el linter, tambien de cobertura se usaron coverage.py y pytest-cov, escogi este lengua y herramientas por que son muy buenas y rapidas sobretodo por que python tiene una gran cantidad de documentacion y workflow estables

3. Definicion y justificacion de un umbal de 85%:

Creo que este procentaje es uno muy optimo y equilibrado por que 70% es un porcentaje relativamente bajo y 90% y superior puede que implique hacer pruebas especificas 

-Parte 4 Validacion y logs:

1. Como identificar fallas de linter, pruebas y logs

Los errores con ruff se verifican con el comando de ruff check ., los de pytest salen con stacktrace y la cobertura falla con un porcentaje menor a 85%

2. Como generar un run fallido y uno exitoso:

<img width="1358" height="616" alt="image" src="https://github.com/user-attachments/assets/a476f613-dc5d-4622-8b4f-c0f61e032559" />

-Parte 5 - IA y Etica:

1. Dos metodos comunes de deteccion de Ia son los Detectores estadísticos (GPTZero, ZeroGPT, OpenAI Text Classifier) y el otro es el analisis de patrones de Github copilot(marcas invisibles en el código, estilo muy uniforme)

2. Explicar por qué no es posible asegurar al 100% la autoría:

3. Propuestas de politicas razonables del uso de la IA:

Primero el uso de la IA como ayuda o soporte para aprender y entender conceptos y errores desconocidos
