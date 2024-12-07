from django.shortcuts import redirect, render
from django.utils.timezone import now
from .models import *

def track_click(request):
    ip_address = get_client_ip(request)
    browser_info = request.META.get('HTTP_USER_AGENT', 'Unknown')
    project = request.GET.get('project', 'default')

    Click.objects.create(
        ip_address = ip_address,
        browser_info = browser_info,
        timestamp = now(),
        project = project
    )

    return redirect('thank_you', project=project)



def thank_you(request, project):
    return render(request, 'tracker/thank_you.html', context={'project':project})



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    return ip
