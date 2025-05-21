import yaml


def convert_dict_to_yaml(_dict):
    return yaml.dump(_dict, sort_keys=False)


class YAMLLoader:
    def __init__(self, _file_path=None, _encoding='utf-8'):
        self.encoding = _encoding
        self._file_path = _file_path
        self._data = None
        self._components = None
        self._schemas = None
        self._again = True

    def loader(self, _encoding='utf-8'):
        with open(self._file_path, 'r') as f:
            self._data = yaml.load(f, Loader=yaml.SafeLoader)
            self._schemas = self._data['components']['schemas']

    def loader_file(self, _file_path, _encoding='utf-8'):
        with open(_file_path, 'r') as f:
            self._data = yaml.load(f, Loader=yaml.SafeLoader)
            self._schemas = self._data['components']['schemas']

    def get_openapi_version(self):
        return self._data['openapi']

    def get_info(self):
        return self._data['info']

    def get_paths(self):
        return self._data['paths']

    def sanitize_spec(self, _root_dict):
        for _item in _root_dict:
            if isinstance(_root_dict[_item], dict):
                _root_dict[_item] = self.sanitize_spec(_root_dict[_item])
            elif isinstance(_root_dict[_item], list):
                for item_list in _root_dict[_item]:
                    if isinstance(item_list, dict):
                        _root_dict[_item][_root_dict[_item].index(item_list)] = self.sanitize_spec(item_list)
            else:
                if _item == '$ref':
                    _root_dict = self._schemas[_root_dict[_item].split('/')[3]]
                    self._again = True
                    return _root_dict
        return _root_dict

    def has_more(self):
        return self._again

    def reset_again(self):
        self._again = False

    def start_more(self):
        self._again = True

