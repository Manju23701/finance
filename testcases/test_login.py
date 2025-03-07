import pytest
from pages.login import loginclass

@pytest.mark.usefixtures('setup')
class Test_login:
    def test_login(self):

        loginobj = loginclass(self.driver)
        loginobj.login()
