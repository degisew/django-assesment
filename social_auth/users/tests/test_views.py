from django.urls import resolve
from social_auth.users.views import HomeView


class TestHome():
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.view_name == 'home'
