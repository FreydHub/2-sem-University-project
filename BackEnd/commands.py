import time
import random
import winsound
import webbrowser

from fuzzywuzzy import fuzz
from BackEnd import json_reader


class Commands:

    def __init__(self):
        self.cmd = json_reader.get_commands()
        self.ans = json_reader.get_answers()
        self.marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''

    def find_command(self, recognized_text):
        f_name = 'find_command'
        recognized_text = recognized_text.lower()
        for key in self.cmd:
            for value in self.cmd[key]:
                if value in recognized_text:
                    print(f'[{f_name}]', key)
                    return eval(f'self.{key}("{recognized_text}")')
        else:
            print(f'[{f_name}] No such command:', recognized_text)
            return 'Нет такой команды'

    def find_command_fuzz(self, recognized_text):
        f_name = 'find_command_fuzz'
        max_rating = 0
        max_key = ''
        for c in self.marks:
            recognized_text = recognized_text.replace(c, '')
        for key in self.cmd:
            for item in self.cmd[key]:
                current_rating = fuzz.partial_ratio(recognized_text, item)
                if current_rating > max_rating:
                    max_rating = current_rating
                    max_key = key
                    print(item, max_rating)
        if max_rating > 80:
            print(f'[{f_name}]', max_key, max_rating)
            return eval(f'self.{max_key}("{recognized_text}")')
        else:
            print(f'[{f_name}] No such command:', recognized_text)
            return self.browser_search(recognized_text)

    def find_command_fuzz_upd(self, recognized_text):
        f_name = 'find_command_fuzz_upd'
        for c in self.marks:
            recognized_text = recognized_text.replace(c, '')
        for key in self.cmd:
            for item in self.cmd[key]:
                bench = recognized_text[:(len(item))]
                current_rating = fuzz.QRatio(bench, item)
                if current_rating > 80:
                    recognized_text = recognized_text.replace(bench, '')
                    print(f'[{f_name}]', key, item, current_rating)
                    return eval(f'self.{key}("{recognized_text}")')
        print(f'[{f_name}] No such command:', recognized_text)
        return self.browser_search(recognized_text)

    def greetings(self, *_):
        return random.choice(self.ans['greetings'])

    def what_is_up(self, *_):
        return random.choice((self.ans['what_is_up']))

    def you_tube(self, *_):
        webbrowser.open('https://www.youtube.com/')
        return random.choice(self.ans['open_site'])

    def google(self, *_):
        webbrowser.open('https://www.google.ru/')
        return random.choice(self.ans['open_site'])

    def yandex(self, *_):
        webbrowser.open('https://yandex.ru/')
        return random.choice(self.ans['open_site'])

    def long_command_for_test(self, *_):
        return random.choice(self.ans['long_command_for_test'])

    def browser_search(self, text, *_):
        text.replace(' ', '+')
        webbrowser.open(f'https://yandex.ru/search/?text={text}')
        return random.choice(self.ans['browser_search'])

    def bye(self, *_):
        return random.choice(self.ans['bye'])

    def pptx_end(self, *_):
        return self.ans['pttx_end'][0]

    def eva(self, *_):
        return self.ans['eva'][0]

    def c_time(self, *_):

        a = time.localtime(time.time())
        if int(str(a.tm_hour)[-1]) == 1:
            hour = 'час'
        elif int(str(a.tm_hour)[-1]) in [2, 3, 4]:
            hour = 'часа'
        else:
            hour = 'часов'

        if int(str(a.tm_min)[-1]) == 1:
            minutes = 'минута'
        elif int(str(a.tm_min)[-1]) in [2, 3, 4]:
            minutes = 'минуты'
        else:
            minutes = 'минут'

        return f'Сейчас {str(a.tm_hour)} {hour} {str(a.tm_min)} {minutes}'

    def c_date(self, *_):
        a = time.localtime(time.time())
        day = {1: "первое", 2: "второе", 3: "третье", 4: "четвертое", 5: "пятое", 6: "шестое", 7: "седьмое",
               8: "восьмое", 9: "девятое", 10: "десятое",
               11: "одиннадцатое", 12: "двенадцатое", 13: "тринадцатое", 14: "четырнадцатое", 15: "пятнадцатое",
               16: "шестнадцатое", 17: "семнадцатое", 18: "восемнадцатое", 19: "девятнадцатое", 20: "двадцатое",
               21: "двадцать первое", 22: "двадцать второе", 23: "двадцать третье", 24: "двадцать четвертое",
               25: "двадцать пятое", 26: "двадцать шестое", 27: "двадцать седьмое", 28: "двадцать восьмое",
               29: "двадцать девятое", 30: "тридцатое",
               31: "тридцать первое"}
        month = {1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня", 7: "июля", 8: "августа",
                 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"}
        week = {0: "понедельник", 1: "вторник", 2: "среда", 3: "четверг", 4: "пятница", 5: "суббота", 6: "воскресение"}
        return f'Сегодня {day[a.tm_mday]} {month[a.tm_mon]}, {week[a.tm_wday]}'

    def random_coin(self, *_):
        winsound.PlaySound('../B/audio_beeps/coin.wav', winsound.SND_FILENAME)
        return random.choice(self.ans['random_coin'])


if __name__ == '__main__':
    print(Commands().random_coin())
