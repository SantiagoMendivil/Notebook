# Table of contents
- [Table of contents](#table-of-contents)
- [Email validation with Django](#email-validation-with-django)

# Email validation with Django
The purpose of this section is to teach how to implement an email validation form where the user will register into our platform, and in order to validate that the email is correct, then we will send a code or link in order to finish the process. 

Take as an example this view: 
```python

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render to string
from django.utils.http import urlsafe64, urlsafed-base64, decode
from django.contrib.auth.token import default_token_generator
from django.utils.encoding import force_bytes
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

            current_site = get_current_site(request)
            mail_subject = "Please activate your account with us"
            body = render_to_string('app/app_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode( force_bytes(user.pk) ), # Transform to characters 
                'token': default_token_generator.make_token(user), 
            })

            to_email = email
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()

            messages.success(request, 'The user was succesfully registered')
            return redirect('register')

