import datetime

def convert(obj):
    d = datetime.datetime.strptime(obj, "%Y-%m-%dT%H:%M:%SZ")
    return d