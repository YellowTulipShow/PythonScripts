# coding: UTF-8

import file

def __test_config_json_file():
    path = file.to_abs_path('../config', 'databases.json')
    content = file.config_json_file_read(path)
    print(content)
    path = file.to_abs_path('../__auto__/config', 'databases.json')
    path = file.config_json_file_write(path, content)
    print(path)

if __name__ == '__main__':
    __test_config_json_file()
