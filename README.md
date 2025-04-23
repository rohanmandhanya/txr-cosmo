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

    #### e. Run the Django development server
    ```
    python manage.py runserver
    ```

    The web app will be exposed on port 8000, and the endpoints will be accessible at http://localhost:8000/dashboard

---

## 📆 Scheduled Ingestion

The app uses APScheduler to ingest shipment data from the CosmoCargo API every 30 minutes.

Scheduler is configured in shipments/tasks.py
Automatically runs on Django app startup
To customize the interval, adjust [this line](https://github.com/rohanmandhanya/txr-cosmo/blob/de92482e356ffdc55759d13fc1c50ba95686bf5c/shipments/tasks.py#L48) in tasks.py:

```python
# Every 15 minutes (default)
scheduler.add_job(fetch_and_store_shipments, 'interval', minutes=15)

# Alternatives:
# scheduler.add_job(fetch_and_store_shipments, 'interval', minutes=5)
# scheduler.add_job(fetch_and_store_shipments, 'interval', seconds=30)
# scheduler.add_job(fetch_and_store_shipments, 'interval', hours=1)
```

---

## ✍️ Future Improvements

- Unit test and integration test
- Add Logger
- Celery Beat can be used for distrbuted system