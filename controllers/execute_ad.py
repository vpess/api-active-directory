from pyad import pyad
from app.ad_api import AdApi
from app.long_args import LongArgs
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
            response_detail = LongArgs.info_not_found(self.object_str)
            AdApi.error_handling(404, response_detail)

        elif ad_obj_type == 'group':
            response_detail = LongArgs.info_bad_request(self.object_str, ad_obj_type)
            AdApi.error_handling(400, response_detail)

        elif ad_group_type is None:
            response_detail = LongArgs.info_not_found(self.group_str)
            AdApi.error_handling(404, response_detail)

        elif ad_group_type != 'group':
            response_detail = LongArgs.info_bad_request(self.group_str, ad_group_type)
            AdApi.error_handling(400, response_detail)

        else:
            return True

    def run_action(self, action: str):
        success_msg = {
            'add': 'adicionado ao grupo',
            'del': 'removido do grupo'
        }

        validation = self.validation()
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
                response_detail = LongArgs.info_unprocessable_entity(f'{err}')
                AdApi.error_handling(422, response_detail)
        else:
            return validation
