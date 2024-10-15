from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def access_code_view(request, code=None):
    if request.method == "POST":
        code = request.POST.get('code')

        # Define a list of models to check
        models = [Security_pdf]

        for model in models:
            try:
                secure_word = get_object_or_404(model, access_code=code)

                # Check if the PDF file exists
                if secure_word.continue_word and secure_word.continue_word.path:
                    file_path = secure_word.continue_word.path
                    with open(file_path, 'rb') as file:
                        response = HttpResponse(file.read(), content_type="application/pdf")
                        response['Content-Disposition'] = f'inline; filename={secure_word.continue_word.name}'
                        return response
            except Http404:
                continue  # If the code doesn't match in this model, continue to the next model

        # If no match is found, render the login page with an error
        return render(request, 'login.html', {'error': 'Invalid access code'})

    return render(request, 'login.html')


def base_redirect(request):
    return redirect('https://my.gov.uz/')


def custom_404_view(request, exception):
    # Redirect to another site
    return HttpResponseRedirect('https://my.gov.uz/')