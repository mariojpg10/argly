from flask import Blueprint, request
from api.services.data_loader import get_canasta, get_canasta_history, get_canasta_range
from api.utils.responses import success, error

canasta_bp = Blueprint("canasta", __name__, url_prefix="/api/canasta")


@canasta_bp.route("/", methods=["GET"])
def obtener_canasta():
    data = get_canasta()
    if not data:
        return error("No hay datos de canasta disponibles", 404)
    return success(data)


@canasta_bp.route("/history", methods=["GET"])
def obtener_canasta_historico():
    data = get_canasta_history()
    if not data:
        return error("No hay histórico de canasta disponible", 404)
    return success(data)


@canasta_bp.route("/range", methods=["GET"])
def obtener_canasta_rango():
    desde = request.args.get("desde")
    hasta = request.args.get("hasta")

    if not desde or not hasta:
        return error("Parámetros 'desde' y 'hasta' requeridos (YYYY-MM)", 400)

    data = get_canasta_range(desde, hasta)
    return success(data)
