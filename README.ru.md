<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/usalko/test11">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Test11</h3>

  <p align="center">
    Ответ на вопрос: [Fast API + Apache Airflow in Docker](https://stackoverflow.com/questions/69219633/fast-api-apache-airflow-in-docker)
    <br />
    <a href="https://github.com/usalko/test11/-/blob/dev/documentation/index.md?ref_type=heads"><strong>Просмотр документов »</strong></a>
    <br />
    <br />
    <a href="https://test11.qstand.art">Просмотр демо</a>
    ·
    <a href="https://github.com/usalko/test11/issues/new?labels=bug&template=bug-report---.md">Новый баг</a>
    ·
    <a href="https://github.com/usalko/test11/issues/new?labels=enhancement&template=feature-request---.md">Новая фича</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Оглавление</summary>
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
## Сводная информация о проекте

[![Product Name Screen Shot][product-screenshot]](https://cargo.biacorp.ru)

Проект бэкенда для прототипа "BIA Грузоотправитель" предоставляет АПИ для веб и мобильного приложений, а также обеспечивает интеграцию со сторонними сервисами (телеграмм, traffic.online)

Цели создания прототипа "BIA Грузоотправитель":
* Решение позволяющее в едином окне вести реестр заявок, подбирать исполнителей по заданным параметрам, отправлять заявки на биржи и отслеживать статус исполнения заказов

<p align="right">(<a href="#readme-top">назад наверх</a>)</p>


<a name="built-with"></a>
### Стек технологий

Django, Postgres, Kafka, Redis.

* [Django][Django-url]
* [Postgres][Postgres-url]
* [Kafka][Kafka-url]
* [Redis][Redis-url]


<p align="right">(<a href="#readme-top">назад наверх</a>)</p>



<!-- GETTING STARTED -->
<a name="getting-started"></a> 
## Начало разработки

Разработка происходит в любой IDE пригодной для редактирования файлов и запуска команд из командной строки. Активно, разработчиками используются две среды разработки: Visual Studio Code, Pycharm.

<a name="prerequisites"></a>
### Пререквизиты

- docker-compose
- Linux terminal  (WSL/Bash для Windows)

<a name="installation"></a>
### Установка

#### далее все команды выполняются в linux 
#### команды могут отличаться, к примеру в некоторых дистрибутивах используется docker-compose а не docker compose

1. Первичная сборка :


```
./buildew
```

после первичной сборки надо добавлять аргумент, к примеру

```
./buildew restart
```

или

```
./buildew run
```

2. Работа с докером :

после первичной сборки вам (возможно) будет удобнее пользоваться docker

```
docker compose up 
```

и для пересборки образов после изменения

```
docker compose up --build
```

3. Настройка переменных окружения и миграции :

после запуска оркестра, скорее всего, в логе будут вылетать ошибки, связанные с чат токеном

для этого установите токен бота телеграм в .env.dev, его можно взять в BotFather(найти оригинал)

(как пример)
```
CHAT_BOT_TOKEN=000000000:dwkLKNewdnwbuhbsaKJBDSD11enka
```

далее вам надо из нового терминала (или же с флагом -d в docker) зайти в контейнер keeper и выполнить миграции

делать при рабочем docker compose!


```
docker compose exec -it keeper bash
```

### работа в контейнере 

```
cd service
```

```
python manage.py migrate
```

### конец работы в контейнере 


4. Советы по упрощению работы :

для просмотра логов только по основному приложению можно использовать такую команду 

```
docker compose up (опционно --build) --attach cargo
```

вместо cargo можно указать контейнер по которому хотите просматривать логи

для работы с бд можно использовать psql

```
docker compose exec -it pg psql -U cargo -d cargo
```

но я бы рекомендовал использовать что то вроде dbeaver




<!-- USAGE EXAMPLES -->
<a name="usage"></a> 
## Использование

Разворачивание на dev и pre-prod стендах осуществляется через [ci встроенный в gitlab](https://gitlab.biacorp.ru/itm23/cargo-back/pipelines).

Полный список переменных окружения, можно посмотреть в [документации](documentation/index.md).


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
<a name="roadmap"></a>
## Дорожная карта

- [ ] Создание прототипа для запуска пользовательского тестирования

См. [открытые задачи](https://gitlab.biacorp.ru/itm32/cargo-front/issues) для полного списка предлагаемых фич (и найденых дефектов/багов).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
<a name="contributing"></a>
## Вклад

Вклад в разработку, это то что делает наше небольшое сообщество разработчиков, таким потрясающим местом для обучения, вдохновления и создания нового смысла и значения для наших пользователей. Все ваши вклады  **высоко ценятся**.

Разработка осуществляется в соответствии с базовыми стилевыми соглашениями по оформлению кода (pep8), если у вас есть предложения по улучшению процесса разработки или кода, делайте форк проекта и кидайте merge request или просто [заводите задачи](https://gitlab.biacorp.ru/itm32/cargo-front/issues) с тегом "enhancement".
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

Ссылка на проект: [https://gitlab.biacorp.ru/itm32/cargo-back](https://gitlab.biacorp.ru/itm32/cargo-back)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<a name="acknowledgments"></a>
## Ссылки

Список полезных ссылок

* [PEP8 reference](https://peps.python.org/pep-0008/)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [GitLab Flavored Markdown (GLFM)](https://docs.gitlab.com/ee/user/markdown.html)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
[Django-url]: https://docs.djangoproject.com/en/4.2/
[Postgres-url]: https://www.postgresql.org/docs/15/index.html
[Kafka-url]: https://kafka.apache.org/documentation
[Redis-url]: https://redis.io/

