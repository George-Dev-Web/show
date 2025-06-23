from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint('guest', __name__, url_prefix='/guests')

@guest_bp.route("", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    return jsonify([
        {
            "id": guest.id,
            "name": guest.name,
            "occupation": guest.occupation
        } for guest in guests
    ])
