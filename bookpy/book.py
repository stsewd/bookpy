class Book():
    def __init__(self, isbn, title, authors, year):
        self._authors = Book._get_authors(authors)
        self._title = title
        self._short_title = Book._get_short_title(title)
        self._isbn = isbn
        self._year = year

    def authors(self, template="{name}", sep=", ", empty=True):
        if not self._authors and empty:
            return ""
        return sep.join(
            template.format(**author)
            for author in self._authors
        )

    def main_author(self, template="{name}", empty=True):
        if not self._get_main_author and empty:
            return ""
        return template.format(**self._get_main_author())

    def _get_main_author(self):
        return self._authors[0] if self._authors else Book._get_author("")

    def title(self, template="{title}", empty=True):
        if not self._title and empty:
            return ""
        return template.format(
            title=self._title
        )

    def short_title(self, template="{short_title}", empty=True):
        if not self._short_title and empty:
            return ""
        return template.format(
            short_title=self._short_title
        )

    def year(self, template="{year}", empty=True):
        if not self._year and empty:
            return ""
        return template.format(
            year=self._year
        )

    def isbn(self, template="{isbn}", empty=True):
        if not self._isbn and empty:
            return ""
        return template.format(
            isbn=self._isbn
        )

    def name(self, template=None, **kwargs):
        if not template:  # Load defaulf template
            template = "{short_title}{main_author}{year}"
            kwargs = {
                'year': " ({year})",
                'main_author': " - {name}",
            }
        kwargs = self._parse_args(kwargs)
        return template.format(**kwargs)

    def _parse_args(self, k):
        title_f = k.get('title', "{title}")
        short_title_f = k.get('short_title', "{short_title}")
        main_author_f = k.get('main_author', "{name}")
        authors_f = k.get('authors', "{name}")
        sep_authors = k.get('sep_authors', ", ")
        isbn_f = k.get('isbn', "{isbn}")
        year_f = k.get('year', "{year}")

        return {
            'title': self.title(title_f),
            'short_title': self.short_title(short_title_f),
            'main_author': self.main_author(main_author_f),
            'authors': self.authors(authors_f, sep=sep_authors),
            'isbn': self.isbn(isbn_f),
            'year': self.year(year_f),
        }

    @staticmethod
    def _get_authors(authors):
        authors = [Book._get_author(author_name) for author_name in authors]
        return authors

    @staticmethod
    def _get_author(author_name):
        names = author_name.split()
        author = {
            'name': author_name,
            'first_name': names[0],
            'last_name': names[-1] if len(names) > 1 else "",
        }
        return author

    @staticmethod
    def _get_short_title(title):
        return title.split(':')[0]

    def __str__(self):
        return "{title}{main_author}{year}".format(
            title=self.title(),
            main_author=self.main_author(" - {name}"),
            year=self.year(" ({year})")
        )
