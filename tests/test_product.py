from app import app
# import app

# with app.test_client() as c:
#     rv = c.post('/products', json={"name": "samaki","description": "a good fish","price": "2000","qty": "2"})
#     json_data = rv.get_json()
#     #  assert rv.status_code == 200
#     assert rv.status_code == 200
#     # assert json(email, json_data['token'])

from flask import json

def test_fetching_products():        
    response = app.test_client().post(
        '/products',
        data=json.dumps({"name": "samaki","description": "a good fish","price": "2000","qty": "2"}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    # assert data['sum'] == 3