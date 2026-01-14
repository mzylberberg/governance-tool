from fastapi import FastAPI

app = FastAPI(title="Governance Translator API")

@app.get("/health")
def health():
    return {"status": "ok"}
