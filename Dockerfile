FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /django

# Install system dependencies for PostgreSQL and package builds
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create the log directory for Gunicorn
RUN mkdir -p /var/log/gunicorn

COPY requirements.txt requirements.txt

EXPOSE 8000

RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "trydocker2.wsgi:application"]