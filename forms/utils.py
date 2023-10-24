import logging

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')



def ipaddress(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        return user_ip.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def log(request, message):
    loged_user = request.user.username
    ip = ipaddress(request)
    logging.info(f'{ip} {loged_user} {message}')
