# ConstrainedMarkovChainTextGenerator
A constrained Markov chain text generator using a stochastic grammar-like rule system. Generates a paragraph of text based on the words inputted and the rules written.

## Explanation
**Contrained**: the next word must follow a set of rules for it to be allowed.
**Markov chain**: the next word is dependent on the current word.
**Stochastic**: random but constrained.
**Grammar-like**: make your own grammar rules. Since they are not that complicated, it will follow general grammar but will still be incorrect (See usage).

## Function
Generates a paragraph of text based on the words inputted and the rules written.

## Usage
Words have a type (like adjective or verb). Make them like this: 
```python
Word("word text", "type")

word_list = [
    Word("sausages", "noun"), 
    Word("popping", "verb"),
]
```

Grammar rules are written in the form:
```python
{"current_word_type": ["allowed_following_word_type1", "allowed_following_word_type2", "etc"]}

{
    "noun": ["conjunction", "verb", "preposition"],
    "conjunction": ["noun", "adjective", "preposition"],
}
```

Put these into a *Paragraph*, set a length.
Then you can convert the paragraph to a string, or print it.
```python
string_paragraph = str(paragraph)
print(paragraph)
```

**See the example in this file.**

## Example code
```python
    simple_grammar_rules = {
        "noun": ["conjunction", "verb", "preposition"],
        "conjunction": ["noun", "adjective", "preposition"],
        "verb": ["conjunction", "noun", "adjective", "preposition"],
        "adjective": ["noun"],
        "preposition": ["noun", "adjective"],
    }

    test_words = [
        Word("sausages", "noun"), 
        Word("potatoes", "noun"),
        Word("popping", "verb"),
        Word("quiet", "adjective"),
        Word("and", "conjunction"),
        Word("with", "preposition"),
    ]

    paragraph = Paragraph(simple_grammar_rules, test_words, length=100, random_seed=0)

    print(paragraph)
```

### Output
sausages popping and with quiet potatoes with potatoes and with potatoes

# License
A constrained Markov chain text generator using a stochastic grammar-like rule system. Generates a paragraph of text based on the words inputted and the rules written.
Copyright (C) 2026 AaronMisc

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.