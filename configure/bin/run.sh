#!/bin/sh

if [ "$DEBUG" -eq "1" ]; then
    uvicorn app.main:app --host 0.0.0.0 --port 8081 --reload
else
    uvicorn app.main:app --host 0.0.0.0 --port 8081 --workers 3
fi