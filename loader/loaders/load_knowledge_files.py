from loaders.knowledge.base import KNOW_001
from loaders.knowledge_loader import KnowledgeLoader

dict_base = [KNOW_001]

knowledge_base = KnowledgeLoader(_dict_knowledge=dict_base)
knowledge_base.loader()