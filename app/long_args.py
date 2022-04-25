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
                "name": "Executar (Em desenvolvimento)",
                "description": "Executa ações no Active Directory. **As ações não são realizadas em lote.**"
            }
        ]

    @staticmethod
    def json_not_found(object_str: str):
        return f"Não foi possível localizar '{object_str}' no Active Directory. Revise o que foi digitado, e se " \
               f"necessário, tente novamente."
