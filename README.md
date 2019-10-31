# REST API in Flask [![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/) [![Software License][ico-license]](LICENSE.md) ![Build Status][ico-travis]

A minimal REST API made using Flask & SQL Alchemy. Products API using Python Flask, SQL Alchemy and Marshmallow.

## Quick Start

Using Pipenv shell managerand pip package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

### Getting started

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

- GET `/product`
- GET `/product/:id`
- POST`/product`
- PUT `/product/:id`
- DELETE `/product/:id`

## Changelog

Please see [CHANGELOG](CHANGELOG.md) for more information what has changed recently.

## Testing

```bash
$ pytest test
```

## Contributing

Pull requests are welcome. Please see [CONTRIBUTING](./.github/CONTRIBUTING.md) and [CODE_OF_CONDUCT](./.github/CODE_OF_CONDUCT.md) for details.

## Security

If you discover any security related issues, please email [hello@alphaolomi.com](mailto:hello@alphaolomi.com) instead of using the issue tracker.

## Credits

- **Alpha Olomi** [hello@alphaolomi.com](hello@alphaolomi.com)
- [All Contributors][link-contributors]

## License

The Apache 2 License. Please see [License File](LICENSE) for more information.

[ico-license]: https://img.shields.io/badge/license-Apache2-brightgreen.svg?style=flat-square
[ico-travis]: https://img.shields.io/travis/alphaolomi/wazo/master.svg?style=flat-square
[link-author]: https://github.com/alphaolomi
[link-contributors]: ../../contributors
