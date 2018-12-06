

def get_client_ip(request):
    x_fordwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_fordwarded_for:
        ip = x_fordwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", None)
    return ip