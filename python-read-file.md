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
