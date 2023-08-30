# Projeto do curso de Análise e Desenvolvimento de Sistemas pela FATEC.

## Máterias abordadas ##
-
-
-

## Como utilizar? ##

**:warning: Warning:** É necessário ter o Docker instalado:
- 🐳 [Docker Engine Installation](https://docs.docker.com/engine/install/ubuntu/)  
- 🐳 [Docker Compose Installation](https://docs.docker.com/compose/install/)  
- **💡 Tip:** [For any doubts please use Docker documentation](https://docs.docker.com/)  

### Utilizando a aplicação

Após instalar o Docker e o Docker-compose, abar um terminal e execute:

```sh
sudo docker-compose up
```
Para acessar a aplicação, abra uma nova aba no seu terminal e execute:

```sh
sudo docker-compose run --rm web bash
```

#### Rodar o banco de dados

```sh
sudo docker-compose run -d postgres
```

Para resetar a aplicação, execute:

```sh
docker-compose down && docker-compose up
```

#### Rodar migrações

```sh
sudo docker-compose run --rm web python manage.py makemigrations
sudo docker-compose run --rm web python manage.py migrate
```

#### Acessar o Shell

```sh
sudo docker-compose run --rm web python manage.py shell
```

#### Carregar dados iniciais da aplicação
```sh
sudo docker-compose run --rm web python manage.py populate_db
```

#### Criar superuser

```sh
sudo docker-compose run --rm web python manage.py createsuperuser
```

#### Criar fixtures
```sh
sudo docker-compose run --rm web ./create_fixtures
```

#### Recriar e Popular banco
```sh
sudo docker-compose run --rm db ./populate_db
```

### Permissões de arquivos ###
Quando se cria arquivos dentro de um contâiner Docker eles irão pertencer ao contâiner, para mudar a permissão rode o seguinte comando:

```sh
sudo chown -R $USER:$USER .
```

## Referências ##
[1° Django + Docker](https://github.com/claudimf/django-docker)  
[2° Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)  
[3° How to provide initial data for models](https://docs.djangoproject.com/en/4.0/howto/initial-data/)  
[4° Django: setup básico com Bootstrap](https://dev.to/thalesbruno/django-projeto-generico-com-bootstrap-3d86)  
