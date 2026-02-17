from views import reponse_ok, reponse_salut


def get_routes():
    return {
        "/ok": reponse_ok,
        "/salut": reponse_salut
    }