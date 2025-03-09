![Main Foodgram workflow ](https://github.com/sonjpog/foodgram/actions/workflows/main.yml/badge.svg)

#  Foodgram

Foodgram, «Продуктовый помощник». Онлайн-сервис и API для него. На этом сервисе пользователи публикуют свои рецепты, подписываются на публикации других пользователей, добавляют понравившиеся рецепты в список «Избранное», а перед походом в магазин могут скачать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

IP проекта: 89.169.168.95

Домен проекта: https://sonyapgsn.ru/

Email для логина суперюзера: sonyapgsn@gmail.com

Пароль для логина суперюзера: Foodgram2025


## Развернуть проект на удаленном сервере:

### Клонировать репозиторий:

```yaml
https://github.com/sonjpog/foodgram.git
```

### Установить на сервере Docker, Docker Compose:

```yaml
sudo apt install curl                                   - установка утилиты для скачивания файлов
curl -fsSL https://get.docker.com -o get-docker.sh      - скачать скрипт для установки
sh get-docker.sh                                        - запуск скрипта
sudo apt-get install docker-compose-plugin              - последняя версия docker compose
```

### Скопировать на сервер файлы docker-compose.yml, nginx.conf из папки infra (команды выполнять находясь в папке infra):

```yaml
scp docker-compose.yml nginx.conf username@IP:/home/username/

# username - имя пользователя на сервере
# IP - публичный IP сервера
```

### Для работы с GitHub Actions необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:

```yaml
DOCKER_PASSWORD - пароль от Docker Hub
DOCKER_REPOSITORY - имя пользователя в GitHub
DOCKER_USERNAME - имя пользователя Docker Hub
HOST - ip сервера
SSH_KEY - ключ ssh для доступа к удаленному серверу
SSH_PASSPHRASE - пароль ssh
TELEGRAM_TO - id пользователя TELEGRAM
TELEGRAM_TOKEN - TELEGRAM токен
USER - имя пользователя сервера
```

### Создать и запустить контейнеры Docker, выполнить команду на сервере (версии команд «docker compose» или «docker-compose» отличаются в зависимости от установленной версии Docker Compose):

```yaml
sudo docker compose up -d
```

### Выполнить миграции:

```yaml
sudo docker compose exec backend python manage.py migrate
```

### Для остановки контейнеров Docker:

```yaml
sudo docker compose down -v      - с их удалением
sudo docker compose stop         - без удаления
```

### После каждого обновления репозитория (push в ветку master) будет происходить:

1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
2. Сборка и доставка докер-образов frontend и backend на Docker Hub
3. Разворачивание проекта на удаленном сервере
4. Отправка сообщения в Telegram в случае успеха

## Локальный запуск проекта:

### Склонировать репозиторий к себе

```yaml
git@github.com:sonjpog/Foodgram.git
```

### В директории infra создать файл .env и заполнить своими данными:

```yaml
POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django

DB_HOST=db
DB_PORT=5432
```

### Создать и запустить контейнеры Docker, как указано выше.

После запуска проект будут доступен по адресу: http://localhost/

Документация будет доступна по адресу: http://localhost/api/docs/

## Стек технологий

![django](https://camo.githubusercontent.com/5cc076a62f7189d22260996c9bec5ca6eef5e5b537f62e64b68e3028d0de29b5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f6c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465) ![postgresql](https://camo.githubusercontent.com/0c918464c578d8cd8f9be93baaabc8e84b94d8f03efe4e3f18799e2c3de395f8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f737467726553514c2d3333363739313f6c6f676f3d706f737467726573716c266c6f676f436f6c6f723d7768697465) ![Nginx](https://camo.githubusercontent.com/cd6eba769dc7617401e02baea47325fdd47b841c920acccca94f411020f9d507/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e67696e782d3030393633393f6c6f676f3d6e67696e78266c6f676f436f6c6f723d7768697465) ![Docker](https://camo.githubusercontent.com/0bba72db052794db7b917abda181702a7af7d352e704868f8b0eef45304d7dcf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3234393645443f6c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465) ![GitHubActions](https://camo.githubusercontent.com/46ced4d91ace1d06b77689c0ba6d10688b02219fef3f21dfe8b0a95067ad16cf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875625f416374696f6e732d3230383846463f6c6f676f3d6769746875622d616374696f6e73266c6f676f436f6c6f723d7768697465)


Работу выполнила [Софья Погосян](https://github.com/sonjpog)
