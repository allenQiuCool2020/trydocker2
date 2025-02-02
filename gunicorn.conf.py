# gunicorn.conf.py

# Binding to 0.0.0.0:8000 to allow Gunicorn to be accessed from any container or machine
bind = "0.0.0.0:8000"

# Number of worker processes (adjust based on your server's CPU cores)
workers = 3  # Typically, you want (2 * CPU + 1) workers

# Log configuration
accesslog = "/var/log/gunicorn/gunicorn-access.log"  # Log access requests to this file
errorlog = "/var/log/gunicorn/gunicorn-error.log"    # Log errors to this file
loglevel = "info"  # Log level, could also be "debug" or "warning"

# Maximum requests before workers are restarted (for graceful memory management)
max_requests = 1000
max_requests_jitter = 100

# Timeout (seconds) for worker requests
timeout = 30

# Graceful reloads (good for updating the app with zero downtime)
graceful_timeout = 30
