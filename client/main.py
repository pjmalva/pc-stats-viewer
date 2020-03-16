import platform
from crontab import CronTab
from app.Resources import Resources

def main ():
    _so_name = platform.system()
    if _so_name in [ 'Windows', 'Linux' ]:
        Resources().start()
    else:
        print('SO not suported, Linux and Windows only')

if __name__ == "__main__":
    main()
