from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/sample/api')
def get_sample_api():
    return 'hello'


