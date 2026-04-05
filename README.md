# AI Travel Assistant API

**Sinh viên thực hiện:** Nguyễn Minh Trọng
**Mã số sinh viên:** 24120233
**Lớp - Môn học:** 24CTT5 - Tư duy tính toán 
**Giảng viên hướng dẫn:** Lê Đức Khoan

---

## 1. Mô hình Hugging Face
* **Tên mô hình:** `Qwen/Qwen2.5-3B-Instruct`
* **Loại bài toán:** Sinh văn bản (Text Generation)
* **Link Hugging Face:** [Link tới mô hình](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)

## 2. Giới thiệu Dự án
Dự án này là một hệ thống Web API được xây dựng bằng **FastAPI** từ mô hình Học Máy open source trên Hugging Face. Chức năng chính là xử lý và tạo sinh các đoạn văn bản cho các câu hỏi liên quan đến du lịch như một chuyên gia du lịch. Có áp dụng các system prompt để câu trả lời đúng format đoạn văn, và chống ảo giác với các câu hỏi sai sự thật.

## 3. Cấu trúc Source Code
* `config.yaml`: File cấu hình lưu đường dẫn model.
* `requirements.txt`: Danh sách các thư viện Python cần thiết.
* `main_api.py`: Khởi tạo server bằng FastAPI, định nghĩa các endpoint (GET, POST).
* `model_handler.py`: Class xử lý tải model, tokenizer và thực hiện tạo sinh văn bản.
* `test_api.py`: Script dùng để gọi và kiểm thử các endpoint của API.

## 4. Hướng dẫn Cài đặt & Chạy chương trình
### Cách 1. Chạy trên máy cá nhân (Local)
**Bước 1: Cài đặt thư viện**
Mở terminal tại thư mục dự án và chạy lệnh:
```bash
py -m pip install -r requirements.txt
```
**Bước 2: Khởi động Server**
```bash
py -m uvicorn main_api:app --reload
```
**Bước 3: Chạy file Test**
Mở terminal khác cùng thư mục và chạy lệnh:
```bash
py test_api.py
```
### Cách 2. Chạy trên Google Colab
**Bước 1:** Tải file notebook `TextGenerateTravel_api_model.ipynb` lên Google Colab.
**Bước 2: Cấp phát phần cứng**
Vào menu **Runtime** > **Change runtime type** > Chọn **T4 GPU** và lưu lại.
**Bước 3: Cài đặt và Khởi tạo**
Chạy tuần tự các ô code từ trên xuống dưới để cài đặt thư viện và tự động tạo các file cấu hình hệ thống.
**Bước 4: Bật Server và Mở đường hầm (Tunneling)**
Chạy ô code khởi động Server chạy ngầm. Đợi model load xong thì mở terminal lên và chạy lệnh 'ssh -p 443 -R0:localhost:8000 qr@a.pinggy.io' để mở port qua **Pinggy**. Hệ thống sẽ in ra một đường link Public (Ví dụ: `https://xudap-34-21-180-83.run.pinggy-free.link`).
**Bước 5: Kiểm thử API**
Có 2 cách để gọi thử API:
- **Chạy trực tiếp trên local colab** API_URL = "http://127.0.0.1:8000"
- **Chạy trên Public API** Copy đường link Pinggy ở Bước 4, dán vào biến `API_URL` sau đó bấm chạy.

## 5. Hướng dẫn gọi API
### 5.1. Endpoint Kiểm tra thông tin API
Dùng để lấy thông tin về API đang dùng.
* **Đường dẫn:** `/`
* **Phương thức:** `GET`
* **Ví dụ:**
  ```python
    response = requests.get(f"{API_URL}/")
    print(response.json())
  ```
* **Kết quả trả về (JSON):**
  ```json
  {
      "name": "AI Travel Assistant API",
      "description": "API tạo sinh nội dung giới thiệu địa điểm du lịch bằng Qwen2.5.",
  }
  ```
### 5.2. Endpoint Kiểm tra trạng thái (Health Check)
Dùng để kiểm tra xem Server đã khởi động và sẵn sàng nhận lệnh hay chưa.
* **Đường dẫn:**`/health`
* **Phương thức:** `GET`
* **Ví dụ:**
  ```python
    response = requests.get(f"{API_URL}/health")
    print(response.json())
  ```
* **Kết quả trả về (JSON):**
  ```json
  {
      "status": "Active", 
      "message": "Hệ thống đang hoạt động bình thường!"
  }
  ```
### 5.3. Endpoint Tạo sinh nội dung (Generate)
Dùng để gửi câu hỏi du lịch và nhận về đoạn văn bản do AI tư vấn.
* **Đường dẫn:** `/generate`
* **Phương thức:** `POST`
* **Headers:** `Content-Type: application/json`
* **Dữ liệu gửi lên (Body JSON):**
  ```json
  {
      "prompt": "Nội thành Huế có gì thu hút khách du lịch?"
  }
  ```
* **Kết quả trả về thành công:**
  ```json
  {
      "input_prompt": "Nội thành Huế có gì thu hút khách du lịch.",
      "generated_text": " ",
  }
  ```

## 6. Link video demo: 