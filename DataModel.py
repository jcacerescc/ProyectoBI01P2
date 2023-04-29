from pydantic import BaseModel

class DataModel(BaseModel):
    title: str
    review_text: str

    def columns():
        return ["title", "review_text"]
