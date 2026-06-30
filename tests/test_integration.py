from test_main import get_test_app

def test_app_loads_correctly():
    test_app = get_test_app()
    assert test_app is not None
