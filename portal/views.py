from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from portal.forms import PortalLoginForm


def hello_world(request):
    return HttpResponse("Hello World!!")


@login_required()
def portal_home(request):
    return HttpResponse("Portal home")


def portal_login(request):
    if request.user.is_authenticated():
        return redirect('portal_home')
    form = PortalLoginForm(initial=request.GET)
    if request.method == "POST":
        form = PortalLoginForm(request.POST, request=request)
    template_data = {'form': form}
    return render(request, 'portal/login.html', template_data)