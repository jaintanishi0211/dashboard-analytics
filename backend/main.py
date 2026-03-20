from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import stats

app = FastAPI(title="Dashboard Analytics")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stats.router, prefix="/api")