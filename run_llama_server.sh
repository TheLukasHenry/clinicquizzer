#!/bin/bash

echo "Installing required packages..."
pip install transformers torch fastapi uvicorn pydantic

echo "Starting the Llama3-OpenBioLLM-70B server..."
python serve_llama3.py 