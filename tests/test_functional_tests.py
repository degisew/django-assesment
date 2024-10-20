from selenium.webdriver import Chrome

browser = Chrome()


class TestFunctional():
    def test_should_find_app_title(self):
        browser.get('http://127.0.0.1:8000/accounts/signup/')

        assert 'Signup' in browser.title
