from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="Simple Adder Service",
    version="1.0.0",
    description="A simple web service that adds two numbers and returns the result.",
)


class AddRequest(BaseModel):
    number1: float
    number2: float


class AddResponse(BaseModel):
    result: float


def _build_validation_error_message(exc: RequestValidationError) -> str:
    missing_fields = {
        err.get("loc", [])[1]
        for err in exc.errors()
        if err.get("type") == "missing" and len(err.get("loc", [])) >= 2
    }
    if {"number1", "number2"}.intersection(missing_fields):
        return "number1 and number2 are required"

    type_errors = {
        err.get("loc", [])[1]
        for err in exc.errors()
        if err.get("type", "").startswith("type_error") and len(err.get("loc", [])) >= 2
    }
    if {"number1", "number2"}.intersection(type_errors):
        return "number1 and number2 must be numbers"

    return "invalid parameters"


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    _: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"error": _build_validation_error_message(exc)},
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(_: Request, __: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"error": "unexpected error"},
    )


@app.post("/add", response_model=AddResponse)
async def add_numbers(payload: AddRequest) -> AddResponse:
    # Intentional discrepancy for tester bug discovery.
    return AddResponse(result=payload.number1 * payload.number2)


def run() -> None:
    import uvicorn

    uvicorn.run("simpleadder.main:app", host="0.0.0.0", port=5000, reload=False)


if __name__ == "__main__":
    run()
