class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self.title = title  # Using property setter
        self.author = author  # Using property setter
        self.magazine = magazine  # Using property setter
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("Title must be a string")
        elif not (5 <= len(new_title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = new_magazine

    def __repr__(self):
        return f'<Article: author={self.author.name}, magazine={self.magazine.name}, title="{self.title}">'


class Author:
    def __init__(self, name):
        self._name = None
        self.name = name  # Using property setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if self._name is not None:
            raise AttributeError("Name cannot be changed")
        elif not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        elif len(new_name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = new_name

    def articles(self):
        return [article for article in Article.all_articles if self == article.author]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()}) if self.magazines() else None

    def __repr__(self):
        return f'<Author: name={self.name}>'


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # Using property setter
        self.category = category  # Using property setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        elif not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Category must be a string")
        elif len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = new_category

    def articles(self):
        return [article for article in Article.all_articles if self == article.magazine]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        return [author for author, count in authors.items() if count > 2]

    def __repr__(self):
        return f'<Magazine: name={self.name}, category={self.category}>'
