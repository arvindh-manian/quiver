from flask import send_file
import os
import requests
from datetime import datetime, timedelta
import logging
import os

# stores stringnames of files that have been cached
cache_times = dict()


def request_file_from_server(app, filename, server=f"http://{os.environ['INGESTION_PULL_SERVICE_HOST']}:{os.environ['INGESTION_PULL_SERVICE_PORT']}/streams/hls"):
    try:
        response = requests.get(f'{server}/{filename}')
        response.raise_for_status()

        with open(f'/app/cache/{filename}', 'wb+') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)

        cache_times[filename] = datetime.now()
    except Exception as e:
        app.logger.error(f"Error caching file: {e}")

def is_file_stale(filename):
    if filename not in cache_times:
        return True

    base_name, ext = filename.split('.')

    if ext == 'm3u8':
        cache_expiration_time = timedelta(seconds=1)
    elif ext == 'ts':
        cache_expiration_time = timedelta(seconds=600)
    else:
        return True

    earliest_valid_cache_time = datetime.now() - cache_expiration_time
    valid_cache = cache_times[filename] > earliest_valid_cache_time

    if not valid_cache:
        del cache_times[filename]

    return valid_cache

def fetch_file(app, filename):
    if is_file_stale(filename):
        request_file_from_server(app, filename)
    else:
        logging.debug(f"Fetching {filename} from cache")
    return send_file(f'cache/{filename}')