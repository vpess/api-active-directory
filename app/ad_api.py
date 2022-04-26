from fastapi import FastAPI, HTTPException
from uvicorn import run
from controllers.search_ad import SearchAD
from app.long_args import LongArgs


class AdApi:
    def __init__(self, tags_metadata):
        self.tags_metadata = tags_metadata
        self.app = FastAPI(
            version='1.0',
            title='Active Directory Explorer',
            description='API desenvolvida para realizar ações no Active Directory (RSAT).',
            openapi_tags=self.tags_metadata,
            contact={"name": "vpess · GitHub", "url": "https://github.com/vpess"},
            swagger_ui_parameters={"syntaxHighlight.theme": "nord",
                                   "defaultModelsExpandDepth": -1})

    def execute(self):
        run(self.app, host="127.0.0.1", port=8000)

    @staticmethod
    def error_handling(obj: str, ad_obj: str):
        if obj == '404':
            raise HTTPException(status_code=404,
                                detail=LongArgs.info_not_found(ad_obj))
        elif obj == '400':
            obj_type = SearchAD(ad_obj).get_type()
            raise HTTPException(status_code=400,
                                detail=LongArgs.info_bad_request(ad_obj, obj_type))
        else:
            pass
