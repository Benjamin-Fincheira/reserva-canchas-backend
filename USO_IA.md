# Declaración de Uso de Inteligencia Artificial (USO_IA.md)

## Declaración de Herramientas Utilizadas

Durante el desarrollo del back-end de SportsReserve se utilizaron las herramientas de inteligencia artificial Gemini y Gemini Notebook como asistente de desarrollo.

## Porcentaje Estimado de Participación de IA por Archivo

| Archivo                                | Uso Estimado de IA | Descripción de la Participación                                                                         |
| -------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| backend/settings.py                    | 35%                | Ajustes generales del proyecto en INSTALLED_APPS, middleware y vinculación con wsgi.py.                 |
| backend/wsgi.py                        | 60%                | Configuración del conector WSGI para solucionar errores de importación al iniciar el servidor.          |
| canchas/models.py                      | 10%                | Apoyo en las relaciones en cascada. Se usaron las mismas variables que en Front-end                     |
| canchas/serializers.py                 | 15%                | Ayuda en la lógica de validación para evitar reservas duplicadas en el mismo horario.                   |
| canchas/views.py                       | 10%                | Información y apoyo sobren los controladores ModelViewSet para las operaciones CRUD.                    |
| canchas/urls.py                        | 15%                | Enrutamiento dinámico mediante DefaultRouter .                                                          |
| Documentación (README.md / USO_IA.md)  | 5%                 | Estrucuta de esta tabla en USO_IA.md                                                                    |

## Respuestas Reflexivas

### 1. ¿En qué aspectos del proyecto utilizaron inteligencia artificial?

La IA se utilizó principalmente en la configuracion de Django y corrección de errores de configuracióny  en la comprensión de procesos como el de serialización con Django REST Framework.

### 2. ¿Qué partes del código fueron desarrolladas principalmente por ustedes?

El diseño y modelado de datos en models.py (Cancha, Cliente, Reserva y cada variable), la ejecución de comandos de en consola (makemigrations, migrate, runserver) y la prueba manual completa con la API mediante Postman.

### 3. ¿Qué errores o problemas encontraron en las respuestas generadas por IA?

Generaba respuestas incorrectas en posibles soluciones frente a errores pues tomaba otra version de python o de Django y antes de comprobar eso arrojaba 100 posibles respuestas que no solucionaban el problema, solo lo hacian más grande.

### 4. ¿Cómo verificaron que el código sugerido funcionaba correctamente?

La verificación se realizó ejecutando las migraciones en el entorno local y realizando peticiones HTTP a la API a través de Postman, validando que cada operación devolviera los códigos de estado correspondientes (Ej:200 OK).

### 5. ¿Qué conocimientos adquirieron durante el desarrollo?

Se adquirieron conocimientos en la construcción de API REST con Django REST Framework, serialización de datos, manejo de relaciones en clases o variables con borrado en cascada, gestión de migraciones en SQLite y pruebas de integración con clientes HTTP.