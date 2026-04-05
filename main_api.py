from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model_handler import TextGenerator

app = FastAPI(title="AI Travel Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

try:
    generator = TextGenerator("config.yaml")
except Exception as e:
    print(f"Lỗi khi tải model: {e}")


@app.get("/")
async def read_root():
    return {
        "name": "AI Travel Assistant API",
        "description": "API tạo sinh nội dung giới thiệu địa điểm du lịch bằng Qwen2.5."
    }

@app.get("/health")
async def health_check():
    return {"status": "Active", "message": "Hệ thống đang hoạt động bình thường!"}

@app.post("/generate")
async def generate_content(payload: dict):
    prompt_text = payload.get("prompt")
    if not prompt_text or len(prompt_text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Vui lòng nhập câu hỏi hoặc yêu cầu!")
    
    try:
        result = generator.generate_text(prompt_text)
        
        return {
            "input_prompt": prompt_text,
            "generated_text": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi hệ thống khi sinh văn bản: {str(e)}")