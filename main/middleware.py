from django.shortcuts import redirect
from django.urls import resolve, Resolver404

class RedirectOnNotFoundMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Try resolving the URL; if it fails, redirect
            resolve(request.path_info)
        except Resolver404:
            # Redirect to the desired URL on 404
            return redirect('https://my.gov.uz/')  # Replace with the desired URL
        return self.get_response(request)
