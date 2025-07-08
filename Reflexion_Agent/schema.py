from pydantic import BaseModel, Field
from typing import List

class Reflection(BaseModel):
    missing: str = Field(description="Critique of what is missing")
    superfluous: str = Field(description="Critique of what is superfluous")

class AnswerQn(BaseModel):
    """Answer the Question"""

    answer: str = Field(description="~250 word detailed answer to the question")
    searched_queries: List[str] = Field(description="1-3 search queries for researching improvements" \
    "address the critique of current answer")
    
    reflection: Reflection = Field(description="Your reflection on current answer")

class ReviseAnswer(AnswerQn):
    """Revise your original answer to your question."""

    references: List[str] = Field(
        description="Citations motivating your updated answer."
    )