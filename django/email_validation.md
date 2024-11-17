# Table of contents
- [Table of contents](#table-of-contents)
- [Email validation with Django](#email-validation-with-django)
- [Part One](#part-one)
- [Part Two](#part-two)

# Email validation with Django
The purpose of this section is to teach how to implement an email validation form where the user will register into our platform, and in order to validate that the email is correct, then we will send a code or link in order to finish the process. 


# Part One
Take as an example this view: 
```python

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.email.import Emmail Mess


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name, 
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                password=password,
            )

            user.save()

            current_site = get_current_site(request) # Current site 
            mail_subject = "Please activate your account with us" # The subject of the email 
            body = render_to_string('app/app_verification_email.html', {
                'user': user, # What user will activate his account
                'domain': current_site,
                'uid': urlsafe_base64_encode( force_bytes(user.pk) ), # Transform to characters 
                'token': default_token_generator.make_token(user), 
            })

            to_email = email # What email will be the receiver
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()

            messages.success(request, 'The user was succesfully registered')
            return redirect('register')

```

Then we have to create the template
```html
<!-- app/app_verification_email.h-->
{% autoescape off %}

Hola {{ user }},

Por favor activa tu cuenta dandole click al siguiente link: 

http://{{domain}}{% url "activate" uidb64=uid token=token %}

Bienvenido!

{% endautoescape %}
```


Hay que hacer la url de activate 
```python
    path('activate/<uidb64>/<token>/', views.activate, name="activate")
```

En vistas
```python
def activate(request, udib64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Cuenta activada con exito")
        return redirect('login')
    else:
        messages.error(request, "No se pudo activar tu cuenta")
        return redirect('register')
```

Despues en settings
```python
# settings.py
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'echeraritours@gmail.com'
EMAIL_HOST_PASSWORD = 'FuckPelona14!'
EMAIL_USE_TLS = True
```


# Part Two
In the register view, redirect to login 

```python 
return redirect('usuario/seleccion_registro/?command=verification&email='+email)
```

In the view that we are blocking
```html
{% if request.GET.command == 'verification' %}
<div class="container mx-auto alert alert-info" role='alert' style="max-width=380px;" margin-top="100;">
    Gracias por registrarte. Entra a tu cuenta de correo para terminar de configurar tu cuenta.
</div>
{% else %}
<!-- El else es de todos los que no le saben. -->