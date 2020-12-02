from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user


@api.route("/")
class UserList(Resource):
    @api.doc("list of registered users")
    @token_required
    @api.marshal_list_with(_user, envelope="data")
    def get(self):
        """ List all registered users """
        return get_all_users()

    @api.response(201, "User successfully created.")
    @api.doc("create a new user")
    @api.expect(_user, validate=True)
    def post(self):
        """ Create a new user """
        data = request.json
        return save_new_user(data=data)


@api.route("/<public_id>")
@api.param("public_id", "The user identifier")
@api.response(404, "User not found.")
class User(Resource):
    @api.doc("get a user")
    @api.marshal_with(_user)
    def get(self, public_id):
        """ Get a user given itts identifier """
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
