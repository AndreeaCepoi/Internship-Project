#!/bin/bash

word_file="/usr/share/dict/words"

random_word=$(grep -E "^[a-zA-Z]{$1}$" "$word_file" | shuf -n 1) # cu grep cauta in 'word_file' liniile care au un caracter  care trebuie sa fie o litera (mare sau mica) de lungimea '$1'

# random_word=$(shuf -n 1 "$word_file") #shuf -n 1 -> amesteca liniile fișierului cu cuvinte și apoi extrage prima linie (care este un cuvânt random)
echo "Random Word: $random_word"

