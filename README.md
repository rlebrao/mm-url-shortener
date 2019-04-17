# Encurtador de URL

Esse projeto provê um Web Service Restful, onde terá a função de encurtar URL's requisitadas pelos usuários. 

**Bibliotecas utilizadas:**

  * [Flask](http://flask.pocoo.org/) - Framework para construir microserviços na linguagem python
  * [Flask-restful](https://flask-restful.readthedocs.io/en/latest/) - Uma extensão para a biblioteca Flask. Possui suporte para a construção de APIs Restful
  * [Mysql Connector](https://dev.mysql.com/downloads/connector/python/) - Driver de conexão para o banco de dados MySql
  

**Instalação - passo a passo**

1) Para a execução desse projeto, será necessário a versão 3.6 ou maior do Python. Caso não possua, o download pode ser feito por [aqui](https://www.python.org/downloads/)
2) Além do Python 3.6+, deve-se também possuir instalado [pip](https://pypi.org/project/pip/) (Recomenda-se estar na versão mais atualizada)
3) Faça o download, ou clone esse projeto para sua máquina local.
4) Entre via linha de comando na pasta raíz do projeto e execute: ```pip install -r requirements.txt ``` para instalar todas as dependências
5) Você também deverá possuir uma instância do MySQL em sua máquina local. Sendo assim, poderá importar o arquivo url_info.sql em seu banco de dados, que será responsável por criar as tabelas necessárias para o funcionamento do serviço
6) Agora basta entrar na linha de comando e executar ```python main.py``` para inciar o serviço.
