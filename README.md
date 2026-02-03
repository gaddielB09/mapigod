# MapiGod 📍
> **Gestiona tus ubicaciones con precisión divina.**

![Estado del Proyecto](https://img.shields.io/badge/Estado-Finalizado-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-lightgrey)

## 📖 Descripción del Proyecto

**MapiGod** es una aplicación web integral de geolocalización diseñada para permitir a los usuarios interactuar con mapas de manera intuitiva. La aplicación permite detectar la ubicación actual del usuario, colocar marcadores personalizados, guardar puntos de interés y gestionarlos a través de un panel de control dinámico.

El proyecto es el resultado de una evolución progresiva a través de 5 etapas (actividades), culminando en una solución robusta desplegada en la nube.

## 📂 Estructura del Repositorio

Este repositorio documenta el desarrollo paso a paso de la aplicación:

* **📁 Actividad 1:** *Landing Page* (Diseño y presentación inicial).
* **📁 Actividad 2:** *Geolocalización* (Integración del mapa y detección de ubicación del usuario).
* **📁 Actividad 3:** *Marcadores* (Funcionalidad para añadir y guardar puntos en el mapa).
* **📁 Actividad 4:** *Panel de Control* (Visualización de los puntos guardados en una lista interactiva).
* **📁 Actividad 5 (Final):** *Integración Total* (Unificación de todas las funcionalidades anteriores en una sola app).

> **Nota:** La versión final (Actividad 5) se encuentra actualmente desplegada y operativa en **PythonAnywhere**.

---

## 🛠️ Stack Tecnológico

El proyecto utiliza tecnologías modernas para asegurar rendimiento y diseño responsivo:

* **Backend:** [Flask](https://flask.palletsprojects.com/) (Python) - Para el enrutamiento y lógica del servidor.
* **Mapas:** [Leaflet.js](https://leafletjs.com/) - Para la renderización de mapas interactivos y marcadores.
* **Estilos:** [Tailwind CSS](https://tailwindcss.com/) - Para una interfaz de usuario limpia, moderna y responsiva.
* **Almacenamiento:** Sistema de archivos/JSON (según implementación) para la persistencia de puntos.

---

## 🚀 Cómo correrlo localmente

Sigue estos pasos para ejecutar la versión integrada (Actividad 5) en tu máquina local:

1.  **Clona el repositorio:**
    ```bash
    git clone <URL_DE_TU_REPO>
    cd MapiGod
    ```

2.  **Navega a la carpeta de la integración final:**
    ```bash
    cd "Actividad 5"
    ```
    *(Nota: Asegúrate de entrar a la carpeta donde está el `app.py` final)*.

3.  **Crea y activa un entorno virtual (Opcional pero recomendado):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Instala las dependencias:**
    ```bash
    pip install Flask
    ```

5.  **Ejecuta la aplicación:**
    ```bash
    python app.py
    ```

6.  **Abre tu navegador:**
    Visita `http://127.0.0.1:5000` para ver MapiGod en acción.

---

## 🎨 Justificación de Diseño (UX/UI)

El diseño de MapiGod prioriza la **usabilidad y la claridad**, basándose en las iteraciones realizadas durante las actividades previas:

* **Navegación Intuitiva:** El mapa ocupa el protagonismo visual, permitiendo al usuario entender la función principal de inmediato (Actividad 2).
* **Feedback Visual:** Al hacer clic en el mapa, el usuario recibe confirmación inmediata mediante marcadores (Actividad 3) y actualizaciones en la lista lateral (Actividad 4).
* **Estética Limpia:** Gracias a **Tailwind CSS**, eliminamos el desorden visual, utilizando espaciados amplios y tipografía legible, lo que facilita el uso tanto en móviles como en escritorio.
* **Consistencia:** La integración final (Actividad 5) mantiene una coherencia visual entre la Landing Page y la aplicación funcional, ofreciendo una experiencia de usuario fluida sin "saltos" de diseño.

---

## 🤖 Créditos a la IA

Este código fue co-creado con **Gemini Canvas**.

* **Prompt principal utilizado:** *"Genera una estructura de aplicación Flask que integre un mapa de Leaflet, permita guardar coordenadas y las muestre en una lista lateral estilizada con Tailwind."*

---
Hecho con ❤️ por [Tu Nombre/Usuario]
