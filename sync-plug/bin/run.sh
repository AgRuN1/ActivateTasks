#!/bin/sh

if [ "$DEBUG" -eq "1" ]; then
    uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
else
    uvicorn app.main:app --host 0.0.0.0 --port 8080 --workers 3
fi