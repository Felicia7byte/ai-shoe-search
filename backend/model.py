import torch
import open_clip


class CLIPModel:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model, _, _ = open_clip.create_model_and_transforms(
            "ViT-B-32",
            pretrained="openai"
        )

        self.tokenizer = open_clip.get_tokenizer("ViT-B-32")

        self.model = self.model.to(self.device)
        self.model.eval()

    def encode_text(self, text: str):
        tokens = self.tokenizer([text]).to(self.device)

        with torch.no_grad():
            features = self.model.encode_text(tokens)

        features = features / features.norm(
            dim=-1,
            keepdim=True
        )

        return features.cpu().numpy().astype("float32")
