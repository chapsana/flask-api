# Flask App API

<br />

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![Software License][ico-license]](LICENSE.md)
![Build Status][ico-travis]

<br />

A minimal REST API made using Flask & SQL Alchemy. Products API using Python Flask, SQL Alchemy and Marshmallow.

<br />

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

# Install requirements
pip3 install -r requirements.txt

# Set the FLASK_APP environment variable
# (Unix/Mac) export FLASK_APP=run.py
# (Windows) set FLASK_APP=run.py
# (Powershell) $env:FLASK_APP = ".\run.py"
export FLASK_APP=run.py

# Set up the DEBUG environment
# (Unix/Mac) export FLASK_ENV=development
# (Windows) set FLASK_ENV=development
# (Powershell) $env:FLASK_ENV = "development"
export FLASK_ENV=development

# Run the application
# --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
# --port=5000    - specify the app port (default 5000)
flask run --host=0.0.0.0 --port=5000
# Access the app in browser: http://127.0.0.1:5000/
```

<br />

## Endpoints

- GET `/products`
- GET `/products/:id`
- POST`/products`
- PUT `/products/:id`
- DELETE `/products/:id`

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

- **Alpha Olomi** [alphaolomi@gmail.com](alphaolomi@gmail.com)
- [Flask Framework](https://www.palletsprojects.com/p/flask/)
- [All Contributors][link-contributors]

## Testing

```bash
pytest test
```

## Contributing

Pull requests are welcome. Please see [CONTRIBUTING](./.github/CONTRIBUTING.md) and [CODE_OF_CONDUCT](./.github/CODE_OF_CONDUCT.md) for details.

## Security

If you discover any security related issues, please email [alphaolomi@gmail.com](mailto:alphaolomi@gmail.com) instead of using the issue tracker.

## License

MIT License. Please see [License File](LICENSE) for more information.

[ico-license]: https://img.shields.io/badge/license-Apache2-brightgreen.svg?style=flat-square
[ico-travis]: https://img.shields.io/travis/alphaolomi/wazo/master.svg?style=flat-square
[link-author]: https://github.com/alphaolomi
[link-contributors]: ../../contributors
