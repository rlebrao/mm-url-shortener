# Encurtador de URL

Esse projeto provê um Web Service Restful, onde terá a função de encurtar URL's requisitadas pelos usuários. 

**Bibliotecas utilizadas:**

  * [Flask](http://flask.pocoo.org/) - Framework para construir microserviços na linguagem python
  * [Flask-restful](https://flask-restful.readthedocs.io/en/latest/) - Uma extensão para a biblioteca Flask. Possui suporte para a construção de APIs Restful
  * [Mysql Connector](https://dev.mysql.com/downloads/connector/python/) - Driver de conexão para o banco de dados MySql
  

**Instalação - passo a passo**

1) Para a execução desse projeto, será necessário a versão 3.6 ou maior do Python. Caso não possua, o download pode ser feito por [aqui](https://www.python.org/downloads/)
2) Além do Python 3.6+, deve-se também possuir instalado o [pip](https://pypi.org/project/pip/) (Recomenda-se estar na versão mais atualizada)
3) Faça o download, ou clone esse projeto para sua máquina local.
4) Entre via linha de comando na pasta raíz do projeto e execute: ```pip install -r requirements.txt ``` para instalar todas as dependências
5) Você também deverá possuir uma instância do MySQL em sua máquina local. Sendo assim, poderá importar o arquivo url_info.sql em seu banco de dados, que será responsável por criar as tabelas necessárias para o funcionamento do serviço
6) Agora basta entrar na linha de comando e executar ```python main.py``` para inciar o serviço. O serviço irá ser iniciado no localhost na porta 5000 (http://127.0.0.1:5000)

**Configuração**

Como padrão, o projeto vem configurado para acessar a instância local do mysql. Caso deseja alterar as informações de conexão com o banco de dados, sinta-se livre para editar os valores no arquivo ```config.json```, dentro da pasta config

**Utilização**

*Enpoints*

 * http://127.0.0.1:5000/shorturl
     * Esse endpoint é responsável por retornar a URL encurtada ao usuário.
     * Métodos permitidos: **POST**
     * Parâmetros: 
         * "url" - URL que deve ser encurtada 
     * Exemplo de envio:
         ``` 
             curl -X POST \
             http://127.0.0.1:5000/shorturl \
             -H 'Content-Type: application/json' \
             -d '{
             "url":"https://g1.com.br"
             }' 
         ```
      * Exemplo de resposta:
         ```json
         {
           "original": "https://g1.com.br",
           "short": "https://mm.com/2935E2"
         }
         ```
     
 * http://127.0.0.1:5000/get-details
     * Esse endpoint é responsável por retornar todas as URLs cadastradas, com a versão encurtada, versão original, total de cliques e a data que ela foi gerada.
     * Métodos permitidos: **GET**
     * Exemplo de envio:
      ``` json
      curl -X GET \
      http://localhost:5000/get-details \
      -H 'Content-Type: application/json' \
      ```
     * Exemplo de respota:
     ``` json  
     {
     "url_details": [
        {
            "original": "https://g1.com.br",
            "short": "https://mm.com/2935E2",
            "timestamp": "Wed, 17 Apr 2019 10:26:37 GMT",
            "total_clicks": 1554
        }
    ]
   }
     ```
