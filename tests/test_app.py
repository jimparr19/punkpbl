import os
import sys
import pytest

app_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, app_path)

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
