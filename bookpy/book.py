class Book():
    def __init__(self, isbn, title, authors, year):
        self._authors = Book._get_authors(authors)
        self._title = title
        self._short_title = Book._get_short_title(title)
        self._isbn = isbn
        self._year = year

    def authors(self, pattern="{name}", sep=", ", empty=False):
        if not self._authors and empty:
            return ""
        return sep.join(
            pattern.format(**author)
            for author in self._authors
        )

    def main_author(self, pattern="{name}", empty=False):
        if not self._get_main_author and empty:
            return ""
        return pattern.format(**self._get_main_author())

    def _get_main_author(self):
        return self._authors[0] if self._authors else Book._get_author("")

    def title(self, pattern="{title}", empty=False):
        if not self._title and empty:
            return ""
        return pattern.format(
            title=self._title
        )

    def short_title(self, pattern="{short_title}", empty=False):
        if not self._short_title and empty:
            return ""
        return pattern.format(
            short_title=self._short_title
        )

    def year(self, pattern="{year}", empty=False):
        if not self._year and empty:
            return ""
        return pattern.format(
            year=self._year
        )

    def isbn(self, pattern="{isbn}", empty=False):
        if not self._isbn and empty:
            return ""
        return pattern.format(
            isbn=self._isbn
        )

    def name(self, pattern, **kwargs):
        return str(self)  # TODO Add global separator for blank spaces

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
        return "{title} - {main_author} {year}".format(
            title=self.title(),
            main_author=self.main_author(empty=True),
            year=self.year("({year})", True)
        )
