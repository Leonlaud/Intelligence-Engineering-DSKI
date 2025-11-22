import numpy as np
import pandas as pd
from datasets import load_dataset

ds = load_dataset("Tobi-Bueck/customer-support-tickets")
df = ds["train"].to_pandas()

df_lang = df['language'].unique()

