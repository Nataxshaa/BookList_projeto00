class Genre:
    def __init__(self, name):
        self._name = name

if __name__ == "__main__":
    g = Genre("Fiction")
    print(g._name)