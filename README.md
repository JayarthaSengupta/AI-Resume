# AI Interview Platform

Portfolio project: AI-driven resume feedback and mock interview practice.

## Stack
- Frontend: Next.js (App Router) + TypeScript
- Backend: FastAPI

## Running locally

Backend:
cd backend
uvicorn main:app --reload
# runs on http://localhost:8000

Frontend:
cd frontend
npm run dev
# runs on http://localhost:3000

## Env vars
backend/.env: FRONTEND_ORIGIN
frontend/.env.local: NEXT_PUBLIC_API_URL