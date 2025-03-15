#!/usr/bin/env python3
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
import uvicorn
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model and tokenizer
print("Loading model and tokenizer...")
model_id = "aaditya/Llama3-OpenBioLLM-70B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)
print("Model and tokenizer loaded successfully!")

class Message(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = None
    stream: Optional[bool] = False

class ChatChoice(BaseModel):
    index: int
    message: Message
    finish_reason: str

class ChatCompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[ChatChoice]
    usage: Dict[str, int]

@app.post("/v1/chat/completions")
async def chat_completion(request: ChatCompletionRequest):
    from datetime import datetime
    import time
    import random
    import string

    # Format the input as a conversation for the model
    prompt = ""
    for msg in request.messages:
        if msg.role == "user":
            prompt += f"User: {msg.content}\n"
        elif msg.role == "assistant":
            prompt += f"Assistant: {msg.content}\n"
        elif msg.role == "system":
            prompt += f"System: {msg.content}\n"
    prompt += "Assistant: "

    # Generate a response using the model
    inputs = tokenizer.encode(prompt, return_tensors="pt").to(model.device)
    
    max_tokens = request.max_tokens if request.max_tokens else 512
    
    outputs = model.generate(
        inputs, 
        max_new_tokens=max_tokens,
        temperature=request.temperature,
        do_sample=True,
    )
    
    response_text = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
    
    # Create the response
    response = ChatCompletionResponse(
        id=f"chatcmpl-{''.join(random.choices(string.ascii_letters + string.digits, k=12))}",
        object="chat.completion",
        created=int(time.time()),
        model=request.model,
        choices=[
            ChatChoice(
                index=0,
                message=Message(role="assistant", content=response_text),
                finish_reason="stop"
            )
        ],
        usage={
            "prompt_tokens": inputs.shape[1],
            "completion_tokens": outputs.shape[1] - inputs.shape[1],
            "total_tokens": outputs.shape[1]
        }
    )
    
    return response

@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "aaditya/Llama3-OpenBioLLM-70B",
                "object": "model",
                "created": 1677610602,
                "owned_by": "openai",
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 