import json
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

input_file = "/home/hutu/PersonaDataset/PE/data/data_augment/distill_augment_data/valid_augment_after_process.json"
output_file = "/home/hutu/PersonaDataset/AMRBART/examples/utterance_parsing.jsonl"

with open(input_file,"r") as f:
    raw_data = json.load(f)

texts = []
for x in raw_data:
    if len(x[0]['triple']):
        texts.append(x[2])

with open(output_file, 'w') as f:
    for text in texts:
        text = text.split(".")
        amr_dict = {"sent":text, "amr":""}
        f.write(json.dumps(amr_dict)+"\n")


print("gg")


