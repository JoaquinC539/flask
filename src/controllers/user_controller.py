from flask import Blueprint, jsonify, request
from requests import get,post
from src.models.user import User

user_bp=Blueprint("user",__name__)

@user_bp.route("/users",methods=["GET"])
def get_users():
    data=get("https://reqres.in/api/users?page=2").json()
    return jsonify(data)
@user_bp.route('/users', methods=['POST'])
def create_user():
    data=request.get_json()
    new_user={"username":data["username"],"password":data["password"]}
    
    data_post=post("https://reqres.in/api/users?page=2",data=new_user).json()
    return jsonify(data_post)

