from polymorphism_demo import Shape, Rectangle, Circle
from book_class import Book


def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)             # __str__
    print(repr(my_book))       # __repr__
    del my_book                # __del__


if __name__ == "__main__":
    main()


def main():
    shapes = [Rectangle(10, 5), Circle(7)]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    main()
