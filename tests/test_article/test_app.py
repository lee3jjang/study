import pytest
import requests

@pytest.mark.parametrize(
    'data',
    [
        {
            'author': 'John Doe',
            'title': 'New Article',
            'content': 'Some extra awesome content'
        },
        {
            'author': 'John Doe',
            'title': 'New Article',
        },
        {
            'author': 'John Doe',
            'title': None,
            'content': 'Some extra awesome content'
        }
    ]
)
def test_create_article_bad_request(client, data):
    """
    GIVEN request data with invalid values or missing attributes
    WHEN endpoint /create-article/ is called
    THEN it should return status 400 and JSON body
    """
    response = client.post(
        '/create-article/',
        data=json.dumps(
            data
        ),
        content_type='application/json',
    )

    assert response.status_code == 400
    assert response.json is not None

@pytest.mark.e2e
def test_create_list_get(client):
    requests.post(
        'http://localhost:5000/create-article/',
        json={
            'author': 'john@doe.com',
            'title': 'New Article',
            'content': 'Some extra awesome content'
        }
    )
    response = requests.get(
        'http://localhost:5000/article-list/',
    )

    articles = response.json()

    response = requests.get(
        f'http://localhost:5000/article/{articles[0]["id"]}/',
    )

    assert response.status_code == 200