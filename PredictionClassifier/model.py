from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import numpy as np


class ModelClassifier:
    def __init__(self, path: str = "./model"):
        self.model = AutoModelForSequenceClassification.from_pretrained(path)
        self.tokenizer = AutoTokenizer.from_pretrained(path)

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        self.model.eval()

    def prediction(self, sentence: str):
        try:
            inputs = self.tokenizer(
                sentence,
                return_tensors="pt",
                truncation=True,
                padding=True,
                max_length=512
            )

            inputs = {key: value.to(self.device) for key, value in inputs.items()}

            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits
                probabilities = torch.nn.functional.softmax(logits, dim=-1)
                predicted_class = torch.argmax(probabilities, dim=-1).item()

            return {
                "predicted_class": predicted_class,
                "probabilities": probabilities.tolist(),
            }
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def __calc_entropy(raspr: list):
        summary = 0.0
        for i in raspr:
            summary -= i * np.log(i)
        return summary

    def inference(self, sentence: str, entropy=0.72):
        ddict = self.prediction(sentence)

        if ModelClassifier.__calc_entropy(ddict["probabilities"][0]) > entropy:
            return -1
        else:
            return ddict["predicted_class"]



