# Apple Registration Project

This is a Django web application designed for registering and tracking apples, potentially within an orchard or agricultural context. It allows users to record details about individual apples, including their breed, year of production, and location (row, column, latitude, longitude).

## Features

*   User authentication (implied by `Profile` model linked to `User`)
*   Apple registration and tracking
*   Stores apple details: breed, production year, location coordinates.

## Setup and Running

1.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2.  **Install Dependencies:**
    *   Ensure necessary system build dependencies for Pillow are installed (example for Debian/Ubuntu):
        ```bash
        sudo apt-get update
        sudo apt-get install -y python3-dev libjpeg-dev zlib1g-dev libfreetype-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev
        ```
    *   Install Python packages:
        ```bash
        pip install -r requirements.txt
        ```

3.  **Apply Database Migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Run Development Server:**
    ```bash
    python manage.py runserver
    ```

The application should now be running at `http://127.0.0.1:8000/`.