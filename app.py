from transformers import TrOCRProcessor
from transformers import VisionEncoderDecoderModel
from PIL import Image

print("Loading model...")

processor = TrOCRProcessor.from_pretrained(
    "microsoft/trocr-base-handwritten"
)

model = VisionEncoderDecoderModel.from_pretrained(
    "microsoft/trocr-base-handwritten"
)

print("Model loaded!")

image = Image.open("output/line1.jpg").convert("RGB")

pixel_values = processor(
    image,
    return_tensors="pt"
).pixel_values

generated_ids = model.generate(
    pixel_values,
    max_new_tokens=50
)

text = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True
)[0]

print("\nDetected Text:")
print(text)
