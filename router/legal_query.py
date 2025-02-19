from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from groq import Groq

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

client = Groq()

@router.post("/legal-query")
async def legal_query(request: QueryRequest):
    query_text = request.query.strip()
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant specializing in legal topics. Hi, please note that the following response is for informational purposes only  "
                        "If the user's query is legal-related, provide a detailed legal answer with the appropriate legal terms; if its incident then appropriated law  and help the user to understand . if not, respond with 'I don't know'."
                    )
                },
                {
                    "role": "user",
                    "content": query_text
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )
        return {"response": chat_completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
