from fastapi import FastAPI, Request
import uvicorn
import jwt, time

app = FastAPI()

flag = open("./flag.txt").read()
private_key = open("priv").read()
public_key = open("pub").read()


@app.get("/get_token")
async def get_token():
    token = jwt.encode(
        {"admin": False, "now": time.time()}, private_key, algorithm="RS256"
    )
    return token


@app.post("/get_flag")
async def get_flag(request: Request):
    request_body = await request.json()
    token = request_body["token"]
    payload = jwt.decode(token, public_key, algorithms=["RS256"])
    if payload["admin"]:
        return flag
    return {"message": "Sorry i can't give you the flag"}


@app.get("/get_source_code")
async def get_source_code():
    return open(__file__).read()


@app.get("/")
async def home():
    return {"Message": "Powered by fastapi"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, host="0.0.0.0", reload=True, access_log=False)
