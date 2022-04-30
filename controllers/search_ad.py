from pyad import pyad
from app.error_handling import ErrorHandling


class SearchAD:
    def __init__(self, object_str: str):
        self.object_str = object_str
        self.ad_object = pyad.from_cn(object_str)
        self.object_type = self.get_type()

    def get_type(self):
        if self.ad_object is not None:
            return self.ad_object.type
        else:
            return None

    def get_group(self, group=None):
        if group is not None:
            return {
                "name": group.name,
                "distinguishedName": group.distinguishedname,
                "description": group.description
            }
        else:
            if self.object_type is None:
                ErrorHandling.raise_not_found(self.object_str)
            elif self.object_type != 'group':
                ErrorHandling.raise_bad_request(self.object_str, self.object_type)
            else:
                try:
                    return {
                        "name": self.ad_object.name,
                        "distinguishedName": self.ad_object.distinguishedname,
                        "description": self.ad_object.description
                    }
                except Exception as err:
                    ErrorHandling.raise_unprocessable_entity(str(err))

    def get_object(self, request_type: str):
        if self.object_type is None:
            ErrorHandling.raise_not_found(self.object_str)
        elif self.object_type != request_type:
            ErrorHandling.raise_bad_request(self.object_str, self.object_type)
        else:
            try:
                return self.__object_dicts(self.object_type)
            except Exception as err:
                ErrorHandling.raise_unprocessable_entity(str(err))

    def __object_dicts(self, object_type: str):
        groups = self.ad_object.memberof

        default_dict = {
            "name": self.ad_object.name,
            "distinguishedName": self.ad_object.distinguishedname,
            "description": self.ad_object.description,
            "whenCreated": self.ad_object.whencreated.Format(),
            "whenChanged": self.ad_object.whenchanged.Format(),
            "memberOf": self.__get_group_list(groups)
        }
        if object_type == 'user':
            return {
                "displayName": self.ad_object.displayname,
                "mail": self.ad_object.mail,
                **default_dict
            }
        else:
            return default_dict

    def __get_group_list(self, gp_list: list):
        group_list = []
        for gp in gp_list:
            group = pyad.from_dn(gp)
            group_list.append(self.get_group(group))

        return group_list
