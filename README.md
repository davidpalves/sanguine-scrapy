# ![doe sangue](assets/icon-small.svg) Doe Sangue Scraping Tool 
![GitHub](https://img.shields.io/github/license/edumco/doe-sangue-scrapy)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/280a21aeb4df47fd9a9f5ab22f7d85d9)](https://www.codacy.com/manual/edumco/doe-sangue-scrapy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=edumco/doe-sangue-scrapy&amp;utm_campaign=Badge_Grade)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/davidpierre21/doe-sangue-scrapy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/davidpierre21/doe-sangue-scrapy/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/davidpierre21/doe-sangue-scrapy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/davidpierre21/doe-sangue-scrapy/context:python)
[![Code Quality Score](https://www.code-inspector.com/project/3097/status/svg)](https://frontend.code-inspector.com/public/project/3097/doe-sangue-scrapy/dashboard)
[![Code Quality Score](https://www.code-inspector.com/project/3097/score/svg)](https://frontend.code-inspector.com/public/project/3097/doe-sangue-scrapy/dashboard)

[![DeepSource](https://static.deepsource.io/deepsource-badge-light.svg)](https://deepsource.io/gh/edumco/doe-sangue-scrapy/?ref=repository-badge)


Ferramenta de monitoramento de estoque dos bancos de sangue do estado de Pernambuco.

Bancos de sangue pesquisados:
- [HEMOPE - Recife](http://www.hemope.pe.gov.br)
- [HEMATO (Grupo GSH)- Recife](https://doesanguedoevida.com.br/doar-sangue-recife)

---

## Instalação do projeto

### Usando o Docker

   #### Requisitos
   1. Docker Comunity Edition 19.03.5
   2. Docker compose 1.21.0

   #### Passos
   1. Clone o repositório
   2. Navegue até a pasta criada
   2. Inicie os servicos usando o docker-compose
      ```bash
      docker-compose up -d --build
      ``` 
    
### Usando o Linux

   #### Requisitos
   1. [Mongodb 4.11](https://www.mongodb.com/)
   2. [Python 3.6.7](https://www.python.org/)
   3. [Pymongo 3.7.2](https://api.mongodb.com/python/3.7.2/api/index.html)
   4. [Python Decouple 3.1](https://github.com/henriquebastos/python-decouple)
   5. [Scrapy 1.5.1](https://scrapy.org/)

   #### Passos
   1. Clone o repositório
   2. Instale o Python
   3. Instale os requisitos do projeto
      ```bash
      pip install -r requirements.txt
      ```
   4. Instale o MongoDB
   5. Inicie o servico do mongo
      ```bash
      sudo service start mongod
      ```
   6. Verifique o status do serviço
      ```bash
      sudo service status mongod
      ```
   7. Inicie o shell do Mongo
      ```bash
      mongo
      ```
   8. Selecione a base de dados chamada "doe_sangue" (se não ainda existir é criada automaticamente)
      ```bash
      use doe_sangue;
      ```
   9. Crie a coleção de dados chamada "niveis"
      ```bash
      db.createCollection("niveis");
      ```
---

## Coletando os dados das bases

1. Acesse o conteiner ou navegue até o diretório do projeto
2. Execute a busca passando como argumento o banco de sangue a ser buscado:
   ```bash
   scrapy crawl hemope
   ```
   Ou buscando em todos os bancos
   ```bash
   make py.crawl
   ```
3. Para visualizar os dados, utilize o comando:
   ```bash
   db.niveis.find();
   ```
4. Para exportar para json, fora do shell do Mongodb, utilize:
   ```bash
   mongoexport --db doe_sangue --collection niveis --out niveis.json
   ```
6. Para exportar para json, fora do shell do Mongodb, utilize:
   ```bash
   mongoexport --db doe_sangue --collection niveis --out niveis.json
   ```
