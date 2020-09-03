class Shelf():
    def __init__(self):
        self.books = []

    def push (self, book):
        self.books.append(book)

    def pop (self):
        self.books.pop()

    def is_empty(self):
        return self.books == []

    def get_shelf(self):
        return self.books

    def peek (self):
        if self.is_empty() == False:
            return self.books[-1]

s = Shelf()
print(s.is_empty())
s.push('Harry Potter')
s.push('Million $')
s.push('Rich dad poor dad')
print(s.is_empty())
print(s.get_shelf())
print(s.peek())