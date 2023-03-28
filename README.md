# WebKnife

## Table of Contents
  * [Installation](#installation)
  * [Quick start](#quick-start)
  * [Usage](#Usage)
  * [Features](#features)
  
## Installation

Download using git, pip.

```bash
$ pip install git+'https://github.com/Revi1337/WebKnife.git'  
$ git clone 'https://github.com/Revi1337/WebKnife.git'
```
(Mac/homebrew users may need to use ``pip3``)


## Quick start
```bash
$ python .\WebKnife.py -h
```


## Usage
```bash
$ python WebKnife.py discovery -h

     _  _  _ _______ ______       _     _ __   _ _____ _______ _______
     |  |  | |______ |_____]      |____/  | \  |   |   |______ |______
     |__|__| |______ |_____]      |    \_ |  \_| __|__ |       |______


                                                @Author: revi1337


usage: WebKnife.py discovery [-h] [-X METHOD] [-b COOKIES] [-A AGENTS] [-H HEADERS] [-k] [--wordlist WORDLIST] [-fs [CODE ...]] [-fc [SIZE ...]] [-mc [CODE ...]]
                             [-ms [SIZE ...]] [--find-string TEXT] [--regex REGEX]

options:
  -h, --help           show this help message and exit

Global options:
  -X METHOD            http method
  -b COOKIES           http cookie value
  -A AGENTS            http user-agent
  -H HEADERS           additional header.
  -k                   skip ssl certificate
  --wordlist WORDLIST  specify entering valid, unexpected or random data wordlist

Discovery Options:
  -fs [CODE ...]       filter response status code.
  -fc [SIZE ...]       filter response size
  -mc [CODE ...]       match response status code
  -ms [SIZE ...]       match response size
  --find-string TEXT   find a string contained in response
  --regex REGEX        find a string match with regular expression
```

## Features
  * Discovery Web Contents With Wordlists
  * Fuzzing