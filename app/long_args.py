from app.response_models import Message, DetailedMessage

class LongArgs:

    @staticmethod
    def tags_metadata():
        return [
            {
                "name": "Consultar",
                "description": "Realiza consultas no Active Directory. Os dados são retornados de acordo com o tipo "
                               "de objeto "
                               "do Active Directory. "
            },
            {
                "name": "Executar",
                "description": "Executa ações no Active Directory. **As ações não são realizadas em lote.**"
            }
        ]
        
    @staticmethod
    def json_responses():
        return {
            404: {
                "model": Message
            },
            400: {
                "model": Message
            },
            422: {
                "model": DetailedMessage
            }
        }

    @staticmethod
    def info_not_found(object_str: str):
        return f"Não foi possível localizar '{object_str}' no Active Directory. Revise o que foi digitado, e se " \
               f"necessário, tente novamente."

    @staticmethod
    def info_bad_request(object_str: str, object_type: str):
        return f"O objeto {object_str} foi encontrado no Active Directory, mas é do tipo {object_type.upper()}. " \
               f"Utilize a request de forma adequada."

    @staticmethod
    def info_unprocessable_entity(err: str):
        return {
            'message': 'Não foi possível executar a ação da request.',
            'details': f'{err}'
        }
