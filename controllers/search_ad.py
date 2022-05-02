from pyad import pyad
from app.error_handling import ErrorHandling


class SearchAD:
    def __init__(self, object_str: str):
        self.object_str = object_str
        self.ad_object = pyad.from_cn(object_str)
        self.object_type = self.get_type()

    def get_type(self):
        """Retorna o tipo do ad_object (user, computer ou group)."""
        if self.ad_object is not None:
            return self.ad_object.type
        else:
            return None

    def get_group(self, group=None):
        """Retorna um Dict com as informações do grupo. Se o argumento group for None, logo, o ad_object é do tipo
        group. """
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
        """
        @param request_type: tipo de objeto que será consultado (user ou computer)
        @return: Dict
        """
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
        """Cria um Dict de informações de acordo com o tipo do objeto."""
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
        """Retorna uma lista com todos os dados dos grupos presentes na lista. Os dados são gerados pelo método
        get_group(). """
        group_list = []
        for gp in gp_list:
            group = pyad.from_dn(gp)
            group_list.append(self.get_group(group))

        return group_list
