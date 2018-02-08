Criar ambiente de Desenvolvimento
=================================

Requisitos:

- Python 3.5+
- Virtualenv
- Django 2.0+

**º - Crie uma pasta para projetos.**

*Unix*

`mkdir -p Projetos`

*Windows*


**º - Instalar o virtualenv**

*Unix*

`pip install virtualenv`

*Window*

**º - Criar a pasta para ambientes de desenvolvimento dentro da pasta Projetos.**

*Unix*

`mkdir Projetos/Environments`

*Windows*

**º - Dentro da pasta Environments criar um environment de Python 3.**

*Unix*

`virtualenv -p python3 deputados`

*Windows*

**º - Ativar o environment.**

*Unix*

`source ~/Documentos/Projetos/deputados/bin/activate`

**º - Clonar o repositório dentro da pasta de Projetos.**

`git clone https://gitlab.com/edelygomes/deputados.git`


**º - Entrar na pasta do projeto e instalar os requirements.**

`pip install -r requirements`

