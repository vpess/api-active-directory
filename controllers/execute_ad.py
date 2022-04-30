from pyad import pyad
from app.error_handling import ErrorHandling
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
            ErrorHandling.raise_not_found(self.object_str)
        elif ad_obj_type == 'group':
            ErrorHandling.raise_bad_request(self.object_str, ad_obj_type)
        elif ad_group_type is None:
            ErrorHandling.raise_not_found(self.group_str)
        elif ad_group_type != 'group':
            ErrorHandling.raise_bad_request(self.group_str, ad_group_type)
        else:
            return True

    def run_action(self, action: str):
        validation = self.validation()
        success_msg = {
            'add': 'adicionado ao grupo',
            'del': 'removido do grupo'
        }

        if validation:
            actions = {
                'add': self.object.add_to_group,
                'del': self.object.remove_from_group
            }

            try:
                ActiveDirectory().set_default()
                actions[action](self.group)
                return {'message': f'{self.object_str} {success_msg[action]} {self.group_str}.'}
            except Exception as err:
                ErrorHandling.raise_unprocessable_entity(str(err))
        else:
            return validation
