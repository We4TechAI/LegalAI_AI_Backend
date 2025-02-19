from fastapi import FastAPI
from router.legal_query import router as legal_query_router
from cors_config import configure_cors

app = FastAPI()

# Configure CORS to allow all origins.
configure_cors(app)

# Include the legal advice router.
app.include_router(legal_query_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
