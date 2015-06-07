#-*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Cookie Law Decorator
def cookie_law_decorator(function):
    """
    This decorator can be used to redirect the visitor to the cookie policy page when it has not been accepted
    """
   def wrap(request, *args, **kwargs):        
       if request.COOKIES.get('cookie_accepted', False):
           return function(request, *args, **kwargs)
       else:
           return HttpResponseRedirect(reverse('cookiePolicy'))
   wrap.__doc__=function.__doc__
   wrap.__name__=function.__name__
   return wrap
