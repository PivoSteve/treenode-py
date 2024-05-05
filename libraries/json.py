import json

class massive():
    def load_words_from_json(self):
        with open('libraries/russian-words.json' , 'r', encoding="utf-8") as f:
            words_list = json.load(f)
        return words_list

if __name__ == '__main__':
    words = massive().load_words_from_json()
    print(words)