#!/bin/sh

if [ "$DEBUG" -eq "1" ]; then
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 3
fi