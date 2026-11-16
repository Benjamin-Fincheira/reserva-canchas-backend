# Declaración de Uso de Inteligencia Artificial (USO_IA.md)

## Declaración de Herramientas Utilizadas

Durante el desarrollo del back-end de SportsReserve se utilizaron las herramientas de inteligencia artificial Gemini y Gemini Notebook como asistente de desarrollo.

## Porcentaje Estimado de Participación de IA por Archivo

| Archivo                                | Uso Estimado de IA | Descripción de la Participación                                                                         |
| -------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| backend/settings.py                    | 35%                | Integración de las aplicaciones rest_framework y canchas en INSTALLED_APPS.                             |
| backend/wsgi.py                        | 70%                | Configuración del conector WSGI para solucionar errores de importación al iniciar el servidor.          |
| canchas/models.py                      | 20%                | Apoyo en la definición de modelos, claves foráneas y relaciones en cascada (on_delete=models.CASCADE).  |
| canchas/serializers.py                 | 50%                | Asesoría en la lógica de validación para evitar reservas duplicadas en el mismo horario.                |
| canchas/views.py                       | 30%                | Configuración de los controladores ModelViewSet para exponer las operaciones CRUD.                      |
| canchas/urls.py                        | 20%                | Enrutamiento dinámico mediante DefaultRouter para la generación de endpoints.                           |
| Documentación (README.md / USO_IA.md)  | 0%                 | Se utilizó como apoyo el readme del front-end                                                           |

