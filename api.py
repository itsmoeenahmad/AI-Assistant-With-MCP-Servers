# Required Libraries Are
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from main import ai_assistant


# FastAPI Instance
app = FastAPI(
    title='AI Assistant Using MCP Servers',
    description='Develop an AI assistant powered by MCP Servers, designed for efficient and scalable task automation. Integrate Playwright for browser automation, Airbnb for rental data access, and DuckDuckGo for privacy-focused web search.',
    version='0.1',
)

# Base Model - For API body
class PostApiBody(BaseModel):
    user_query: str
    

#Api endpoint code
@app.post('/ai_assistant')
async def calling_ai(body: PostApiBody):
    try: 
        # Calling main code
        response = await ai_assistant(user_query=body.user_query)

        # returning the response
        return JSONResponse(
            status_code=200,
            content={"response": response}
        )

    except Exception as e:
        return HTTPException(
            status_code=400,
            detail=f"An internal error occurred: {str(e)}"
        )