class Shelf():
    def __init__(self):
        self.books = []

    def push(self, book):
        self.books.append(book)

    def pop (self):
         return self.books.pop()

    def get_stack (self):
        return self.books

    def is_empty(self):
        return self.books == []

    def peek(self):
        if self.is_empty != []: 
            return self.books[-1]    

s = Shelf()
print(s.is_empty())
s.push('Harry Poter')
s.push('The Millionaire') 
s.push('Rich Dad Poor Dad')
print(s.is_empty())
print(s.get_stack())
print(s.peek())  