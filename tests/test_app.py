"""Integration tests for app.py"""
import json
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client):
    response = client.post('/accounts/Test')
    assert response.status_code == 200
    json_data = response.data
    data = json.loads(json_data)
    assert data['name'] == 'Test'


def test_retrieving_created_account(client):
    client.post('/accounts/Test')
    response = client.get('/accounts/Test')

    assert response.status_code == 200
    json_data = response.data
    data = json.loads(json_data)
    assert data['name'] == 'Test'


def test_adding_funds(client):
    client.post('/accounts/Test')
    response = client.post('/money', json={
        'name': 'Test', 'amount': 10
    })

    assert response.status_code == 200


def test_can_get_balance_report(client):
    client.post('/accounts/Test')
    response = client.get('/accounts/Test/balance')

    assert response.status_code == 200
    json_data = response.data
    data = json.loads(json_data)
    assert data == 10
