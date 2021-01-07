from pydantic.main import BaseModel


class NotebookSchema(BaseModel):
    name: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Algebra",
            }
        }
