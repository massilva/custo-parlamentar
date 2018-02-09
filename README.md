Criar ambiente de Desenvolvimento
=================================

Requisitos:

- Python 3.5+
- Virtualenv
- Postgresql==9.6

**º - Crie uma pasta para projetos e entrar nela.**

`mkdir Projetos`

`cd Projetos`

**º - Instalar o virtualenv**

`pip install virtualenv`

**º - Criar a pasta para ambientes de desenvolvimento dentro da pasta Projetos e entrar nela.**

`mkdir Environments`

`cd Environments`

**º - Dentro da pasta Environments criar um environment de Python 3.**

`virtualenv -p python3 deputados`

*Se a versão padrão do Python for a 3, não é preciso especificar no comando*

`virtualenv deputados`

**º - Ativar o environment.**

*Unix*

`source deputados/bin/activate`

*Windows*

`deputados\Scripts\activate`

**º - Clonar o repositório dentro da pasta de Projetos.**

`cd ../../`

`git clone https://gitlab.com/edelygomes/deputados.git`


**º - Entrar na pasta do projeto e instalar os requirements.**

`pip install -r requirements`


**º - Entrar no psql e cria usuário 'alba' e banco de dados 'assembleia'.**

*Entra no cli do Postresql*

`psql -U postgres`

*Cria usuário alba*

`postgres=# create user alba with password '123456';`

*Cria banco de dados assembleia*

`postgres=# create database assembleia;`

**º - Após sair da CLI do Posgresql, importar banco de dados.**

`psql -h localhost -p 5432 -U postgres -f assembleia.sql assembleia`

**º - Rodar as migrations.**

`python manage.py migrate`

