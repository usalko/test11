<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.biacorp.ru/itm23/service-back">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Test11</h3>

  <p align="center">
    Response to the question: [Fast API + Apache Airflow in Docker](https://stackoverflow.com/questions/69219633/fast-api-apache-airflow-in-docker)
    <br />
    <a href="https://github.com/usalko/test11/-/blob/dev/documentation/index.md?ref_type=heads"><strong>Просмотр документов »</strong></a>
    <br />
    <br />
    <a href="https://test11.qstand.art">View demo</a>
    ·
    <a href="https://github.com/usalko/test11/issues/new?labels=bug&template=bug-report---.md">Новый баг</a>
    ·
    <a href="https://github.com/usalko/test11/issues/new?labels=enhancement&template=feature-request---.md">Новая фича</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Сводная информация о проекте</a>
      <ul>
        <li><a href="#built-with">Стек технологий</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Начало разработки</a>
      <ul>
        <li><a href="#prerequisites">Пререквизиты</a></li>
        <li><a href="#installation">Установка</a></li>
      </ul>
    </li>
    <li><a href="#usage">Использование</a></li>
    <li><a href="#roadmap">Дорожная карта</a></li>
    <li><a href="#contributing">Вклад</a></li>
    <li><a href="#contact">Контакты</a></li>
    <li><a href="#acknowledgments">Ссылки</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
<a name="about-the-project"></a> 
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://service.biacorp.ru)

A prototype "Fast API + Apache Airflow in Docker".

Goals of making prototype "Fast API + Apache Airflow in Docker":
* Skills demonstration

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="built-with"></a>
### Built With

FastAPI, Apache Airflow.

* [Django][Django-url]
* [Postgres][Postgres-url]
* [Kafka][Kafka-url]
* [Redis][Redis-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
<a name="getting-started"></a> 
## Getting Started

Development takes place in any IDE suitable for editing files and running commands from the command line. Developers actively use two development environments: Visual Studio Code, Pycharm.

<a name="prerequisites"></a>
### Prerequisites

- docker-compose
- Linux terminal  (WSL/Bash для Windows)

<a name="installation"></a>
### Installation

#### then all commands are executed in Linux 
#### the commands may differ, for example, some distributions use docker-compose and not docker compose

1. Primary assembly :


```
./buildew
```

after the initial assembly you need to add an argument, for example

```
./buildew restart
```

or

```
./buildew run
```

2. Working with Docker :

after the initial build, you (maybe) will be more comfortable using docker

```
docker compose up 
```

and for rebuilding images after changes

```
docker compose up --build
```

3. Setup Environment and Migration Variables :

After launching the orchestra, most likely, errors related to the chat token will appear in the log

to do this, install the telegram bot token in .env.dev, you can take it from BotFather (find the original)

(as an example)
```
CHAT_BOT_TOKEN=000000000:dwkLKNewdnwbuhbsaKJBDSD11enka
```

Next, you need to go into the keeper container from a new terminal (or with the -d flag in docker) and perform migrations

do with working docker compose!

```
docker compose exec -it keeper bash
```

### working in a container

```
cd service
```

```
python manage.py migrate
```

### end of work in container


4. Tips to make your work easier :

To view logs only for the main application, you can use this command

```
docker compose up (optionally --build) --attach service
```

instead of service, you can specify the container for which you want to view logs

you can use psql to work with the database

```
docker compose exec -it pg psql -U service -d service
```

but I would recommend using something like dbeaver



<!-- USAGE EXAMPLES -->
<a name="usage"></a> 
## Usage

Разворачивание на dev и pre-prod стендах осуществляется через [ci встроенный в github](https://github.com/usalko/test11/pipelines).

Полный список переменных окружения, можно посмотреть в [документации](documentation/index.md).


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
<a name="roadmap"></a>
## Дорожная карта

- [ ] Создание прототипа для запуска пользовательского тестирования

См. [открытые задачи](https://github.biacorp.ru/itm32/service-front/issues) для полного списка предлагаемых фич (и найденых дефектов/багов).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
<a name="contributing"></a>
## Вклад

Вклад в разработку, это то что делает наше небольшое сообщество разработчиков, таким потрясающим местом для обучения, вдохновления и создания нового смысла и значения для наших пользователей. Все ваши вклады  **высоко ценятся**.

Разработка осуществляется в соответствии с базовыми стилевыми соглашениями по оформлению кода (pep8), если у вас есть предложения по улучшению процесса разработки или кода, делайте форк проекта и кидайте merge request или просто [заводите задачи](https://github.biacorp.ru/itm32/service-front/issues) с тегом "enhancement".
Не забудьте кинуть звездочку на проект! Спасибо, спасибо!

1. Форк проекта
2. Создай свою фичу (ветку) (`git checkout -b feature/AmazingFeature`)
3. Комить изменения (`git commit -m 'Add some AmazingFeature'`)
4. Сделай пуш бранча (`git push origin feature/AmazingFeature`)
5. Открой пул реквест

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
<a name="contact"></a>
## Контакты

Ссылка на проект: [https://github.biacorp.ru/itm32/service-back](https://github.biacorp.ru/itm32/service-back)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<a name="acknowledgments"></a>
## Ссылки

Список полезных ссылок

* [PEP8 reference](https://peps.python.org/pep-0008/)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [github Flavored Markdown (GLFM)](https://docs.github.com/ee/user/markdown.html)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
[Django-url]: https://docs.djangoproject.com/en/4.2/
[Postgres-url]: https://www.postgresql.org/docs/15/index.html
[Kafka-url]: https://kafka.apache.org/documentation
[Redis-url]: https://redis.io/

