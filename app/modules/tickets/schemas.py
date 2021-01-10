from pydantic import BaseModel


class CreateTicketSchema(BaseModel):
    notebook_name: str
    question: str
    answer: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "notebook_name": "Notebook name",
                "question": "Sample ticket question",
                "answer": "Sample ticket answer"
            }
        }


class UpdateTicketSchema(BaseModel):
    notebook_name: str
    question: str
    new_question: str
    new_answer: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "notebook_name": "Notebook name",
                "question": "Sample ticket question",
                "new_question": "New ticket question",
                "new_answer": "New ticket answer"
            }
        }


class DeleteTicketSchema(BaseModel):
    notebook_name: str
    ticket_question: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "notebook_name": "Notebook name",
                "ticket_question": "Sample ticket question"
            }
        }
