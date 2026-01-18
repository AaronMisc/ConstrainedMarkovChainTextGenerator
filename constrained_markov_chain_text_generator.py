# A constrained Markov chain text generator using a stochastic grammar-like rule system. Generates a paragraph of text based on the words inputted and the rules written.
# Copyright (C) 2026 AaronMisc

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from collections import defaultdict
from random import choice, seed

class Word:
    def __init__(self, text:str, word_type:str):
        self.text = text
        self.word_type = word_type

class Sentence:
    def __init__(self, string:str="", current_word:Word=None):
        self.string = string
        self.current_word = current_word

    def __str__(self):
        return self.string
    
    def is_empty(self) -> bool:
        if self.string == "":
            return True
        else:
            return False

    def add_word(self, new_word:Word) -> None:
        self.string += new_word.text + " "
        self.current_word = new_word

class WordList:
    def __init__(self):
        self.all_words = {}
        self.all_types = defaultdict(list)
    
    def append(self, new_word:Word) -> None:
        self.all_words.update({new_word.text: new_word})
        self.all_types[new_word.word_type].append(new_word)

class Paragraph:
    def __init__(self, default_follower_types:dict[str, list[str]], possible_words:list[Word], length:int=30, random_seed:int|None=None):
        self.default_follower_types = default_follower_types
        
        self.sentence = Sentence() 
        self.word_list = WordList()

        if not (random_seed is None):
            seed(random_seed)
        
        for possible_word in possible_words:
            self.word_list.append(possible_word)

        for i in range(length):
            self.continue_sentence()

    def __str__(self):
        return str(self.sentence)
    
    def continue_sentence(self) -> None:
        if self.sentence.is_empty():
            self.sentence.add_word(list(self.word_list.all_words.values())[0])
        else:
            current_follower_types = self.default_follower_types[self.sentence.current_word.word_type]
            next_word_type = choice(current_follower_types)
            next_word = choice(self.word_list.all_types[next_word_type])
            self.sentence.add_word(next_word)


def microphone_test_example():
    simple_grammar_rules = {
        "noun": ["conjunction", "verb", "preposition"],
        "conjunction": ["noun", "adjective", "preposition"],
        "verb": ["conjunction", "noun", "adjective", "preposition"],
        "adjective": ["noun"],
        "preposition": ["noun", "adjective"],
    }

    microphone_test_words = [
        Word("sausages", "noun"), 
        Word("potatoes", "noun"),
        Word("marmelades", "noun"),
        Word("bubbles", "noun"),
        Word("jelly", "noun"),
        Word("bacon", "noun"),
        Word("pepper", "noun"),
        Word("seashells", "noun"),
        Word("shores", "noun"),
        Word("popping", "verb"),
        Word("kicking", "verb"),
        Word("ceasing", "verb"),
        Word("joking", "verb"),
        Word("zapping", "verb"),
        Word("sizzling", "verb"),
        Word("quiet", "adjective"),
        Word("six", "adjective"),
        Word("black", "adjective"),
        Word("dark", "adjective"),
        Word("pampered", "adjective"),
        Word("loud", "adjective"),
        Word("and", "conjunction"),
        Word("after", "conjunction"),
        Word("but", "conjunction"),
        Word("at", "preposition"),
        Word("except", "preposition"),
        Word("as", "preposition"),
        Word("with", "preposition"),
    ]

    paragraph = Paragraph(simple_grammar_rules, microphone_test_words, length=100, random_seed=0)
    print(paragraph)

if __name__ == "__main__":
    microphone_test_example()