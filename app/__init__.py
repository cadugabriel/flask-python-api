from flask import Flask
from . import config
import datetime
import warnings

warnings.filterwarnings("ignore")
app = Flask(__name__)           # Inicia Flask
app.config.from_object(config)  # Carrega configurações

print("{:%d/%m/%Y %H:%M:%S} Iniciou - {}".format(datetime.datetime.now(),__name__))

from app import routes          # Inicia as rotas da API (deve ficar aqui, pois só pode ser chamado após iniciar objeto app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
