from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class User(BaseModel):
    id: UUID = uuid4()
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    age: int = Field(min=10, max=60)
    email_id: str = Field(min_length=10)