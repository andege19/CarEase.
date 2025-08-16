from flask import Blueprint, request, jsonify

# Create a blueprint for API routes
bp = Blueprint("api", __name__)

# Example POST route for appointments
@bp.route("/get_appointments", methods=["POST"])
def get_appointments():
    # You can later replace this with actual DB queries
    data = request.get_json()
    print("Received request data:", data)

    # Dummy response for now
    appointments = [
        {"id": 1, "time": "10:00 AM", "client": "John Doe"},
        {"id": 2, "time": "11:00 AM", "client": "Jane Smith"},
    ]

    return jsonify({"status": "success", "appointments": appointments})
