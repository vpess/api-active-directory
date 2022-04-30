from app.ad_api import AdApi
from app.long_args import LongArgs
from app.response_models import *
from controllers.search_ad import SearchAD
from controllers.execute_ad import ExecuteAd

ad_api = AdApi(LongArgs.tags_metadata())
app = ad_api.app


@app.get("/user/{ad_user}", tags=["Consultar"], response_model=GetUser, responses=LongArgs.json_responses())
async def get_user(ad_user):
    """Retorna informações de um usuário do Active Directory."""
    return SearchAD(ad_user).get_object('user')


@app.get("/computer/{ad_computer}", tags=["Consultar"], response_model=GetComputer, responses=LongArgs.json_responses())
async def get_computer(ad_computer):
    """Retorna informações de um computador do Active Directory."""
    return SearchAD(ad_computer).get_object('computer')


@app.get("/group/{ad_group}", tags=["Consultar"], response_model=GetGroup, responses=LongArgs.json_responses())
async def get_group(ad_group):
    """Retorna informações de um grupo do Active Directory."""
    return SearchAD(ad_group).get_group()


@app.post("/incluir-objeto", tags=["Executar"], response_model=AddAction, responses=LongArgs.json_responses())
async def add_object(ad_object: AdObject):
    """Adiciona um objeto (user ou computer) em um grupo do Active Directory. **A ação não é feita em lote.**"""
    return ExecuteAd(ad_object.objeto, ad_object.grupo).run_action('add')


@app.delete("/remover-objeto", tags=["Executar"], response_model=DelAction, responses=LongArgs.json_responses())
async def remove_object(ad_object: AdObject):
    """Remove um objeto (user ou computer) de um grupo do Active Directory. **A ação não é feita em lote.**"""
    return ExecuteAd(ad_object.objeto, ad_object.grupo).run_action('del')


if __name__ == "__main__":
    ad_api.execute()
