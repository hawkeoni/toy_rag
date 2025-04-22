import torch
import fitz

def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

# Example usage
text = pdf_to_text("/root/2501.12948v1.pdf")
chunks = []
length = 800
for start in range(0, len(text), 600):
    chunks.append(text[start: start + length])
print(len(chunks))

from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-large-en-v1.5')
model = AutoModel.from_pretrained('BAAI/bge-large-en-v1.5').cuda()
model.eval()

batch_size = 4
batch = []
embeds = []
from tqdm import tqdm
for chunk in tqdm(chunks):
    batch.append(chunk)
    if len(batch) % batch_size == 0:
        encoded_input = tokenizer(batch, padding="longest", truncation=True, return_tensors='pt')
        for k, v in encoded_input.items():
            encoded_input[k] = v.cuda()
        with torch.no_grad():
            model_output = model(**encoded_input)
            sentence_embeddings = model_output[0][:, 0]
            sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
            embeds.append(sentence_embeddings)
            batch = []

if len(batch) % batch_size == 0:
    encoded_input = tokenizer(batch, padding="longest", truncation=True, return_tensors='pt')
    for k, v in encoded_input.items():
        encoded_input[k] = v.cuda()
    with torch.no_grad():
        model_output = model(**encoded_input)
        sentence_embeddings = model_output[0][:, 0]
        sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
        embeds.append(sentence_embeddings)

print(len(embeds))
all_embeds = torch.cat(embeds, dim=0)
print(all_embeds.shape)
torch.save((chunks, all_embeds), "database.pt")