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


class AddAction(BaseModel):
    action_log: str
    # message: str
    # details: str


class DelAction(AddAction):
    pass

class Message(BaseModel):
    message: str