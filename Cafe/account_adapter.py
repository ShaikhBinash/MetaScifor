from allauth.account.adapter import DefaultAccountAdapter

class NoNewUserAccountAdater(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return False