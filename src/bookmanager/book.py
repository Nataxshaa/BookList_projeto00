from abc import ABC, abstractmethod
from .genre import Genre
class Book(ABC):
    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author
        self._status = "quero ler"
        self.rating = None  # Initialize rating as None
        self.genre = None  # Initialize genre as None

    def mark_as_read(self):
        self._status = "lido"
    
    def mark_as_reading(self):
        self._status = "lendo"

    def mark_as_want_to_read(self):
        self._status = "quero ler"

    @abstractmethod
    def format_info(self) -> str:
        pass 

    @abstractmethod
    def estimated_time(self) -> int:
        pass



class PhysicalBook(Book):
    def __init__(self, title: str, author: str, pages: int):
        super().__init__(title, author)
        self._pages = pages

    def format_info(self) -> str:
        return f"Physical Book: {self._title} by {self._author}, {self._pages} pages, Status: {self._status}"

    def estimated_time(self) -> int:
        return self._pages * 2  # Assuming 2 minutes per page

class EBook(Book):
    def __init__(self, title: str, author: str, pages: int, file_formart: str):
        super().__init__(title, author)
        self.__pages = pages
        self.__file_formart = file_formart

    def format_info(self) -> str:
        return f"E-Book: {self._title} by {self._author}, {self.__pages} pages, Format: {self.__file_formart}, Status: {self._status}"

    def estimated_time(self) -> int:
        return self.__pages * 1  # Assuming 1 minute per page for digital books


class AudioBook(Book):
    def __init__(self, title: str, author: str, duration_minutes: int, narrator: str):
        super().__init__(title, author)
        self.__duration_minutes = duration_minutes
        self.__narrator = narrator

    def format_info(self) -> str:
        return f"Audio Book: {self._title} by {self._author}, Duration: {self.__duration_minutes} minutes, Narrator: {self.__narrator}, Status: {self._status}"

    def estimated_time(self) -> int:
        return self.__duration_minutes


if __name__ == "__main__":
    physical_book = PhysicalBook("1984", "George Orwell", 328)
    print(physical_book.genre)
    physical_book.genre = Genre("Dystopian")
    print(physical_book.genre._name)
    ebook = EBook("The Great Gatsby", "F. Scott Fitzgerald", 180, "PDF")
    audiobook = AudioBook("To Kill a Mockingbird", "Harper Lee", 960, "Sissy Spacek")

    print(physical_book.format_info())
    print(ebook.format_info())
    print(audiobook.format_info())
