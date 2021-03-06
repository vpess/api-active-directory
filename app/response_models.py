from pydantic import BaseModel
from pydantic.schema import Optional
from typing import List


class GetGroup(BaseModel):
    name: str
    distinguishedName: str
    description: Optional[str]


class GetUser(BaseModel):
    displayName: str
    mail: Optional[str]
    name: str
    distinguishedName: str
    whenCreated: str
    whenChanged: str
    memberOf: List[GetGroup]


class GetComputer(GetGroup):
    whenCreated: str
    whenChanged: str
    memberOf: List[GetGroup]


class AdObject(BaseModel):
    objeto: str
    grupo: str


class Message(BaseModel):
    message: str


class DetailedMessage(Message):
    details: str


class AddAction(Message):
    pass


class DelAction(Message):
    pass
