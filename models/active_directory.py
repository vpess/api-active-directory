from pyad import pyad
from time import sleep


class ActiveDirectory:
    def __init__(self):
        self.ldap_server = ''
        self.ldap_port = ''
        self.username = ''
        self.password = ''

    def set_default(self):
        try:
            pyad.set_defaults(ldap_server=self.ldap_server,
                              ldap_port=self.ldap_port,
                              username=self.username,
                              password=self.password)
            sleep(1)
        except Exception as err:
            print(f"Erro ocorrido ao estabelecer conexão: {err}")
