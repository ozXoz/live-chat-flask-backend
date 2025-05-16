from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
from extensions import mongo  # ✅ direct import

protected_bp = Blueprint("protected", __name__)

@protected_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)}, {"password": 0})

    if user:
        user["_id"] = str(user["_id"])
        return jsonify(user)

    return jsonify({"msg": "User not found"}), 404
