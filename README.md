# Doe Sangue Scraping Tool ![doe sangue](assets/icon.svg)

Ferramenta de monitoramento de estoque dos bancos de sangue do estado de Pernambuco.

Bancos de sangue pesquisados:
- [HEMOPE - Recife](http://www.hemope.pe.gov.br)
- [HEMATO - Recife](https://doesanguedoevida.com.br/doar-sangue-recife)

---

## Instalação do projeto

### Usando o Docker

   #### Requisitos
   1. Docker Comunity Edition 19.03.5
   2. Docker compose 1.21.0

   #### Passos

### Usando o Linux

   #### Requisitos
   1. [Python 3.6.7](https://www.python.org/)
   2. [Mongodb](https://www.mongodb.com/)
   3. [Pymongo](https://api.mongodb.com/python/current/)
   4. [Python Decouple](https://github.com/henriquebastos/python-decouple)
   5. [Scrapy](https://scrapy.org/)

#### Passos
1. Instale o Python
2. Instale os requisitos do projeto
   ```bash
   pip install -r requirements.txt
   ```
3. Instale o MongoDB
4. Inicie o servico do mongo
   ```bash
   sudo service start mongod
   ```
5. Verifique o status do serviço
   ```bash
   sudo service status mongod
   ```
6. Inicie o shell do Mongo
   ```bash
   mongo
   ```
7. Selecione a base de dados chamada "doe_sangue" (se não ainda existir é criada automaticamente)
   ```bash
   use doe_sangue;
   ```
8. Crie a coleção de dados chamada "niveis"
   ```bash
   db.createCollection("niveis");
   ```
---

## Coletando os dados das bases
### No docker
### No Linux
1. Clone o repositório
   ```bash
   git clone https://github.com/DavidPierre21/doe-sangue-scrapy.git
   ``````bash
2. Navegue até o diretório do projeto
   ```bash
   cd doe_sangue
   ```
3. Finalmente, execute a busca passando como argumento o banco de sangue a ser buscado:

   ```bash
   scrapy crawl hemope
   ```
   
   Ou buscando em todos os bancos
   ```bash
   make py.crawl
   ```
4. Para visualizar os dados, utilize o comando:
   ```bash
   db.niveis.find();
   ```
5. Para exportar para json, fora do shell do Mongodb, utilize:
   ```bash
   mongoexport --db doe_sangue --collection niveis --out niveis.json
   ```
6. Para exportar para json, fora do shell do Mongodb, utilize:
   ```bash
   mongoexport --db doe_sangue --collection niveis --out niveis.json
   ```

Obs: O servidor do database esta configurado para o localhost e na porta 27017
