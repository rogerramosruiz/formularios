import logging
from datetime import datetime

from .models import Log

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')



def ipaddress(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        return user_ip.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def logger(request, usuario, accion, messagedb, messagetxt):
    loged_user = request.user
    ip = ipaddress(request)

    log_db(ip, loged_user, usuario, accion, messagedb)
    log_txt(ip, loged_user.username, accion, messagetxt)

def log_db(ip, loged_user, usuario, accion, message):
    log = Log()
    log.user = loged_user
    log.usuario = usuario
    log.ip = ip
    log.accion = accion
    log.descripcion = message
    log.time_stamp = datetime.now()
    log.save()


def log_txt(ip, loged_user, accion, message):
    logging.info(f'{ip} {loged_user} {accion} {message}')