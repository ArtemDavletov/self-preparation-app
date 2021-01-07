from pydantic import BaseModel


class TicketSchema(BaseModel):
    notebook_name: str
    question: str
    answer: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "question": "Sample ticket question",
                "answer": "Sample ticket answer",
            }
        }
