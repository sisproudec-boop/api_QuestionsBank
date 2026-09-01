# API QuestionsBank

API REST desarrollada para la gestión del banco de preguntas y recursos académicos del proyecto **QuestionsBank**.

La API permite administrar asignaturas, preguntas, materiales de apoyo y las relaciones entre estos elementos. Está desarrollada utilizando Django y Django REST Framework.

---

## 📌 Descripción

**QuestionsBank API** es el backend encargado de proporcionar los servicios necesarios para la gestión de un banco de preguntas académico.

La API permite:

- Gestionar asignaturas.
- Crear, consultar, actualizar y eliminar preguntas.
- Gestionar materiales de apoyo.
- Asociar preguntas con materiales.
- Asociar preguntas con asignaturas.
- Almacenar imágenes de materiales mediante Cloudinary.
- Proporcionar una API REST para ser consumida por el frontend.

La arquitectura está basada en una API REST desarrollada con **Django REST Framework**.

---

## 🛠️ Tecnologías utilizadas

- **Python**
- **Django**
- **Django REST Framework**
- **PostgreSQL / SQLite**
- **Cloudinary**
- **Pillow**
- **python-decouple**
- **Git / GitHub**

---

## 📂 Estructura del proyecto

```text
api_QuestionsBank/
│
├── api/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── drf/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .env
└── README.md
