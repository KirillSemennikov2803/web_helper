from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from auth_my.models import Users
from web_helper.common import get_response_error_auth, get_response_success, get_response_error


def check_auth(login, password_hash):
    user = Users.objects.filter(login=login, password_hash=password_hash)
    if user:
        return True
    else:
        return False


class UserView(APIView):
    def post(self, request):
        try:
            user_data = request.data
            login = user_data["login"]
            password_hash = user_data["password_hash"]

            if not check_auth(login, password_hash):
                return get_response_error_auth()

            body = {
                "auth": "True"
            }
            return get_response_success(body)

        except Exception as s:
            print("auth_service error: " + s)
            return get_response_error()
