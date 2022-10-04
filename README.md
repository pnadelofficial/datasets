# Example Datasets for CLS 161 
This repo contains several datasets that I have compiled for CLS161 in the Fall of 2022. They are in varying states of difficulty, based on their relative cleanness. Please see the license below as well as the LICENSE file in the repo itself if you have any questions about usage. 

## Contents
* *cahiers_de_doleance.csv*: This dataset contains all of the Cahiers de Dolence sent to Louis XVI before, during and after the events of the Summer of 1789.
* *democracy_in_america_de_tocqueville.csv*: This is a CSV form of both volumes of *Democracy in America* by Alexis de Tocqueville (first volume: 'https://www.gutenberg.org/files/815/815-h/815-h.htm'; second volume: 'https://www.gutenberg.org/files/816/816-h/816-h.htm'). 
* *ramayana_by_canto*: This is a CSV form of the whole *Ramayana* by Valmiki (original: https://www.gutenberg.org/files/24869/24869-h/24869-h.html). 
* *thus_spake_zarathustra*: This is a CSV form of *Thus Spake Zarathrustra* by Frederick Neitzsche (original: https://www.gutenberg.org/files/1998/1998-h/1998-h.htm). 
* *truth_commission*: This is a dataset of amnesty trial transcripts (taken from: https://sabctrc.saha.org.za/documents/amntrans.htm). Before you can begin working with this dataset, you must convert the raw strings of in the last columns into list literals using the `ast` Python module.  
* *ushh_rand_fifty*: This is a dataset of fifty random US Congressional Hearings (taken from: https://archive.org/details/us_house_hearings?tab=collection). If you would like to work with the full dataset or a different subset, let me know.
* *lyrics_app*: This folder should be copied into a working directory and the `lyrics.py` file can be called on the command line by passed an artist and an album. A CSV of all of the songs and their lyrics will be generated. This file uses the Genius API and the associated [`lyricsgenius` Python package](https://github.com/johnwmillr/LyricsGenius). 


Not all of the code to generate these datasets is provided here, though much of it is kept in the `notebooks` subdirectory. If you have any questions about it or want it for yourself, let me know and I'll send it to you.


Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg