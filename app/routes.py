from app import app, controllers

# Exemplo verificar se aplicação está no ar
@app.route('/keepalive', methods=['GET'])
def keepalive():
    return controllers.controller_keepalive()

# Exemplo listagem
@app.route('/list_carros', methods=['GET'])
def list_carros():
    return controllers.controller_list_carros()

# Exemplo filtrando (com passagem de parâmetro)
@app.route('/get_carro', methods=['GET'])
def get_carro():
    return controllers.controller_get_carro()

#Exemplo Post
@app.route('/create_carro',methods=['POST'])
def create_carro():
    return controllers.controller_create_carro()
