from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.utils import timezone
from datetime import timedelta

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.failed_attempts >= 3:
            if timezone.now() > user.last_failed_attempt + timedelta(minutes=5):
                user.failed_attempts = 0
                user.save()
            else:
                form.add_error(None, "Account is locked. Please try again later.")
                return self.form_invalid(form)
        user.failed_attempts = 0
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        user = form.get_user()
        if user:
            user.failed_attempts += 1
            user.last_failed_attempt = timezone.now()
            user.save()
        return super().form_invalid(form)

def accounts_home(request):
    return render(request, 'accounts/home.html')
