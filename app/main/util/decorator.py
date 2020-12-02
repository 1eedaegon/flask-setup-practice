from functools import wraps
from flask import request

from app.main.service.auth_helper import Auth


def token_required(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get("data")

        if not token:
            return data, status

        return func(*args, **kwargs)

    return decorate


def admin_token_required(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get("data")

        if not token:
            return data, status

        admin = token.get("admin")
        if not admin:
            response_object = {"status": "fail", "message": "admin token required"}

            return response_object, 401
        return func(*args, **kwargs)

    return decorate