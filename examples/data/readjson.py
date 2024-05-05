import json
import os   
current_dir = os.path.dirname(os.path.realpath(__file__))

class massive():
    def load_words_from_json(self):
        with open(f'{current_dir}/russian-words.json' , 'r', encoding="utf-8") as f:
            words_list = json.load(f)
        return words_list

if __name__ == '__main__':
    words = massive().load_words_from_json()
    print(words)