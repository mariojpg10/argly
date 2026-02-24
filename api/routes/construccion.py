from flask import Blueprint
from api.services.data_loader import get_construccion
from api.utils.responses import success, error

construccion_bp = Blueprint("construccion", __name__, url_prefix="/api/construccion")


@construccion_bp.route("/", methods=["GET"])
def obtener_construccion():
    """
    Obtener el último índice de costo de construcción y precio por m2
    """
    data = get_construccion()
    if not data:
        return error("No hay datos de construcción disponibles", 404)
    return success(data)
