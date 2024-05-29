from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.views import View
import pytesseract
from PIL import Image
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import User, Doctor
from .forms import *
import os, openai
from PIL import Image
from django.conf import settings
from django.core.mail import EmailMessage
from datetime import datetime 
from django.views.generic import ListView
from django.template import context
from django.template.loader import render_to_string, get_template
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
import io
from .serializers import DoctorSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.views.decorators.csrf  import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from sslcommerz_lib import SSLCOMMERZ 
from decimal import Decimal


api_key = os.environ.get("OPENAI_KEY")
openai.api_key = api_key


# Create your views here.
def LandingPage(request):
    return render(request, 'mediaid/LandingPage.html')





def Home(request):
    return render(request, 'mediaid/home.html')






def Services(request):
    return render(request, 'mediaid/services.html')







class ContactUs(View):
    def get(self,request):
        return render(request, 'mediaid/contactus.html')




def ProfilePage(request):
    return render(request, 'mediaid/profile.html',{'active':'btn-info'})








class RegistrationView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request, 'mediaid/register.html' , {'form':form})
    




class DocRegistration(View):
    def get(self,request):
        form = DoctorForm()
        return render(request, 'mediaid/doctorreg.html',{'form':form})




class AppointmentView(View):
    
    def get(self,request):
        return render(request, 'mediaid/appointment1.html')
