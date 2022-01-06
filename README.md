# ![doe sangue](assets/icon-small.svg) Sanguine Scraping Tool

Ferramenta de monitoramento de estoque dos bancos de sangue do estado de Pernambuco.

Bancos de sangue pesquisados:
- [HEMOPE - Recife](http://www.hemope.pe.gov.br)
- [HEMATO (Grupo GSH)](https://doesanguedoevida.com.br/doar-sangue-recife)

---
## Sumário
1. [Instalação do Projeto](https://github.com/davidpalves/sanguine-scrapy#instala%C3%A7%C3%A3o-do-projeto)
2. [Coletando os dados das bases](https://github.com/davidpalves/sanguine-scrapy#coletando-os-dados-das-bases)
3. [Executando o servidor Flask](https://github.com/davidpalves/sanguine-scrapy#executando-o-servidor-flask)
4. [Endpoints da API](https://github.com/davidpalves/sanguine-scrapy#endpoints-da-api)

## Instalação do projeto

Versão Python: 3.7.8
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

## Executando o servidor Flask

1. Certifique-se que você configurou, em seu arquivo `.env` as suas variáveis de ambiente de acordo com o arquivo `.env.example`

2. Para executar o servidor com as devidas configurações, você pode utilizar o comando:
```shell
make runserver
```

3. Você deverá ser capaz de acessar o servidor através da URL:
```
127.0.0.1:5000
```

## Endpoints da API

### Listar todos os bancos de sangue

`/v1/`

#### Request

```shell
curl -i -H 'Accept: application/json' http://127.0.0.1:5000
```

#### Response

```json
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 6777
Server: Werkzeug/1.0.1 Python/3.7.8
Date: Sun, 02 Jan 2022 05:47:28 GMT

[
   {
    "banco": "HEMOPE",
    "cidade": "Recife",
    "data_extracao": "Sat, 01 Jan 2022 02:51:56 GMT",
    "endereco": "RUA JOAQUIM NABUCO, 171 - CEP 52.011-900 - GRA\u00c7AS, RECIFE",
    "estado": "PE",
    "sangue": {
      "A+": "critica",
      "A-": "critica",
      "AB+": "critica",
      "AB-": "estavel",
      "B+": "critica",
      "B-": "alerta",
      "O+": "critica",
      "O-": "critica"
    },
    "unidade": null,
    "url": "http://www.hemope.pe.gov.br/"
  },
  {
    "banco": "HEMATO",
    "cidade": "S\u00e3o Paulo",
    "data_extracao": "Sat, 01 Jan 2022 02:51:57 GMT",
    "endereco": "Rua Tom\u00e1s Carvalhal, 711  - Para\u00edso",
    "estado": "SP",
    "sangue": {
      "A+": "estavel",
      "A-": "alerta",
      "AB+": "estavel",
      "AB-": "estavel",
      "B+": "estavel",
      "B-": "alerta",
      "O+": "estavel",
      "O-": "alerta"
    },
    "unidade": null,
    "url": "https://www.doesanguedoevida.com.br/banco-de-sangue-sao-paulo-jd-paulista"
  }
]
```

### Filtrar pela cidade

### Listar todos os bancos de sangue de determinada cidade

`/v1/?cidade=recife`

#### Request

```shell
curl -i -H 'Accept: application/json' http://127.0.0.1:5000?cidade=recife
```

#### Response

```json
[
   {
    "banco": "HEMOPE",
    "cidade": "Recife",
    "data_extracao": "Sat, 01 Jan 2022 02:51:56 GMT",
    "endereco": "RUA JOAQUIM NABUCO, 171 - CEP 52.011-900 - GRA\u00c7AS, RECIFE",
    "estado": "PE",
    "sangue": {
      "A+": "critica",
      "A-": "critica",
      "AB+": "critica",
      "AB-": "estavel",
      "B+": "critica",
      "B-": "alerta",
      "O+": "critica",
      "O-": "critica"
    },
    "unidade": null,
    "url": "http://www.hemope.pe.gov.br/"
  }
]
```
### Filtrar pelo estado

### Listar todos os bancos de sangue de determinado Estado

`/v1/?estado=PE`

#### Request

```shell
curl -i -H 'Accept: application/json' http://127.0.0.1:5000?estado=PE
```

#### Response

```json
[
   {
    "banco": "HEMOPE",
    "cidade": "Recife",
    "data_extracao": "Sat, 01 Jan 2022 02:51:56 GMT",
    "endereco": "RUA JOAQUIM NABUCO, 171 - CEP 52.011-900 - GRA\u00c7AS, RECIFE",
    "estado": "PE",
    "sangue": {
      "A+": "critica",
      "A-": "critica",
      "AB+": "critica",
      "AB-": "estavel",
      "B+": "critica",
      "B-": "alerta",
      "O+": "critica",
      "O-": "critica"
    },
    "unidade": null,
    "url": "http://www.hemope.pe.gov.br/"
  }
]
```
### Filtrar pelo banco de sangue

### Listar todos os bancos de sangue de determinado banco de sangue

`/?banco=hemope`

#### Request

```shell
curl -i -H 'Accept: application/json' http://127.0.0.1:5000?banco=HEMOPE
```

#### Response

```json
[
   {
    "banco": "HEMOPE",
    "cidade": "Recife",
    "data_extracao": "Sat, 01 Jan 2022 02:51:56 GMT",
    "endereco": "RUA JOAQUIM NABUCO, 171 - CEP 52.011-900 - GRA\u00c7AS, RECIFE",
    "estado": "PE",
    "sangue": {
      "A+": "critica",
      "A-": "critica",
      "AB+": "critica",
      "AB-": "estavel",
      "B+": "critica",
      "B-": "alerta",
      "O+": "critica",
      "O-": "critica"
    },
    "unidade": null,
    "url": "http://www.hemope.pe.gov.br/"
  }
]
```
### Listar os bancos de sangue cadastrados

### Lista todos os bancos de sangue cadastrados

`/bancos-cadastrados/`

#### Request

```shell
curl -i -H 'Accept: application/json' http://127.0.0.1:5000/bancos-cadastrados/
```

#### Response

```json
[
  {
    "banco": "HEMOPE", 
    "cidade": "Recife", 
    "endereco": "RUA JOAQUIM NABUCO, 171 - CEP 52.011-900 - GRA\u00c7AS, RECIFE", 
    "estado": "PE", 
    "unidade": null, 
    "url": "http://www.hemope.pe.gov.br/"
  }, 
  {
    "banco": "HEMATO", 
    "cidade": "Recife", 
    "endereco": "Rua Dom B\u00f4sco, 723  - Boa Vista", 
    "estado": "PE", 
    "unidade": null, 
    "url": "https://www.doesanguedoevida.com.br/banco-de-sangue-hemato"
  }
]
```

### Filtrar pelo estado

### Listar todos os bancos de sangue de determinado Estado

`/bancos-cadastrados/?estado=PE`

#### Request

```shell
curl -i -H 'Accept: application/json' http://127.0.0.1:5000/bancos-cadastrados/?estado=PE
```

#### Response

```json
[
   {
    "banco": "HEMOPE",
    "cidade": "Recife",
    "endereco": "RUA JOAQUIM NABUCO, 171 - CEP 52.011-900 - GRA\u00c7AS, RECIFE",
    "estado": "PE",
    "unidade": null,
    "url": "http://www.hemope.pe.gov.br/"
  }
]
```

### Filtrar pela cidade

### Listar todos os bancos de sangue de determinado Estado

`/bancos-cadastrados/?cidade=recife`

#### Request

```shell
curl -i -H 'Accept: application/json' http://127.0.0.1:5000/bancos-cadastrados/?cidade=recife
```

#### Response

```json
[
   {
    "banco": "HEMOPE",
    "cidade": "Recife",
    "endereco": "RUA JOAQUIM NABUCO, 171 - CEP 52.011-900 - GRA\u00c7AS, RECIFE",
    "estado": "PE",
    "unidade": null,
    "url": "http://www.hemope.pe.gov.br/"
  }
]
```
