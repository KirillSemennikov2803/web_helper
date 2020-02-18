from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
import datetime

from auth_my.models import Users, Notes, Notifications
from auth_my.views import check_auth
from web_helper.common import get_response_error_auth, get_response_success, get_response_error


class UserView(APIView):
    def post(self, request):
        try:
            user_data = request.data
            login = user_data["login"]
            password_hash = user_data["password_hash"]
            note = user_data["note"]
            status = user_data["status"]
            if not check_auth(login, password_hash):
                return get_response_error_auth()
            user = Users.objects.filter(login=login, password_hash=password_hash)
            user = user[0]
            if status == "add":
                Notes.objects.create(user_id=user,text=note["text"], date=note["date"])
            elif status =="change":
                note_c =Notes.objects.filter(user_id=user,date=note["date"])
                note_c = note_c[0]
                note_c.text = note["text"]
                note_c.save()
            elif status == "delete":
                note_c = Notes.objects.filter(user_id=user, date=note["date"])
                note_c = note_c[0]
                note_c.delete()

            body = {
                "answer": "success"
            }
            return get_response_success(body)

        except Exception:
            print("auth_service error: ")
            return get_response_error()