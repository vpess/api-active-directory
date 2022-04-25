from pyad import pyad
from models.active_directory import ActiveDirectory


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

    # def __object_not_found(self):
    #     return {
    #         'error': f'{self.object_str} não foi encontrado no Active Directory.'
    #     }

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
                return '404'
            else:
                return {
                    "name": self.ad_object.name,
                    "distinguishedName": self.ad_object.distinguishedname,
                    "description": self.ad_object.description
                }

    def get_user(self):
        ActiveDirectory().set_default()
        ad_type = self.get_type()

        if ad_type is None:
            return '404'
        else:
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

    def get_computer(self):
        ActiveDirectory().set_default()
        ad_type = self.get_type()

        if ad_type is None:
            return '404'
        else:
            gp_list = self.ad_object.memberof
            return {
                "name": self.ad_object.name,
                "distinguishedName": self.ad_object.distinguishedname,
                "description": self.ad_object.description,
                "whenCreated": self.ad_object.whencreated.Format(),
                "whenChanged": self.ad_object.whenchanged.Format(),
                "memberOf": self.__get_group_list(gp_list)
            }
