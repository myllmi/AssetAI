from pathlib import Path

from ai.gen_ai import AIEmbedding
from db.db_mongo import DBMongo
from loaders.yaml_loader import YAMLLoader, convert_dict_to_yaml

source_dir = Path('./files')
files = source_dir.iterdir()
gen_ai = AIEmbedding()
db_mongo = DBMongo()
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
            obj_spec = ops[op]
            spec = convert_dict_to_yaml(obj_spec)
            print('*** OBJ ', obj_spec)
            print('*** SPEC', spec)
            embedding_context = gen_ai.generate_embedding(obj_spec['summary'] + ' - ' + obj_spec['description'])
            vector_dict = {
                'service_spec': spec,
                'summary': obj_spec['summary'],
                'description': obj_spec['description'],
                'plot_embedding': embedding_context,
            }
            db_mongo.insert_one(_db='MYLLMI', _collection='API_SPEC', _dict=vector_dict)
