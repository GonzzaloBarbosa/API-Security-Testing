from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()

security = HTTPBearer(auto_error=False)

# Tokens de demonstração associados a utilizadores
DEMO_TOKENS = {
    "demo-secret-token": {"id": 1, "username": "alice"},
    "bob-demo-token": {"id": 2, "username": "bob"}
}

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Missing authentication token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    user = DEMO_TOKENS.get(credentials.credentials)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return user

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/profile")
def profile(authenticated_user: dict = Depends(verify_token)):
    return authenticated_user

@app.get("/users/{id}")
def get_users(
    id: int,
    authenticated_user: dict = Depends(verify_token)
):
    users = {
        1: {"id": 1, "username": "alice"},
        2: {"id": 2, "username": "bob"}
    }

    # Verificar se o utilizador existe
    if id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Verificar se o utilizador tem permissão
    if id != authenticated_user["id"]:
        raise HTTPException(
            status_code=403,
            detail="Access forbidden"
        )

    return users[id]

