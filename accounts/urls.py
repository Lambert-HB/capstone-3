# Import native django path function
from django.urls import path
# Import view to address path
from .views import SignUpView

app_name = 'accounts'
urlpatterns = [
    # Link association to django built-in signup
    path("signup/", SignUpView.as_view(), name="signup"),
]
