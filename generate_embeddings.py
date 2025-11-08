import pandas as pd
from sentence_transformers import InputExample
import torch
from torch.utils.data import DataLoader, WeightedRandomSampler
df = pd.read_csv("steam_games_cleaned.csv")
df = df.dropna(subset=["short_description", "name", "metacritic_score"])

# Normalize metacritic_score to [0,1]
min_score = df["metacritic_score"].min()
max_score = df["metacritic_score"].max()
df["weight"] = (df["metacritic_score"] - min_score) / (max_score - min_score)

# Create InputExamples
train_examples = [
    InputExample(texts=[row["short_description"], row["name"]],
                 label=1.0)
    for _, row in df.iterrows()
]

# Convert weights to tensor
weights = torch.tensor(df['weight'].values, dtype=torch.float)

# Weighted sampler for DataLoader
sampler = WeightedRandomSampler(weights=weights, num_samples=len(weights), replacement=True)

def collate_fn(batch):
    return batch
train_dataloader = DataLoader(train_examples, batch_size=16, sampler=sampler,collate_fn=collate_fn)

