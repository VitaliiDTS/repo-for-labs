class Book:


    """
    get and show info about book
    """
    def __init__(self, title, price, number_of_pages, author, quantity, number_of_sales):
        self.title = title
        self.price = price
        self.number_of_pages = number_of_pages
        self.author = author
        self.__quantity = quantity
        self.number_of_sales = number_of_sales

    def get_price(self):
        print(f"price of this book --> {self.price}")

    def get_number_of_pages(self):
        print(f"number of pages im this book --> {self.nuber_of_pages}")

    def get_author(self):
        print(f"author of this book --> {self.author}")

    def get_quantity(self):
        print(f"quantity --> {self.__quantity}")

    def get_number_of_sales(self):
        print(f"number of sales --> {self.number_of_sales}")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"


class BookShop:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"book  was added")

    def remove_book(self, book):
        self.books.remove(book)
        print("book was removed")

    def sort_by_price_key(self , book):
        return book.price

    def top_books_by_price(self, n):
        sorted_books = sorted(self.books, key = self.sort_by_price_key  ,  reverse=True)
        return sorted_books[:n]

    def sort_by_sales_key(self , book):
        return book.number_of_sales

    def top_books_by_sales(self, n):
        sorted_books = sorted(self.books, key = self.sort_by_sales_key  ,  reverse=True)
        return sorted_books[:n]


if __name__ == "__main__":
    book1 = Book("Harry Potter", 20, 300, "Joan Rouling",
    14, 100)
    book2 = Book("Tom Sawyer", 19, 33, "Mark Twen",
    56, 30)
    book3 = Book("Toreadors from Vasyukivka",27, 33, "Vsevolod Nestayko",
    88, 57)

    bookshop = BookShop()
    bookshop.add_book(book1)
    bookshop.add_book(book2)
    bookshop.add_book(book3)

    print("#########################################")

    print("book in the bookshop")
    for book in bookshop.books:
        print(book)

    print("#########################################")

    print("top books by price:")
    top_books_by_price = bookshop.top_books_by_price(3)
    for book in top_books_by_price:
        print(book)

    print("#########################################")

    print("top books by sales:")
    top_books_by_sales = bookshop.top_books_by_sales(3)
    for book in top_books_by_sales:
        print(book)

    print("#########################################")
    bookshop.remove_book(book2)









