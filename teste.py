from flask import Flask
import os

app = Flask(__name__)


@app.get("/comando/<path:programa>")
def executarPrograma(programa):
    print(programa)
    os.system(programa)
    return "Abriu o Financeiro"


@app.get("/fechar")
def fecharAplicacao():
    print("veio pra cá")
    os.system("C:\\Users\\rafael.albuquerque\\Desktop\\testeStop.bat")
    return "Fechando aplicação"


@app.get("/isAlive")
def isAlive():
    return "A aplicação está rodando"


@app.get("/atualizar")
def atualizarAplicacao():
    os.system("C:\\Users\\rafael.albuquerque\\Desktop\\testeAtt.bat")
    return "Aplicação atualizada"


app.run(port=6341)

# https://github.com/top2topii/FlaskServiceWin32/issues/1
# Tava dando problema para executar o exe no arquivo utils.py, escrito abaixo

# Traceback (most recent call last):
#   23, in show_server_banner
#   File "click\utils.py", lineFile "teste.py", line 14, in <module>
#   File "flask\app.py", line 1186, in run
#   File "flask\cli.py", line 7 299, in echo
# AttributeError: 'NoneType' object has no attribute 'write'


# https://stackoverflow.com/questions/9494739/how-to-build-a-systemtray-app-for-windows
# Trocar uma ideia com alguem q conhece python pra ver isso aqui
