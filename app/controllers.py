from app import db
from flask import make_response, jsonify, request
from datetime import datetime

def controller_keepalive():
    response = make_response(jsonify({
                                        "success": True,
                                        "message": "OK",
                                        "date":datetime.now().strftime('%Y-%m-%d'),
                                        "time":datetime.now().strftime('%H:%M:%S')
                                        }),200)
    
    response.headers["Content-Type"] = "application/json"
    return response

def controller_list_carros():
    response = make_response( jsonify(
                                        message='Lista de carros.',
                                        data=db.Carros
                                        ),200)
    
    response.headers["Content-Type"] = "application/json"
    return response

def controller_get_carro():
    id=None
    try:
        url_params = request.args
        try: 
            id = url_params['id'] 
        except:# KeyError:
            id=None
            raise Exception('Parâmetro id é obrigatório')
 
        dados = list(filter(lambda x:str(x['id'])==id, db.Carros))

        response = make_response(
                jsonify(
                    message=f'Find {len(dados)} register(s)',
                    data=dados
                ),200
            )

    except Exception as e:
         response = make_response(
                jsonify(
                    message=f'Error',
                    description=str(e)
                ),400
            )
         
    response.headers["Content-Type"] = "application/json"
    return response

def controller_create_carro():
    try:
        new_car = request.json
        db.Carros.append(new_car)
        response = make_response( jsonify( message='Carro cadastrado com sucesso !'),200)
        response.headers["Content-Type"] = "application/json"
    except Exception as e:
         response = make_response(
                jsonify(
                    message=f'Error',
                    description=str(e)
                ),400
            )

    response.headers["Content-Type"] = "application/json"
    return response
