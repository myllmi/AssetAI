from ai.gen_ai import AIEmbedding, EMBEDDING_OPENAI_TEXT_3_SMALL
from db.db_qdrant import DBQdrant

gen_ai = AIEmbedding(_embedding_model=EMBEDDING_OPENAI_TEXT_3_SMALL)
db_qdrant = DBQdrant()

class KnowledgeLoader:
    def __init__(self, _dict_knowledge=None):
        self._dict_knowledge = _dict_knowledge

    def loader(self):
        self.persist_vector_db()

    def loader_file(self, _dict_knowledge):
        self._dict_knowledge = _dict_knowledge
        self.persist_vector_db()

    def persist_vector_db(self):
        for _dict in self._dict_knowledge:
            embedding_context = gen_ai.generate_embedding(_dict['description'] + '\n\n' + _dict['summary'])
            vector_dict = {
                'description': _dict['description'],
                'summary': _dict['summary'],
                'solution': _dict['solution'],
                'plot_embedding': embedding_context,
            }
            db_qdrant.insert_one_knowledge(_dict=vector_dict)
