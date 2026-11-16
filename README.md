# SportsReserve - BACKEND API

## Descripción

SportsReserve Back-End es la API REST desarrollada en Django y Django REST Framework para la gestión de datos del sistema de reserva de canchas deportivas. La aplicación permite administrar el catálogo de canchas, el registro de clientes y el control de reservas en tiempo real, aplicando reglas de negocio para evitar reservas duplicadas en un mismo horario.

## Funcionalidades Principales

* Gestión completa (CRUD) de canchas (nombre, deporte, superficie, capacidad, precio por hora e imagen).
* Registro de clientes (nombre, correo electrónico y teléfono).
* Control y validación de reservas asociadas a clientes y canchas mediante disponibilidad por fecha y hora.
* Borrado en cascada (CASCADE) para mantener la estructura al eliminar clientes o canchas vinculadas.

## Tecnologías Utilizadas

* Python 3.12
* Django
* Django REST Framework
* SQLite3

## Instrucciones de Ejecución

1. Clonar el repositorio: git clone https://github.com/Benjamin-Fincheira/reserva-canchas-backend.git
2. Acceder al directorio del proyecto: cd reserva-canchas-backend/backend
3. Crear y activar el entorno virtual: python -m venv venv y .\\venv\\Scripts\\Activate.ps1
4. Instalar las dependencias necesarias: pip install django djangorestframework
5. Aplicar las migraciones a la base de datos: python manage.py makemigrations canchas y python manage.py migrate
6. Iniciar el servidor de desarrollo local: python manage.py runserver

## Endpoints de la API

### Canchas (/api/canchas/)

* GET /api/canchas/ - Obtener el listado de canchas disponibles.
* POST /api/canchas/ - Registrar una nueva cancha.
* GET /api/canchas/{id}/ - Consultar el detalle de una cancha específica.
* PUT /api/canchas/{id}/ - Actualizar la información de una cancha.
* DELETE /api/canchas/{id}/ - Eliminar una cancha del catálogo.

### Clientes (/api/clientes/)

* GET /api/clientes/ - Obtener el listado de clientes registrados.
* POST /api/clientes/ - Registrar un nuevo cliente.
* GET /api/clientes/{id}/ - Consultar los datos de un cliente.
* PUT /api/clientes/{id}/ - Actualizar los datos de un cliente.
* DELETE /api/clientes/{id}/ - Eliminar un cliente registrado.

### Reservas (/api/reservas/)

* GET /api/reservas/ - Obtener el historial completo de reservas.
* POST /api/reservas/ - Crear una nueva reserva (valida disponibilidad de fecha y hora).
* GET /api/reservas/{id}/ - Consultar el detalle de una reserva.
* DELETE /api/reservas/{id}/ - Cancelar o eliminar una reserva.

## Evidencia de Pruebas de Funcionamiento

Las pruebas de la API se ejecutaron exitosamente utilizando Postman, verificando las respuestas y códigos de estado HTTP requeridos:

* GET /api/canchas/ - Respuesta 200 OK (Consulta inicial con lista vacía y luego lista de canchas ya creadas).
* POST /api/canchas/ - Respuesta 201 Created (Registro exitoso de Cancha Futbol 7 Techada).
* POST /api/clientes/ - Respuesta 201 Created (Registro exitoso de cliente).
* POST /api/reservas/ - Respuesta 201 Created (Creación exitosa de reserva inicial).
* POST /api/reservas/ - Respuesta 400 Bad Request (Validación correcta al intentar duplicar cancha, fecha y hora).
* DELETE /api/clientes/{id}/ - Respuesta 204 No Content (Eliminación exitosa del cliente).
* GET /api/reservas/ - Respuesta 200 OK (Verificación de eliminación en cascada de las reservas asociadas).