# 🚀 CosmoCargo Dashboard

A galaxy-level shipment dashboard for the fictional interstellar logistics company, **CosmoCargo**. This Django-based web app allows engineers to ingest shipment data from a live API, store it in a relational database, and display it in a user-friendly dashboard with search and creation capabilities.

---

## ✨ Features

- **Live Data Ingestion**  
  Scheduled ETL from the CosmoCargo shipments API every 30 minutes.

- **Clean Data Modeling**  
  Relational schema with normalized `Location`, `WeatherForecast`, and `Shipment` models.

- **REST API**  
  Exposes endpoints with filtering, search, and ordering.

- **HTML Dashboard**  
  Easily explore shipments with a clean, minimal UI.

- **Manual Shipment Entry**  
  Web form to manually add new shipment records.

---

## 📦 Tech Stack

- **Backend**: Django + Django REST Framework  
- **ETL & Scheduling**: APScheduler  
- **Database**: PostgreSQL
- **Frontend**: Django templates

---
## 🧰 Prerequisites

- 🐍 [Python 3.8+](https://www.python.org/downloads/)
- 🐳 [Docker & Docker Compose](https://docs.docker.com/get-docker/)
- 🎭 [Playwright](https://playwright.dev/python/docs/intro) (`playwright install`)
- ⚙️ `pip`, `venv`, and Git
- 🧱 [Redis](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/)


---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/rohanmandhanya/trx-cosmo.git
   cd trx-cosmo
   ```

2. **Run the Application Using Docker Compose**
    ```bash
    docker-compose up
    ```

    The web app will be exposed on port 8000, and the endpoints will be accessible at http://localhost:8000/dashboard
 
3. **Run the Application without Docker**
    #### a. Set up virtual environment (recommended)
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

    #### b. Install dependencies
    ```
    pip install -r requirements.txt
    ```

    #### c. Apply migrations (no models, but standard Django setup)
    ```
    python manage.py migrate
    ```

    #### d. Install Playwright browsers
    ```
    playwright install
    ```
    
    #### e. Start Redis Server
    ```
    redis-server
    ```
    *May have to change [CELERY_BROKER_URL](https://github.com/rohanmandhanya/txr-cosmo/blob/6cf58dc85908080d9794f9920fe77f3de37299bc/cosmo_cargo/settings.py#L141) settings from `redis://redis:6379/0` to `redis://localhost:6379/0`*

    #### e. Run the Django development server
    ```
    python manage.py runserver
    ```

    #### f. Start Celery Worker
    ```
    celery -A core worker --loglevel=info
    ```

    #### j. Start Celery Beat (Optional: for scheduled tasks)
    ```
    celery -A core beat --loglevel=info
    ```


    The web app will be exposed on port 8000, and the endpoints will be accessible at http://localhost:8000/dashboard

---

## 📆 Scheduled Ingestion

The app uses Celery-Beat to ingest shipment data from the CosmoCargo API every 30 minutes.

Scheduler is configured in shipments/apps.py
Automatically runs on Django app startup
To customize the interval, adjust [this line](https://github.com/rohanmandhanya/txr-cosmo/blob/6cf58dc85908080d9794f9920fe77f3de37299bc/shipments/apps.py#L14) in apps.py:

Can also read about celery beat interval [here](https://django-celery-beat.readthedocs.io/en/latest/#example-creating-interval-based-periodic-task) on how to set or change intervals

```python
# Every 15 minutes (default)
schedule, _ = IntervalSchedule.objects.get_or_create(every=30,period=IntervalSchedule.MINUTES)

# Alternatives:
# schedule, _ = IntervalSchedule.objects.get_or_create(every=30,period=IntervalSchedule.SECONDS)
# schedule, _ = IntervalSchedule.objects.get_or_create(every=3,period=IntervalSchedule.HOURS)
```

---

## ✍️ Future Improvements

- Unit test and integration test
- Add Logger
- Celery Beat can be used for distrbuted system
- Add Fragments in [Docker Compose](https://docs.docker.com/reference/compose-file/fragments/#example-4)
