from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django.core.validators import MinLengthValidator
from .validators import number_validator, special_char_validator, letter_validator
from golestan.users.models import BaseUser
from golestan.api.mixins import ApiAuthMixin
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from drf_spectacular.utils import extend_schema


