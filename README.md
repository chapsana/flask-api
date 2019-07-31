<h1 align="center">REST API in Flask</h1>

A minimal REST API made using Flask & SQL Alchemy. Products API using Python Flask, SQL Alchemy and Marshmallow

> Under light developemnt

## Quick Start
Using Pipenv shell managerand pip package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.


### Usage

```bash
# Activate venv
pipenv shell

# Install dependencies
pipenv install
```

```bash
# Create DB
python
from app import db
db.create_all()
exit()

# Run Server (http://localhst:5000)
python app.py
```

## Endpoints

- GET /product
- GET /product/:id
- POST /product
- PUT /product/:id
- DELETE /product/:id



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Author

Alpha Olomi ☺ [hello@alphaolomi.com](mailto:hello@alphaolomi.com)

## License
[MIT](https://choosealicense.com/licenses/mit/) License
