from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/profile")
def profile():
    return {"id": 1, "username": "alice"}

@app.get("/users/{id}")
def get_users(id: int):
    users = {
        1: {"id": 1, "username": "alice"},
        2: {"id": 2, "username": "bob"}
    }
    return users.get(id, {"error": "User not found"})