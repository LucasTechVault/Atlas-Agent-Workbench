from __future__ import annotations

import math
from collections import defaultdict
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from app.config.settings import settings

_model = None

def get_embedder() -> SentenceTransformer:
    global _model
    
    if _model is None:
        _model = SentenceTransformer(model_name_or_path=settings.embed_model)
    
    return _model

def choose_cluster_count(n_items: int) -> int:
    if n_items <= 2:
        return 1

    return max(2, min(6, int(math.sqrt(n_items))))

def cluster_cards(cards: list[dict]) -> dict[int, list[dict]]:
    if not cards:
        return {}
    
    if len(cards) == 1:
        return {
            0: cards # only single cluster
        }
    
    texts = [f"{card['title']}\n{card['content']}" for card in cards]
    embeddings = get_embedder().encode(texts, normalize_embeddings=True)

    n_clusters = choose_cluster_count(len(cards))
    km = KMeans(n_clusters=n_clusters, random_state=16, n_init=10)
    labels = km.fit_predict(embeddings)

    groups = defaultdict(list)
    for label, card in zip(labels, cards):
        groups[int(label)].append(card)
    
    return dict(groups)