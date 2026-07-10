from src.bookmanager import PhysicalBook, EBook, AudioBook
from src.bookmanager.genre import Genre
from src.bookmanager.rating import Rating

def test_start_as_quero_ler():
    book = PhysicalBook("Querido Jonh", "Nicholas Sparks", 200)
    assert book._status == "quero ler"

def test_mark_as_read():
    book = PhysicalBook("Querido Jonh", "Nicholas Sparks", 200)
    book.mark_as_read() 
    assert book._status == "lido"

def test_mark_as_reading():
    book = PhysicalBook("Querido Jonh", "Nicholas Sparks", 200)
    book.mark_as_reading() 
    assert book._status == "lendo"

def test_book_genre():
    book = PhysicalBook("Querido Jonh", "Nicholas Sparks", 200)
    genre = Genre("Romance")
    book.genre = genre
    assert book.genre.get_name() == "Romance"

def test_book_rating():
    book = PhysicalBook("Querido Jonh", "Nicholas Sparks", 200)
    rating = Rating(5, "Great book!")
    book.rating = rating
    assert book.rating.get_stars() == 5
    assert book.rating.get_comment() == "Great book!"

def test_estimated_time_differs():
    physical_book = PhysicalBook("Querido Jonh", "Nicholas Sparks", 200)
    ebook = EBook("Querido Jonh", "Nicholas Sparks", 200, "PDF")
    audiobook = AudioBook("Querido Jonh", "Nicholas Sparks", 120, "Narrator Name")

    assert physical_book.estimated_time() == 400  # 200 pages * 2 minutes
    assert ebook.estimated_time() == 200  # 200 pages * 1 minute
    assert audiobook.estimated_time() == 120  # Duration in minutes
    assert physical_book.estimated_time() != audiobook.estimated_time()