# Surlyllabe
A syllabic highlighter for Word in French language. Developed in VBA Word, the macro analyses every word contained in the selection, calling a Python script to make their syllabation. Finally, it highlights each syllable with different colors, thanks to this analysis.
This project has been made-to-mesure for a French teacher in reading learning grade.

![demo](docs/demo.gif)

## Tree view

* `/word` : the Word Add-in containing the VBA code of the macros
* `/python` : the Python files handling the syllabation part of the project
* `/docs` : the documents used for the project management

## Acknowledgments

* Syllabation part is greatly inspired by [@Stilnoxx](https://openclassrooms.com/fr/membres/francisvoilure)'s work available in this interesting [thread](https://openclassrooms.com/forum/sujet/comment-decoupe-une-chaine-de-caractere-en-syllabe-23388)
* Python call handling is taken from [@bburns.km](https://stackoverflow.com/users/243392/brian-burns)'s answer available [there](https://stackoverflow.com/questions/2784367/capture-output-value-from-a-shell-command-in-vba/32600510#32600510)
