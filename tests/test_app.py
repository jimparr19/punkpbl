from index import server

@pytest.fixture
def app():
    app = server.app
    return app


def test_available(client):
    response = client.get("/available")
    assert response.status_code == 200


