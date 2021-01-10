from pydantic.main import BaseModel


class NotebookSchema(BaseModel):
    notebook_name: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "notebook_name": "Algebra",
            }
        }


class UpdateNotebookSchema(BaseModel):
    notebook_name: str
    new_notebook_name: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Algebra",
                "new_notebook_name": "Geometry"
            }
        }
