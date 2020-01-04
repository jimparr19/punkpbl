import pytest
import index


@pytest.fixture
def app():
    app = index.app
    return app.server


def test_available(client):
    response = client.get("/")
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
