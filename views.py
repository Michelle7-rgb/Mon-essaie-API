def reponse_ok(handler):
    handler.send_response(200)
    handler.wfile.write("OK")


def reponse_salut(handler):
    handler.send_response(200)
    handler.wfile.write("SALUT")