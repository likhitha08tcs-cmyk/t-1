from app.main import app

def get_test_app():
    return app

def test_app_exists():
    assert app is not None
