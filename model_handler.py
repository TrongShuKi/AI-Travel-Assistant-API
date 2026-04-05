import torch
from omegaconf import OmegaConf
from transformers import AutoTokenizer, AutoModelForCausalLM

class TextGenerator:
    def __init__(self, config_path):
        self.config = OmegaConf.load(config_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.config.model_path,
            device_map="auto",
            torch_dtype="auto"
        )

    def generate_text(self, prompt_text):
        messages = [
            {"role": "system",
            "content": (
            "Bạn là một Chuyên gia Du lịch AI am hiểu sâu sắc về địa lý, văn hóa và ẩm thực của Việt Nam và thế giới. "
            "Nhiệm vụ của bạn là tư vấn du lịch một cách chuyên nghiệp, chính xác và đi thẳng vào vấn đề.\n\n"
            "NGUYÊN TẮC TRẢ LỜI:\n"
            "Trả lời từ 3 đến 4 câu.\n"
            "KHÔNG dùng gạch đầu dòng (-), KHÔNG dùng số thứ tự (1, 2) hoặc tạo danh sách.\n"
            "Dựa hoàn toàn vào kiến thức thực tế. Nếu người dùng hỏi một địa điểm không tồn tại hoặc bạn không biết rõ, hãy trả lời duy nhất 1 câu: 'Xin lỗi, tôi chưa có đủ thông tin chính xác về địa điểm này.'")
            },
            {"role": "user", "content": prompt_text}
        ]
        
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
        
        with torch.no_grad():
            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=512,
                temperature=0.7,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        return response