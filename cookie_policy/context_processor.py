#-*- coding: utf-8 -*-

def cookie_policy_accepted_func(request):
    if request.COOKIES.get('cookie_accepted', None):
        return True
    return False

# This "context processor" aggiunge 'show_cookie_policy' to the context of the pages
def cookie_policy(request):
    return {'cookie_accepted' : cookie_policy_accepted_func(request)}
