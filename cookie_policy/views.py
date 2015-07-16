#-*- coding: utf-8 -*-
import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext


def set_cookie(response, key, value, days_expire = 7):
   if days_expire is None:
       max_age = 365 * 24 * 60 * 60  #one year
   else:
       max_age = days_expire * 24 * 60 * 60 
   expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
   response.set_cookie(key, value, max_age=max_age, expires=expires)
 
# Cookie Law Decorator
def cookie_law_decorator(function):
   def wrap(request, *args, **kwargs):        
       if request.GET.get('cookie_accepted', None):
           return function(request, *args, **kwargs)
       if request.COOKIES.get('cookielaw', False):
           return function(request, *args, **kwargs)
       else:
           if i18n_helper(request) == 'it':
               return HttpResponseRedirect('/it/normativa-europea-cookie')
           return HttpResponseRedirect('/en/european-cookie-law')
   wrap.__doc__=function.__doc__
   wrap.__name__=function.__name__
   return wrap


def acceptCookiePolicy_view(request):
    if 'HTTP_REFERER' in request.META:
        response = HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        response =  HttpResponseRedirect('/')
    set_cookie(response, 'cookie_accepted', 1, days_expire=365)
    return response


def policy_view(request):
    return render_to_response('cookie_policy/policy.html', {},
                              context_instance=RequestContext(request))
