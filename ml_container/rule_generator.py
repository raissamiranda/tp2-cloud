import pandas as pd
from fpgrowth_py import fpgrowth
import pickle
import os

# 1. Playlist Rules Generator

#### Obtendo o dataset a partir da variável de ambiente
dataset_path = os.getenv("DATASET", "/app/datasets/2023_spotify_ds1.csv")

try:
    #### Carregando dataset
    print(f"Carregando dataset: {dataset_path}")
    dataset = pd.read_csv(dataset_path, header=0)
except FileNotFoundError:
    print(f"Erro: Dataset {dataset_path} não encontrado.")
    exit(1)

### Manipulando dataset
# Transformando os dados em uma lista de baskets (playlists)
# Agrupando as músicas por playlist (coluna `pid`)
baskets = dataset.groupby('pid')['track_name'].apply(list).tolist()

### Parâmetros para o FP-Growth
# O suporte é uma metrica que quantifica a frequência com que um item ou um conjunto de itens ocorre no dataset,
# ou seja, a porcentagem de transações (ou playlists, no seu caso) que contêm um determinado item ou conjunto de itens
min_support = 0.1  # Limite mínimo de frequência: 10% das playlists

# Descreve a força de uma regra de associação. 0.5 significa que em 50% das vezes que o antecedente ocorreu, o consequente também ocorreu
min_confidence = 0.5

### FP-Growth para encontrar itemsets frequentes e regras de associação
freq_itemsets, rules = fpgrowth(baskets, minSupRatio=min_support, minConf=min_confidence)

### DEBUG: printando resultados
# print("\nItemsets Frequentes:")
# for itemset in freq_itemsets:
#     print(itemset)

# print("\nRegras de Associação:")
# for rule in rules:
#     print(rule)

#### Salvando as regras de associação em um arquivo .pkl
output_path = "/folder/association_rules.pkl"
with open(output_path, 'wb') as f:
    pickle.dump(rules, f)

print(f"\nRegras de associação salvas no arquivo '{output_path}'.")
