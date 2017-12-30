# wikio
## Sumary
Wikio is an application allowing users to consult wikipedia's datas using API of [Wikimedia](https://www.wikimedia.org/ "Wikimedia's Homepage")

## Installation
* Clone the source :
```
git clone https://github.com/vutrang155/wikio
```
* Run from the directory :
```
sudo pip install .
```

## Usage
`wikio` provides two main commands :
1. `-find`
2. `-get`

### Find
The feature allows users to search for informations as snippets and `pageid` of the subject
```
wikio -find David Bowie
```
### Get
This option give the users the detail of the subject that is passed by `pageid` on the command
```
wikio -get 8786
```
