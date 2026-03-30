from transformers import pipeline, set_seed

class GameContentGenerator:
    def __init__(self, model_name="distilgpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate(self, prompt, max_length=150, temperature=0.7, seed=None):
        if seed is not None:
            set_seed(seed)

        output = self.generator(
    prompt,
    max_length=120,
    temperature=temperature,
    num_return_sequences=1,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    pad_token_id=50256
)

        text = output[0]["generated_text"]
        cleaned = text.split("OUTPUT:")[-1].strip()

        return cleaned
