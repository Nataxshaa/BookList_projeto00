class Rating:
    def __init__(self, stars: int, comment: str):
        self.__stars = stars
        self.__comment = comment

    def get_stars(self) -> int:
        return self.__stars

    def get_comment(self) -> str:
        return self.__comment


if __name__ == "__main__":
    r = Rating(5, "Great book!")
    print(r.get_stars())
    print(r.get_comment())