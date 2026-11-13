
# 🔐 API Security Testing Framework

A Python-based project for learning and implementing automated API security tests, with a focus on authentication, authorization, and OWASP API Security Top 10 concepts.

The project combines a controlled **FastAPI demonstration API** with an automated security test suite built using **pytest**.

## 🎯 Project Objectives

- Develop practical API security testing skills.
- Automate positive and negative security test scenarios.
- Understand authentication and authorization mechanisms.
- Explore Broken Object Level Authorization (BOLA).
- Apply OWASP API Security Top 10 concepts.
- Build a foundation for an extensible security testing framework.

## 🛠️ Technologies

- Python
- FastAPI
- pytest
- HTTPX / FastAPI TestClient
- REST APIs
- HTTP Bearer Authentication

## 📁 Project Structure

```text
api-security-framework/
├── main.py
├── tests/
│   ├── test_authentication.py
│   └── test_authorization.py
├── .gitignore
└── README.md
```

## 🔌 Demo API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Public health/demo endpoint |
| GET | `/profile` | Returns the authenticated user's profile |
| GET | `/users/{id}` | Returns user data after authorization checks |

The API currently uses two simulated user identities:

- Alice (ID 1)
- Bob (ID 2)

Authentication uses static demonstration tokens. These are for educational purposes only and must not be used in production.

## 🧪 Implemented Security Tests

### Authentication Testing

The following scenarios are covered:

- Accessing a protected endpoint without a token returns `401`.
- Accessing a protected endpoint with an invalid token returns `401`.
- Accessing a protected endpoint with a valid token returns `200`.

### Authorization Testing

The following scenarios are covered:

- Alice cannot access Bob's user data (`403`).
- Alice can access her own user data (`200`).
- Unauthenticated requests to protected user endpoints return `401`.
- Bob can access his own user data (`200`).
- Bob cannot access Alice's user data (`403`).

**Current automated test suite: 8 tests.**

All eight tests passed during local validation.

## 🛡️ OWASP API Security Top 10

### API1:2023 — Broken Object Level Authorization (BOLA)

The demonstration API implements object-level access controls.

An authenticated user can access their own user record but cannot access another user's private record.

Example:

```http
GET /users/2
Authorization: Bearer demo-secret-token
```

The demonstration token represents Alice (ID 1).

Expected response:

```http
HTTP/1.1 403 Forbidden
```

This project demonstrates how automated tests can validate object-level authorization and help identify missing access controls.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/GonzzaloBarbosa/API-Security-Testing.git
cd API-Security-Testing
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install fastapi uvicorn pytest httpx
```

### 4. Run the demonstration API

```bash
python -m uvicorn main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

### 5. Run the automated security tests

```bash
python -m pytest -v
```

Expected test summary:

```text
8 passed
```

The tests use FastAPI's TestClient and do not require a separate running API server.

## 🔎 Security Concepts Covered

- Authentication vs. authorization
- HTTP status codes: 200, 401, 403
- Bearer token authentication
- Object-level authorization
- Principle of least privilege
- Positive and negative security testing
- Automated security validation

## ⚠️ Limitations

This is an educational security testing project, not a production-ready security framework.

- Authentication uses hardcoded demonstration tokens.
- Users and resources are stored in memory.
- No database or real user authentication system is implemented.
- No token expiration, refresh, or revocation mechanisms exist.
- Security testing currently focuses on authentication and object-level authorization.
- The API is designed for local, controlled testing.

## 🗺️ Roadmap

- [x] Create a FastAPI demonstration API
- [x] Implement basic Bearer token authentication
- [x] Implement object-level authorization
- [x] Create automated authentication tests
- [x] Create automated authorization tests
- [ ] Refactor the tests using pytest fixtures
- [ ] Add input validation security tests
- [ ] Introduce role-based access control (RBAC)
- [ ] Generate automated test reports
- [ ] Expand coverage of OWASP API Security Top 10 risks
- [ ] Add CI-based automated test execution

## 📚 Learning Journey

This project is being developed alongside my preparation for the **CompTIA Security+ certification**.

The goal is to combine my professional experience in backend development and REST API testing with practical cybersecurity knowledge.

---

**Author:** Gonçalo Barbosa

[GitHub Profile](https://github.com/GonzzaloBarbosa) |
[LinkedIn](https://www.linkedin.com/in/goncalobarbosa/)
