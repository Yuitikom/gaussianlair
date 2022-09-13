from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('<int:user_id>', views.profileuser, name='editprofile'),
    path('/changepassword', PasswordChangeView.as_view(template_name='editprofile/changepasswordpage.html',success_url=reverse_lazy('password_change_done')), name='changepassword'),
    path('changepassword/done', PasswordChangeDoneView.as_view(template_name='editprofile/passwordsuccesspage.html'), name='password_change_done'),
 ]

