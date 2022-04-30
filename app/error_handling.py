from fastapi import HTTPException
from app.long_args import LongArgs


class ErrorHandling:

    @staticmethod
    def raise_not_found(object_str: str):
        response = LongArgs.info_not_found(object_str)
        ErrorHandling.__raise_exception(404, response)

    @staticmethod
    def raise_bad_request(object_str: str, object_type: str):
        response = LongArgs.info_bad_request(object_str, object_type)
        ErrorHandling.__raise_exception(400, response)

    @staticmethod
    def raise_unprocessable_entity(error_log: str):
        response = LongArgs.info_unprocessable_entity(f'{error_log}')
        ErrorHandling.__raise_exception(422, response)

    @staticmethod
    def __raise_exception(status: int, response_detail: str):
        raise HTTPException(status_code=status,
                            detail=response_detail)
