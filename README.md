# Products API

A minimal REST API made using Flask & SQL Alchemy. Products API using Python Flask, SQL Alchemy and Marshmallow

> Undre devlopemnt

## Quick Start

Using Pipenv shell manager

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

## Author

Alpha OLomi
