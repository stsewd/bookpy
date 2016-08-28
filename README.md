# bookpy
Renames your e-books for better organization.

# Supported Files
For now only pdf files.

# Dependencies

## Python Packages
- isbnlib
- isbntools
- click

## Extra Dependencies
- [pdftotext](https://en.wikipedia.org/wiki/Pdftotext)

# Basic Usage
```
bookpy [OPTIONS] [SRCS]...

SRCS are the books sources (individual files or a directory).
If any source is given, the current directory will be taken.

Options:
  --version            Show the version and exit.
  -r, --recursive      Get all files recursively from a directory.
  -t, --template       Specify a template with which the books are renamed.
                       Default template is '{short_title} - {main_author} ({year})'
  -h, --help           Show the help and exit.
```

# Example

## Before
```
books/
├── 97.things.every.programmer.should.know.pdf
├── Algorithms.pdf
├── clean_code.pdf
├── intro algorithms.pdf
├── os - andrew tanenbaum.pdf
├── Refactoring.pdf
├── SoftSkills.pdf
└── the_pragmatic_programmer_Andrew_Hunt.pdf
```

## Command
```
bookpy books/
```

## After
```
books/
├── 97 Things Every Programmer Should Know - Kevlin Henney (2010).pdf
├── Algorithms - Robert Sedgewick.pdf
├── Clean code - Robert C. Martin.pdf
├── Introduction To Algorithms - Thomas H. Cormen (2009).pdf
├── Operating Systems - Andrew S. Tanenbaum (2014).pdf
├── Refactoring - Martin Fowler (1999).pdf
├── Soft Skills - John Z. Sonmez (2014).pdf
└── The pragmatic programmer - Andrew Hunt.pdf
```

# Installation

## Using pip
`pip3 install bookpy`

## Manual Installation
`git clone https://github.com/stsewd/bookpy`

`cd bookpy`

`pip3 install -r requirements.txt`

`pip3 install .`

# Coming Soon
- Rename a file given a specific ISBN.
- Specify_a_separator_between_words.
- Full template support (templates for each element (autors, title, etc.)).
- Specify text case.
- Support for epub files.
