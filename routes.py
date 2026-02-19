from views import reponse_ok, reponse_salut
from views_json import reponse_ok_json, reponse_salut_json

def get_routes():
    return {
        "/ok": reponse_ok,
        "/salut": reponse_salut,
        "/json/ok": reponse_ok_json,
        "/json/salut": reponse_salut_json,
    }


