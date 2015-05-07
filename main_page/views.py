from django.shortcuts import render_to_response
from django.template import Context


def main_page(request):
    c = Context({'user_name': request.user.username})
    return render_to_response('main_page.html', context=c)
