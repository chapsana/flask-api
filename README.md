<h1 align="center">flask-api 👋</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a><img src="https://github.com/alphaolomi/flask-api/workflows/Flask%20CI/badge.svg"/></a>
  <a href="https://github.com/alphaolomi/flask-api#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/alphaolomi/flask-api/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/alphaolomi/flask-api/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/alphaolomi/flask-api" />
  </a>
  <a href="http://commitizen.github.io/cz-cli/" target="_blank">
    <img alt="Commitizen friendly" src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg" />
    </a>
</p>

<br />

A minimal REST API made using Flask & SQL Alchemy. Products API using Python Flask, SQL Alchemy and Marshmallow.

<p align="center" style="text-decoration:italic;">
Made with ❤️ using
<a href="https://www.palletsprojects.com/p/flask/">Flask Framework</a>
</p>
<br />

###  Links

🏠 [Homepage](https://github.com/alphaolomi/flask-api#readme)


## Dashboard Features:

- REST API
- SQLite database
- SQLAlchemy ORM

<br />

## Build from sources

```bash
# Clone the sources

# Virtualenv modules installation (Windows based systems)
# virtualenv --no-site-packages env
# .\env\Scripts\activate.bat
# Virtualenv modules installation (Unix based systems)
virtualenv --no-site-packages env
source env/bin/activate
```
```sh
# Install requirements
pip3 install -r requirements.txt
```

```sh
# Set the FLASK_APP environment variable
# (Unix/Mac) export FLASK_APP=run.py
# (Windows) set FLASK_APP=run.py
# (Powershell) $env:FLASK_APP = ".\run.py"
export FLASK_APP=run.py


```sh
# Set up the DEBUG environment
# (Unix/Mac) export FLASK_ENV=development
# (Windows) set FLASK_ENV=development
# (Powershell) $env:FLASK_ENV = "development"
export FLASK_ENV=development
```

```sh
# Run the application
# --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
# --port=5000    - specify the app port (default 5000)
flask run --host=0.0.0.0 --port=5000

# Access the app in browser: http://127.0.0.1:5000/
```

<br />

## Endpoints

- **GET** `/products`
- **GET** `/products/:id`
- **POST**`/products`
- **PUT** `/products/:id`
- **DELETE** `/products/:id`

## Deployment

The app has a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

<br />

### [Docker](https://www.docker.com/) execution

---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
cd flask-api
```

> Start the app in Docker

```bash
sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

<br />

### [Gunicorn](https://gunicorn.org/)

---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
pip install gunicorn
```

> Start the app using gunicorn binary

```bash
gunicorn --bind 0.0.0.0:8001 run:app
# Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)

---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
pip install waitress
```

> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
waitress-serve --port=8001 run:app
# Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Credits & Links

- 👤 **Alpha Olomi** - Website: https://alphaolomi.me  Github: [@alphaolomi](https://github.com/alphaolomi)
- [All Contributors][link-contributors]

## Testing

```bash
pytest test
```

## Contributing <img src="https://img.shields.io/badge/PR-welcome-yellow" />

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/alphaolomi/flask-api/issues). You can also take a look at the [contributing guide](https://github.com/alphaolomi/flask-api/blob/master/CONTRIBUTING.md).


## Security 

If you discover any security related issues, please email [alphaolomi@gmail.com](mailto:alphaolomi@gmail.com) instead of using the issue tracker.


## Show your support

Give a ⭐️ if this project helped you!


## 📝 License

Copyright © 2020 [Alpha Olomi](https://github.com/alphaolomi).<br />
This project is [MIT](https://github.com/alphaolomi/flask-api/blob/master/LICENSE) licensed.


[link-author]: https://github.com/alphaolomi
[link-contributors]: ../../contributors
