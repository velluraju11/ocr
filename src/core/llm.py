from typing import List, Dict, Any, Optional
import os
from openai import OpenAI, OpenAIError
from src.core.config import settings

class LLMService:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
        self.model = settings.DEFAULT_MODEL
        self.client = None
        if self.api_key:
            try:
                self.client = OpenAI(api_key=self.api_key)
            except Exception as e:
                print(f"Warning: Failed to initialize OpenAI client: {e}")

    def generate_response(self, system_prompt: str, user_prompt: str, json_mode: bool = False) -> str:
        """
        Generates a response from the LLM.
        If no API key is present, it returns a simulated response based on the role.
        """
        if not self.client:
            return self._mock_response(system_prompt, user_prompt)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"} if json_mode else {"type": "text"}
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            print(f"OpenAI API Error: {e}. Falling back to mock.")
            return self._mock_response(system_prompt, user_prompt)
        except Exception as e:
            print(f"Unexpected error: {e}. Falling back to mock.")
            return self._mock_response(system_prompt, user_prompt)

    def _mock_response(self, system_prompt: str, user_prompt: str) -> str:
        """
        Simulates intelligent responses for testing purposes.
        """
        print(f"\n[LLM Call] Role: {system_prompt[:30]}... | User: {user_prompt[:30]}...")

        if "Product Manager" in system_prompt:
            return """
# Product Specification: Ryha Generated App

## 1. Executive Summary
A streamlined application to address the user's request.

## 2. User Roles
- Admin
- Regular User

## 3. Core Features
- User Authentication (Login/Signup)
- Dashboard View
- CRUD Operations for main entities
- Profile Management

## 4. User Flow
1. User logs in.
2. User views dashboard.
3. User performs main action.
"""
        elif "System Architect" in system_prompt:
            return """
# System Architecture

## 1. Tech Stack
- **Frontend**: React (Next.js)
- **Backend**: Python (FastAPI)
- **Database**: PostgreSQL
- **DevOps**: Docker

## 2. Database Schema
- **Users**: id, username, email, password_hash
- **Items**: id, user_id, content, created_at

## 3. API Structure
- GET /api/v1/items
- POST /api/v1/items
"""
        else:
            return "I am an AI agent. I have processed your request."
