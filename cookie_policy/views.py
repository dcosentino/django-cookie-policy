#-*- coding: utf-8 -*-
import datetime

from django.http import HttpResponseRedirect


def set_cookie(response, key, value, days_expire = 7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires)

def acceptCookiePolicy_view(request):
    if 'HTTP_REFERER' in request.META:
        response = HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        response =  HttpResponseRedirect('/')
    set_cookie(response, 'cookie_accepted', 1, days_expire=365)
    return response
