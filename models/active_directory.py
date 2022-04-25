from pyad import pyad


class ActiveDirectory:
    def __init__(self):
        self.ldap_server = ''
        self.ldap_port = ''
        self.username = ''
        self.password = ''

    def set_default(self):
        pyad.set_defaults(ldap_server=self.ldap_server,
                          ldap_port=self.ldap_port,
                          username=self.username,
                          password=self.password)
