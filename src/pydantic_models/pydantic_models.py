from pydantic import BaseModel, Field, validator


class SimpleJsonBaseModel(BaseModel):
    """
    model example

    {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
    }
    """
    user_id: int = Field(alias="userId", gt=0)
    id: int = Field(gt=0)
    title: str
    completed: bool

    @validator("title")
    def title_min_length(cls, v):
        if len(v) < 4:
            raise ValueError("Length of title must be grater than 3 chars")
        return v
