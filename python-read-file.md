# How to read a file in using python



## Download the file

#### Create a directory
* I usually like to keep all my projects under one directory
* open your terminal
* `mkdir -p econ312/data-files`
* What is this ?
* `mkdir` -> make a directory
* `-p` -> create any parent directories as required
* Will create a directory call econ312 and under it creates a sub directory called data-files

#### Download file/s into this newly created directory
* example https://github.com/devender/christina-econ312/blob/main/data/UNRATE.csv
* Click on the `Download Raw File` button
* or you can do this
```
open terminal
cd econ312/data-files
wget https://raw.githubusercontent.com/devender/christina-econ312/main/data/UNRATE.csv

```
* Either way now you have this file on your computer in the directory `econ312/data-files`

## Locating the file

Python or for that matter any tool fist needs to know exactly where the file is.

* Open Terminal/Console
* find the file

e.g 
```
➜  ~ cd econ312
➜  econ312 cd data-files
➜  data-files ls
UNRATE.csv
➜  data-files pwd
/Users/devendergollapally/econ312/data-files
➜  data-files
```

* pwd tells you exactly what the path of the file is

* the above output is saying the file is located at `/Users/devendergollapally/econ312/data-files/UNRATE.csv`

## Reading the file

#### Simple CSV Reader
```
import csv

my_file_path = '/Users/devendergollapally/econ312/data-files/UNRATE.csv'

with open(my_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
```

The output of this will be 
```
{'DATE': '1948-01-01', 'UNRATE': '3.4'}
{'DATE': '1948-02-01', 'UNRATE': '3.8'}
{'DATE': '1948-03-01', 'UNRATE': '4.0'}
{'DATE': '1948-04-01', 'UNRATE': '3.9'}
{'DATE': '1948-05-01', 'UNRATE': '3.5'}
{'DATE': '1948-06-01', 'UNRATE': '3.6'}
{'DATE': '1948-07-01', 'UNRATE': '3.6'}
{'DATE': '1948-08-01', 'UNRATE': '3.9'}
....
....
```
