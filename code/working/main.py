import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def index():
    return "Hellow from FastAPI!"


if __name__ == "__main__":
    uvicorn.run(app)
