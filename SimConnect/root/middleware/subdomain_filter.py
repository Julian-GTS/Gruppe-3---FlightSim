class SubdomainFilter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host_parts = request.get_host().split('.')
        if len(host_parts) > 2 and host_parts[0] == 'api':
            request.urlconf = 'api.urls'
        elif len(host_parts) > 2 and host_parts[0] == 'sc':
            request.urlconf = 'upload_jason.urls'
        return self.get_response(request)