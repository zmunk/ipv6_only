from django.shortcuts import render
import ipaddress

def ip_kind(addr):
    return ipaddress.ip_address(addr).version

def my_view(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    kind = ip_kind(ip)  # 4 or 6
    print(f"ipv{kind}:", ip)
    if kind == 4:
        return render(request, "bad.html")
    else:
        return render(request, "good.html")
