# Import native django user creation form
from django.contrib.auth.forms import UserCreationForm
# Import native django quick reverse function
from django.urls import reverse_lazy
# Import native django create view function
from django.views.generic import CreateView


# Django generic Sign-up view
class SignUpView(CreateView):
    """
    A Generic view to handle user registration.
    
    This view allows a user to create a new profile using the UserCreationForm.
    If successful the user is redirected to the login page.

    Args:
        form_class (class): Form used for user signup.
        success_url (str): Redirect url if successful.
        template_name (str)= Path to template to render.
    """

    form_class = UserCreationForm
    # Reverse to login after account creation
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
