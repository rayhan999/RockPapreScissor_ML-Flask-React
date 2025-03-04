# gunicorn_config.py
workers = 1
threads = 2
timeout = 120
preload_app = True
worker_class = 'sync'
max_requests = 100
max_requests_jitter = 10