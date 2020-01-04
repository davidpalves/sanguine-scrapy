![doe sangue](assets/icon.svg)

# Doe Sangue Scraping Tool

Ferramenta de monitoramento de estoque dos bancos de sangue do estado de Pernambuco.

## Bancos de sangue pesquisados

- [HEMOPE - Recife](http://www.hemope.pe.gov.br)
- [HEMATO - Recife](https://doesanguedoevida.com.br/doar-sangue-recife)

## Instruções para executar o projeto

- [Requerimentos do Projeto](https://github.com/DavidPierre21/doe-sangue-scrapy#requerimentos-para-o-projeto)
- [Instalando os requerimentos para o projeto](https://github.com/DavidPierre21/doe-sangue-scrapy#instalando-os-requerimentos-para-o-projeto)
- [Configuração do MongoDB](https://github.com/DavidPierre21/doe-sangue-scrapy#configurando-mongodb)
- [Execução do projeto](https://github.com/DavidPierre21/doe-sangue-scrapy#instru%C3%A7%C3%B5es-para-execu%C3%A7%C3%A3o-do-projeto)

### Requisitos

1. [Python 3](https://www.python.org/)
2. [Mongodb](https://www.mongodb.com/)
3. [Pymongo](https://api.mongodb.com/python/current/)
4. [Python Decouple](https://github.com/henriquebastos/python-decouple)
5. [Scrapy](https://scrapy.org/)

#### Instalando os requisitos do projeto

- A versão utilizada de Python foi a 3.6.7.

```bash
pip install -r requirements.txt
```

### Configurando MongoDB

O projeto usa um database chamado "doe_sangue" e uma collections chamado "niveis"
O servidor do database esta configurado para o localhost e na porta 27017

Antes de tudo, o serviço do MongoDB deve estar rodando, no Linux, utilize:

```bash
sudo service start mongod
```

Caso queira verificar o status do serviço

```bash
sudo service status mongod
```

Para abrir o shell do Mongo, podemos utilizar:

```bash
mongo
```

ou, para o modo "silencioso"

```bash
mongo --quiet
```

Para selecionar o database a ser utilizado

```bash
use doe_sangue;
```

Crie a collection niveis:

```bash
db.createCollection("niveis");
```

[Depois de executar a spider, para visualizar o dataset, utilize o comando:](https://github.com/DavidPierre21/doe-sangue-scrapy#instru%C3%A7%C3%B5es-para-execu%C3%A7%C3%A3o-do-projeto)

```bash
db.niveis.find();
```

e caso queira exportar para json, fora do shell do Mongodb, utilize:

```bash
mongoexport --db doe_sangue --collection niveis --out niveis.json
```

#### Instruções para execução do projeto

1. Clone o repositório

   ```bash
   git clone https://github.com/DavidPierre21/doe-sangue-scrapy.git
   ```

2. Navegue até o diretório do projeto

   ```bash
   cd doe_sangue
   ```

3. Finalmente, execute, passando como argumento o banco de sangue a ser buscado:

   ```bash
   scrapy crawl hemope
   ```

##### Executando todas as spiders

Há duas opções para utilização, caso queira utilizar o script em python, rode:

```bash
make py.crawl
```

Para utilizar o script em shell, utilize:

```bash
make list.crawl
```
