from pyad import pyad
from controllers.search_ad import SearchAD
from models.active_directory import ActiveDirectory


class ExecuteAd:
    def __init__(self, object_str: str, group_str: str):
        self.object_str = object_str
        self.object = pyad.from_cn(object_str)
        self.group_str = group_str
        self.group = pyad.from_cn(group_str)

    def validation(self):
        ad_obj_type = SearchAD(self.object_str).get_type()
        ad_group_type = SearchAD(self.group_str).get_type()

        if ad_obj_type is None:
            return {
                'error': f'O objeto {self.object_str} não foi encontrado no Active Directory.'
            }
        elif ad_group_type is None:
            return {
                'error': f'O grupo {self.group_str} não foi encontrado no Active Directory.'
            }
        else:
            return True

    def run_action(self, action: str):
        success_msg = {
            'add': 'adicionado ao grupo',
            'del': 'removido do grupo'
        }

        actions = {
            'add': self.object.add_to_group,
            'del': self.object.remove_from_group
        }

        validation = self.validation()
        if validation:
            try:
                ActiveDirectory().set_default()
                actions[action](self.group)
                return {
                    'action_log': f'{self.object_str} {success_msg[action]} {self.group_str}.'
                }
            except Exception as err:
                return {
                    'message': f'Erro ao executar a ação "{action}".',
                    'details': f'{err}'
                }
        else:
            return validation
