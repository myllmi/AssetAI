from pathlib import Path

from ai.gen_ai import AIEmbedding, EMBEDDING_OPENAI_TEXT_3_SMALL
from db.db_qdrant import DBQdrant
from loaders.yaml_loader import YAMLLoader, convert_dict_to_yaml

source_dir = Path('./files')
files = source_dir.iterdir()
gen_ai = AIEmbedding(_embedding_model=EMBEDDING_OPENAI_TEXT_3_SMALL)
# db_mongo = DBMongo()
db_qdrant = DBQdrant()
for file in files:
    print(f'Importing file {file}')
    yaml_loader = YAMLLoader(_file_path=file)
    yaml_loader.loader()
    paths = yaml_loader.get_paths()
    for path in paths:
        ops = paths[path]
        yaml_loader.start_more()
        for op in ops:
            while yaml_loader.has_more():
                yaml_loader.reset_again()
                try:
                    spec = yaml_loader.sanitize_spec(_root_dict=ops[op])
                    ops[op] = spec
                except RecursionError as e:
                    print(e)
            summary = ops[op]['summary']
            description = ops[op]['description']
            obj_spec = {path: ops[op]}
            print('Importing endpoint ', path)
            spec = convert_dict_to_yaml(obj_spec)
            embedding_context = gen_ai.generate_embedding(summary + ' - ' + description)
            vector_dict = {
                'service_spec': spec,
                'summary': summary,
                'description': description,
                'plot_embedding': embedding_context,
            }
            db_qdrant.insert_one_spec(_dict=vector_dict)
            # db_mongo.insert_one(_db='MYLLMI', _collection='API_SPEC', _dict=vector_dict)
