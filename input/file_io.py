from translate import Translator
with open('english.txt', 'r') as english_file:
    translator = Translator(to_lang='ja')
    english_lines = english_file.readlines()
    for line in english_lines:
        japanese_line = translator.translate(line)
        with open('japanese.txt', 'a+', encoding='utf-8') as japanese_file:
            japanese_file.write(f'{japanese_line} \n')
