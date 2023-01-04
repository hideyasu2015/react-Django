from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings

class AccountAdapter(DefaultAccountAdapter):
    def is_safe_url(self, url):
        """
        allauthのログイン後に、外部サイトにリダイレクトできるようにするために、
        オーバーライドしている。
        https://stackoverflow.com/questions/69080076/django-allauth-with-custom-redirect-adapter-ignoring-next-parameter
        """
        try:
            from django.utils.http import url_has_allowed_host_and_scheme
        except ImportError:
            from django.utils.http import (
                is_safe_url as url_has_allowed_host_and_scheme,
            )

        return url_has_allowed_host_and_scheme(url, allowed_hosts=settings.ALLAUTH_ALLOWED_REDIRECT_HOSTS)
