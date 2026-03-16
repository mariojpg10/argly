from flask import Blueprint, jsonify
from api.services.credit_scoring import calculate_credit_profile

credit_bp = Blueprint("credito", __name__, url_prefix="/api/credito")


@credit_bp.route("/<cuil>/<salary>/<tea>", methods=["GET"])
def credit_score(cuil, salary, tea):

    try:

        salary = float(salary)
        tea = float(tea)

        result = calculate_credit_profile(cuil, salary, tea)

        return jsonify(result)

    except Exception as e:

        return jsonify({"error": str(e)}), 500
