import os
import psutil
import json
import datetime
import time
import urllib.request

from platform import system as os_name
from crontab import CronTab

class Resources:
    def __init__(self):
        self.config_file = os.getcwd() +  '/config/mid.json'
        self.send_file = os.getcwd() +  '/config/send.json'
        self.configurations = None
        self.network = None
        self.hd = []
        self.cpu = None
        self.memory = None
        self.proccesses_by_memory = None
        self.proccesses_by_cpu = None
        self.pc_info = None
        self.loadConfigurations()

    def loadConfigurations( self ):
        try:
            with open( self.config_file, 'r' ) as config:
                self.configurations = json.load( config )
        except:
            print('Opss, arquivo não encontrado, contate o suporte')

    def getStatusDisk( self ):
        disks = self.configurations['disks']
        for h in disks:
            data = psutil.disk_usage(h)
            self.hd.append(
                {
                    'disk': h,
                    'size': data.total,
                    'usage': data.used,
                    'free': data.free,
                    'percent': data.percent
                }
            )

    def getStatusCPU( self ):
        self.cpu = psutil.cpu_percent(1)

    def getStatusMemory( self ):
        mem = psutil.virtual_memory()
        self.memory = {
            'total': mem.total,
            'available': mem.available,
            'free': mem.free,
            'used': mem.used,
            'percent': mem.percent,
        }

    def getStatusProccesses( self ):
        all_proc = []
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

        def getByMemory(e):
            return e['memory']

        self.proccesses_by_memory = all_proc
        self.proccesses_by_memory.sort( key=getByMemory, reverse=True )

    def getStatusNetwork( self ):
        self.network = {
            'ipaddrs': psutil.net_if_addrs(),
            'send': psutil.net_io_counters().bytes_recv,
            'recv': psutil.net_io_counters().bytes_sent,
            'connections': psutil.net_connections()
        }

    def updateInfo( self ):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.pc_info = {
            'mID': self.configurations['mID'],
            'cID': self.configurations['cID'],
            'date': now,
            'disk': self.hd,
            'memory': self.memory,
            'cpu': self.cpu,
            'network': self.network,
            'proccess': {
                'most_memory': self.proccesses_by_memory,
                'most_cpu': self.proccesses_by_cpu
            }
        }

    def makeJson( self ):
        try:
            with open( self.send_file, 'w' ) as rep:
                json.dump( self.pc_info, rep )
        except:
            print('Opss, não foi possivel escrever o arquivo, contate o suporte')

    def updateResourcesInfo( self ):
        self.loadConfigurations()
        self.getStatusDisk()
        self.getStatusCPU()
        self.getStatusNetwork()
        self.getStatusMemory()
        self.getStatusProccesses()
        self.updateInfo()

        if self.configurations['save_file']:
            self.makeJson()

        self.sendInfoToServer()
        self.reset()

    def sendInfoToServer( self ):
        if self.configurations['server'] == "" \
        or self.configurations['mID'] == "" \
        or self.configurations['cID'] == "":
            print( 'Error! Missing Configurations')
            return False

        URLString = "{url}".format(
            url=self.configurations['server'],
        )

        send_data = json.dumps(self.pc_info).encode('utf8')
        req = urllib.request.Request(URLString, data=send_data,
                                    headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(req)

        if response.code < 300:
            print("Successfuly updated")
            return True
        else:
            print("Coldn't update state")
            return False

    def reset(self):
        self.hd = []
        self.cpu = None
        self.memory = None
        self.network = None
        self.proccesses_by_memory = None
        self.proccesses_by_cpu = None
        self.pc_info = None

    def start( self ):
        while True:
            self.updateResourcesInfo()
            time.sleep( self.configurations['interval'] * 60 )

