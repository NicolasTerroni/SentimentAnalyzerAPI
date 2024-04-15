from fastapi import FastAPI
from routes.results import result


app = FastAPI()

# Include routes
app.include_router(result)