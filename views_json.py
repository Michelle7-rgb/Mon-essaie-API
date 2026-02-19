import json


def send_json(handler, data, status=200):
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.end_headers()
    handler.wfile.write(json.dumps(data).encode())


def reponse_ok_json(handler):
    data = {
        "status": "success",
        "message": "OK"
    }
    send_json(handler, data)


def reponse_salut_json(handler):
    data = {
        "status": "success",
        "message": "SALUT"
    }
    send_json(handler, data)
