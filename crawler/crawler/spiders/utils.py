from datetime import datetime
import requests
import pytz


def convert_datetime(string):
    tz = pytz.timezone('Asia/Saigon')
    dt = tz.localize(datetime.strptime(string, '%d-%m-%Y, %H:%M'))
    return dt


def get_file_size(url):
    try:
        r = requests.head(url)
        return int(r.headers['Content-Length'])//1024
    except Exception:
        return 0
