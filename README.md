# Scraping Doe Sangue

### Projeto feito para raspar niveis de sangue dos bancos de sangue de Recife

------------------------------------------------------

#### Sites raspados:
* [HEMOPE - Recife](http://www.hemope.pe.gov.br)
* [HEMATO - Recife](https://doesanguedoevida.com.br/doar-sangue-recife)

------------------------------------------------------

#### Links para instruções do projeto
* [Requerimentos do Projeto](https://github.com/DavidPierre21/doe-sangue-scrapy#requerimentos-para-o-projeto)
* [Instalando os requerimentos para o projeto](https://github.com/DavidPierre21/doe-sangue-scrapy#instalando-os-requerimentos-para-o-projeto)
* [Configuração do MongoDB](https://github.com/DavidPierre21/doe-sangue-scrapy#configurando-mongodb)
* [Execução do projeto](https://github.com/DavidPierre21/doe-sangue-scrapy#instru%C3%A7%C3%B5es-para-execu%C3%A7%C3%A3o-do-projeto)

------------------------------------------------------

#### Requerimentos para o projeto
1. [Python 3](https://www.python.org/)
2. [Mongodb](https://www.mongodb.com/)
3. [Pymongo](https://api.mongodb.com/python/current/)
4. [Psycopg2](https://pypi.org/project/psycopg2/)
5. [Python Decouple](https://github.com/henriquebastos/python-decouple)
6. [Scrapy](https://scrapy.org/)
7. [PostgreSQL](https://www.postgresql.org/)


#### Instalando os requerimentos para o projeto
* A versão utilizada de Python foi a 3.6.7.

* A versão utilizada do PostgreSQL foi a 9.4.20

Algumas dependencias do projeto podem ser instaladas utilizando o arquivo requirements.txt:
```
pip install -r requirements.txt
```

------------------------------------------------------

#### Configurando MongoDB
O projeto usa um database chamado "doe_sangue" e uma collections chamado "niveis"
O servidor do database esta configurado para o localhost e na porta 27017

Antes de tudo, o serviço do MongoDB deve estar rodando, no Linux, utilize:
```
sudo service start mongod
```

Caso queira verificar o status do serviço
```
sudo service status mongod
```

------------------------------------------------------
Para abrir o shell do Mongo, podemos utilizar:

```
mongo
```

ou, para o modo "silencioso"
```
mongo --quiet
```

Para selecionar o database a ser utilizado
```
use doe_sangue;
```

Crie a collection niveis:
```
db.createCollection("niveis");
```

#### [Depois de executar a spider, para visualizar o dataset, utilize o comando:](https://github.com/DavidPierre21/doe-sangue-scrapy#instru%C3%A7%C3%B5es-para-execu%C3%A7%C3%A3o-do-projeto)
```
db.niveis.find();
```

e caso queira exportar para json, fora do shell do Mongodb, utilize:
```
mongoexport --db doe_sangue --collection niveis --out niveis.json 
```

------------------------------------------------------

#### Instruções para execução do projeto

1. Clone o repositório
```
git clone https://github.com/DavidPierre21/doe-sangue-scrapy.git
```

2. Navegue até o diretório do projeto
```
cd doe_sangue
```

3. Finalmente, execute, passando como argumento o banco de sangue a ser buscado:
```
scrapy crawl hemope
```
