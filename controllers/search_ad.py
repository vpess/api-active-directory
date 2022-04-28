from pyad import pyad
from models.active_directory import ActiveDirectory
from app.ad_api import AdApi
from app.long_args import LongArgs


class SearchAD:
    def __init__(self, object_str: str):
        self.object_str = object_str
        self.ad_object = pyad.from_cn(object_str)

    def get_type(self):
        ActiveDirectory().set_default()

        if self.ad_object is not None:
            return self.ad_object.type
        else:
            return None

    def __get_group_list(self, gp_list: list):
        group_list = []
        for gp in gp_list:
            group = pyad.from_dn(gp)
            group_list.append(self.get_group(group))

        return group_list

    def get_group(self, group=None):
        ActiveDirectory().set_default()

        if group is not None:
            return {
                "name": group.name,
                "distinguishedName": group.distinguishedname,
                "description": group.description
            }
        else:
            ad_type = self.get_type()
            if ad_type is None:
                response = LongArgs.info_not_found(self.object_str)
                AdApi.error_handling(404, response)
            elif ad_type != 'group':
                response = LongArgs.info_bad_request(self.object_str, ad_type)
                AdApi.error_handling(400, response)
            else:
                try:
                    return {
                        "name": self.ad_object.name,
                        "distinguishedName": self.ad_object.distinguishedname,
                        "description": self.ad_object.description
                    }
                except Exception as err:
                    response = LongArgs.info_unprocessable_entity(f'{err}')
                    AdApi.error_handling(422, response)

    def get_user(self):
        ActiveDirectory().set_default()
        ad_type = self.get_type()

        if ad_type is None:
            response = LongArgs.info_not_found(self.object_str)
            AdApi.error_handling(404, response)
        elif ad_type != 'user':
            response = LongArgs.info_bad_request(self.object_str, ad_type)
            AdApi.error_handling(400, response)
        else:
            try:
                gp_list = self.ad_object.memberof
                return {
                    "displayName": self.ad_object.displayname,
                    "mail": self.ad_object.mail,
                    "name": self.ad_object.name,
                    "distinguishedName": self.ad_object.distinguishedname,
                    "whenCreated": self.ad_object.whencreated.Format(),
                    "whenChanged": self.ad_object.whenchanged.Format(),
                    "memberOf": self.__get_group_list(gp_list)
                }
            except Exception as err:
                response = LongArgs.info_unprocessable_entity(f'{err}')
                AdApi.error_handling(422, response)

    def get_computer(self):
        ActiveDirectory().set_default()
        ad_type = self.get_type()

        if ad_type is None:
            response = LongArgs.info_not_found(self.object_str)
            AdApi.error_handling(404, response)
        elif ad_type != 'computer':
            response = LongArgs.info_bad_request(self.object_str, ad_type)
            AdApi.error_handling(400, response)
        else:
            try:
                gp_list = self.ad_object.memberof
                return {
                    "name": self.ad_object.name,
                    "distinguishedName": self.ad_object.distinguishedname,
                    "description": self.ad_object.description,
                    "whenCreated": self.ad_object.whencreated.Format(),
                    "whenChanged": self.ad_object.whenchanged.Format(),
                    "memberOf": self.__get_group_list(gp_list)
                }
            except Exception as err:
                response = LongArgs.info_unprocessable_entity(f'{err}')
                AdApi.error_handling(422, response)
