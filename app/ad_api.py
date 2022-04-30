from fastapi import FastAPI
from uvicorn import run


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
