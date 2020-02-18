from rest_framework.response import Response


def get_response_error():
    body = {
        "errorType": "Что то пошло не так"
    }
    return setup_cors_response_headers(Response(body, status=500, content_type="application/json"))


def get_response_error_auth():
    body = {
        "errorType": "Не авторизован"
    }
    return setup_cors_response_headers(Response(body, status=401, content_type="application/json"))


def get_response_success(body):
    return setup_cors_response_headers(Response(body, status=200, content_type="application/json"))


def setup_cors_response_headers(res):
    res["Access-Control-Allow-Origin"] = "http://127.0.0.1:1329"
    res["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    res["Access-Control-Allow-Headers"] = \
        "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    res["Access-Control-Allow-Credentials"] = "true"

    return res
