# Import native django user creation form
from django.contrib.auth.forms import UserCreationForm
# Import native django quick reverse function
from django.urls import reverse_lazy
# Import native django create view function
from django.views.generic import CreateView


# Django generic Sign-up view
class SignUpView(CreateView):

    form_class = UserCreationForm
    # Reverse to login after account creation
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
