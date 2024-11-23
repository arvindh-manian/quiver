from flask import send_file
import os
import requests
import logging
from diskcache import Cache

cache = Cache('/app/cache')

def request_file_from_server(app, filename, server=f"http://{os.environ['INGESTION_PULL_SERVICE_HOST']}:{os.environ['INGESTION_PULL_SERVICE_PORT']}/streams/hls"):
    try:
        response = requests.get(f'{server}/{filename}')
        response.raise_for_status()

        with open(f'/app/cache/{filename}', 'wb+') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)

        base_name, ext = filename.split('.')
        if ext == 'm3u8':
            cache_expiration_time = 1  # seconds
        elif ext == 'ts':
            cache_expiration_time = 600  # seconds
        else:
            cache_expiration_time = 3600  # default to 1 hour

        cache.set(filename, True, expire=cache_expiration_time)
    except Exception as e:
        app.logger.error(f"Error caching file: {e}")

def fetch_file(app, filename):
    file_path = f'/app/cache/{filename}'
    if not cache.get(filename):
        request_file_from_server(app, filename)
    else:
        logging.debug(f"Fetching {filename} from cache")
    return send_file(file_path)