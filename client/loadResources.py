import os
import psutil
import json
import datetime

config = open( os.getcwd() +  '/config/mid.json', 'r' )
config_obj = json.load( config )

all_proc = []
all_hd = []

for h in config_obj['disks']:
    data = psutil.disk_usage(h)
    all_hd.append(
        {
            'disk': h,
            'size': data.total,
            'usage': data.used,
            'free': data.free,
            'percent': data.percent
        }
    )

cpu = psutil.cpu_percent(1)

mem = psutil.virtual_memory()
memory_data = {
    'total': mem.total,
    'available': mem.available,
    'free': mem.free,
    'used': mem.used,
    'percent': mem.percent,
}

for p in psutil.process_iter():
    try:
        all_proc.append(
            {
                'id': p.pid,
                'name': p.name(),
                'memory': p.memory_percent(),
                'user': p.username()
            }
        )
    except ( psutil.NoSuchProcess, psutil.AccessDenied ):
        pass

proc_memory = []
proc_cpu = []

def getByMemory(e):
    return e['memory']

proc_memory = all_proc
proc_memory.sort( key=getByMemory, reverse=True )

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

pc_info = {
    'mid': config_obj['mid'],
    'name': config_obj['name'],
    'date': now,
    'disk': all_hd,
    'memory': memory_data,
    'cpu': cpu,
    'proccess': {
        'most_memory': proc_memory,
        'most_cpu': proc_cpu
    }
}

with open( 'config/send.json', 'w' ) as rep:
    json.dump( pc_info, rep )
