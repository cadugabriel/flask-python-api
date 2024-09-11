# flask-python-api
Exemplo de API utilizando framework Flask


# Introdução
Essa aplicação FLASK irá simular um cadastro de veículos


# Estrutura do projeto:
app\__init__.py     : Ponto inicial
app\config.py       : Arquivo de configurações
app\controllers.py  : Controle das ações recebidas das rotas 
app\db.py           : Arquivo simulando banco de dados
app\routes.py       : Rotas dos endPoints


# Passo a passo para utilização
1. Recomenda-se criar um ambiente virtual:
    $ python -m venv env

2. Atualize o ambiente:
    $ python.exe -m pip install --upgrade pip

2. Instale as bibliotecas contidas no arquivo requirements.txt
    $ pip install -r requirements.txt

3. Para testar digite "flask run" na raiz do projeto
    $ flask run

4. A aplicação será iniciada no endereço http://127.0.0.1:5000


# Para testar
1. Keep Alive:
    Objetivo   : Verificar se a API está no AR
    Tipo       : Get
    URL        : http://127.0.0.1:5000/keepalive
    Parâmetros : -
    Retorno    : Mensagem OK

2. Listar Carros
    Objetivo    : Listar os carros existentes
    Tipo        : Get
    URL         : http://127.0.0.1:5000/list_carros
    Parâmetros  : -
    Retorno     : Lista de carros

3. Buscar Carro
    Objetivo    : Buscar informações de um determinado carro
    Tipo        : Get
    URL         : http://127.0.0.1:5000/get_carro?id=<id do carro>
    Parâmetros  : id
    Retorno     : Carro pesquisado

4. Cadastrar Carro
    Objetivo    : Buscar informações de um determinado carro
    Tipo        : Post
    URL         : http://127.0.0.1:5000/create_carro
    Parâmetros  : no raw deverá ser passado o seguinte json
                        {
	                        "id"    : ???,
	                        "marca" : "???",
	                        "modelo": "???",
	                        "ano"   : ???
                        }
    Retorno     : Mensagem informando se o cadadtro foi realizado com sucesso