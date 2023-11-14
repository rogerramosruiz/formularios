from django import template

register = template.Library()

@register.filter(name='user_belongs_to_group')
def user_belongs_to_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter(name='can_download')
def can_download(user):
    return user.groups.filter(name='Exportar').exists()