from django.urls import path, include
from . import views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from rest_framework import routers

# router = routers.DefaultRouter()

# router.register('DocFlutter', views.DoctorRegistrationAPIView, basename='DocFlutter')


urlpatterns = [
    path('', views.LandingPage , name='LandingPage'),
    path('home/', views.Home , name='home'),
    path('profile/', views.ProfilePage , name='profile'),
    path('registration/',views.RegistrationView.as_view(), name='registration'),
    path('services/', views.Services , name='services'),
    path('contactus/', views.ContactUs.as_view() , name='contactus'),


    path('appointment/',views.AppointmentView.as_view(), name='appointment'),



    path('doctor-registration/',views.DocRegistration.as_view(), name='doctor-registration'),


    path('accounts/login/', auth_views.LoginView.as_view(template_name='mediaid/login.html', authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='mediaid/changepassword.html',
    form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='changepassword'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='mediaid/passwordchangedone.html'),name='passwordchangedone'),

    path('logout/', auth_views.LogoutView.as_view(next_page='LandingPage'), name='logout'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='mediaid/password_reset.html', form_class=MyPasswordResetForm),
    name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='mediaid/password_reset_done.html'),
    name='password_reset_done'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='mediaid/password_reset_complete.html'),
    name='password_reset_complete'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='mediaid/password_reset_confirm.html',
    form_class=MySetPasswordForm), name='password_reset_confirm'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)