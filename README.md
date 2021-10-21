# ![doe sangue](assets/icon-small.svg) Sanguine Scraping Tool
![GitHub](https://img.shields.io/github/license/edumco/doe-sangue-scrapy)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/davidpierre21/doe-sangue-scrapy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/davidpierre21/doe-sangue-scrapy/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/davidpierre21/doe-sangue-scrapy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/davidpierre21/doe-sangue-scrapy/context:python)
[![Code Quality Score](https://www.code-inspector.com/project/3097/score/svg)](https://frontend.code-inspector.com/public/project/3097/doe-sangue-scrapy/dashboard)

[![DeepSource](https://static.deepsource.io/deepsource-badge-light.svg)](https://deepsource.io/gh/edumco/doe-sangue-scrapy/?ref=repository-badge)


Ferramenta de monitoramento de estoque dos bancos de sangue do estado de Pernambuco.

Bancos de sangue pesquisados:
- [HEMOPE - Recife](http://www.hemope.pe.gov.br)
- [HEMATO (Grupo GSH)](https://doesanguedoevida.com.br/doar-sangue-recife)

---

## Instalação do projeto

### Usando o Linux
   #### Passos
   1. Clone o repositório
   2. Crie um ambiente virtual (Virtualenv)
      ```bash
      virtualenv venv
      ```
   3. Ative o virtualenv criado
      ```bash
      source venv/bin/activate
      ```
   4. Instale os requisitos do projeto
      ```bash
      pip install -r requirements.txt
      ```
   5. Instale o MongoDB
   6. Inicie o servico do mongo
      ```bash
      sudo service start mongod
      ```
   7. Verifique o status do serviço
      ```bash
      sudo service status mongod
      ```
---

## Coletando os dados das bases

1. Execute a busca passando como argumento o banco de sangue a ser buscado:
   ```bash
   scrapy crawl hemope
   ```
   Ou buscando em todos os bancos
   ```bash
   make py.crawl
   ```
2. Para visualizar os dados, utilize o comando:
   ```bash
   db.niveis.find();
   ```
3. Para exportar para json ou outro tipo de arquivo, fora do shell do Mongodb, utilize:
   ```bash
   mongoexport --db doe_sangue --collection niveis --out niveis.json
   ```
