from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
import datetime

from auth_my.models import Users, Notes
from auth_my.views import check_auth
from web_helper.common import get_response_error_auth, get_response_success, get_response_error


class UserView(APIView):
    def post(self, request):
        try:
            user_data = request.data
            login = user_data["login"]
            password_hash = user_data["password_hash"]
            notes = user_data["notes"]

            answer = []
            if not check_auth(login, password_hash):
                return get_response_error_auth()
            user = Users.objects.filter(login=login, password_hash=password_hash)
            user = user[0]

            copy_notes = notes

            for note in notes:
                date = note["date"]
                note_server = Notes.objects.filter(user_id=user.id, date=date)
                if not note_server:
                    note.update({"status": "delete"})
                    answer.append(note)

            note_server = Notes.objects.filter(user_id=user.id)

            for note in note_server:
                date = note.date
                text = note.text
                searchDict = {
                    "date":date.isoformat()[:-6]+"Z",
                    "text":text
                }
                if not searchDict in notes:
                    answer.append({
                    "date":date,
                    "text":text,
                    "status": "add"
                })
            body = {
                "answer":answer
            }
            return get_response_success(body)

        except Exception:
            print("auth_service error: ")
            return get_response_error()
