class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
libro = Book("The Runner","John")
aklat = Book("One Bleach", "Matt")
print(libro.title, libro.author)
print(aklat.title, aklat.author)
del libro.author
#libro.author = " "

print(libro.title, libro.author)
print(aklat.title, aklat.author)

