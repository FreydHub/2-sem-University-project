import json
import pyaudio

with open('../BackEnd/commands_data_base.json', 'r', encoding='utf-8') as f:
    commands_config = json.load(f)

with open('../BackEnd/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)


def get_api():
    return {'open_api': config['API']['open_api'], 'secret_api': config['API']['secret_api']}


def get_mics_list():
    mics = []
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(p.get_device_info_by_index(i))
        if p.get_device_info_by_index(i)['name'] == 'Microsoft Sound Mapper - Input':
            pass
        elif p.get_device_info_by_index(i)['name'] == 'Microsoft Sound Mapper - Output':
            pass
        else:
            mics.append(p.get_device_info_by_index(i))

    return mics


def get_voice():
    return config['VOICE']


def get_assistant_name():
    return sorted(commands_config['ASSISTANT_NAME_VARS'], key=len, reverse=True)


def get_commands():
    for key in commands_config['COMMANDS']['command_list']:
        commands_config['COMMANDS']['command_list'][f'{key}'] = sorted(commands_config['COMMANDS']['command_list'][f'{key}'], key=len, reverse=True)
    return commands_config['COMMANDS']['command_list']


def get_answers():
    return commands_config['COMMANDS']['answer_list']


def save_new_config(new_open_api_key='', new_secret_api_key='', voice=''):
    need_save = False
    if config['API']['open_api'] != new_open_api_key and new_open_api_key != '':
        config['API']['open_api'] = new_open_api_key
        need_save = True
    if config['API']['secret_api'] != new_secret_api_key and new_secret_api_key != '':
        config['API']['secret_api'] = new_secret_api_key
        need_save = True
    if config['VOICE'] != voice and voice != '' and voice != 'None':
        config['VOICE'] = voice
        need_save = True
    if need_save:
        with open('../BackEnd/config.json', 'w', encoding='utf-8') as file:
            json.dump(config, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':

    a = get_mics_list()
    print(a)