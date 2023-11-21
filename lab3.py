class PageSingleton:
    _instance = None
    _page_id = set()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PageSingleton, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def add_page(page_id):
        PageSingleton._page_id.add(page_id)

    @staticmethod
    def get_page_ids():
        return list(PageSingleton._page_id)


class Book:
    def __init__(self, book_type):
        self.book_type = book_type
        self.content = []

    def add_page(self, page_content):
        self.content.append(page_content)


class ScienceBook(Book):
    def __init__(self, book_type):
        super().__init__(book_type)
        self.glossary = []
        self.references = []


class Novel(Book):
    def __init__(self, book_type):
        super().__init__(book_type)
        self.characters = []


class Manual(Book):
    def __init__(self, book_type):
        super().__init__(book_type)
        self.images = []


class BookBuilder:
    def __init__(self, book_type):
        self.book_type = book_type
        self.book = self.create_book_instance()

    def create_book_instance(self):
        if self.book_type == "Science Book":
            return ScienceBook(self.book_type)
        elif self.book_type == "Novel":
            return Novel(self.book_type)
        elif self.book_type == "Manual":
            return Manual(self.book_type)
        else:
            raise ValueError("Incorrect type of book")

    def add_page(self, page_content):
        self.book.add_page(page_content)

    def build(self):
        return self.book


class NovelBuilder(BookBuilder):
    def __init__(self, book_type):
        super().__init__(book_type)
        self.character_ids = []

    def add_characters(self, character_descriptions):
        self.book.characters.extend(character_descriptions)
        self.character_ids.extend(map(id, character_descriptions))
        return self

    def add_character_ids_to_page_singleton(self):
        for character_id in self.character_ids:
            PageSingleton.add_page(character_id)


class ManualBuilder(BookBuilder):
    def __init__(self, book_type):
        super().__init__(book_type)
        self.image_ids = []

    def add_images(self, images):
        self.book.images.extend(images)
        self.image_ids.extend(map(id, images))
        return self

    def add_image_ids_to_page_singleton(self):
        for image_id in self.image_ids:
            PageSingleton.add_page(image_id)


# Example usage
characters = {
    "Luna Lovegood": "A dreamy and eccentric witch from the Harry Potter series who believes in magical creatures like Nargles and Wrackspurts.",
    "Sherlock Holmes": "Famous detective with keen observational and deductive skills.",
    "Aragorn": "Ranger and King of Gondor from The Lord of the Rings, skilled in swordsmanship and leadership.",
    "Daenerys Targaryen": "Mother of Dragons from Game of Thrones, with a strong desire to reclaim the Iron Throne.",
    "Elizabeth Bennet": "Protagonist of Pride and Prejudice, known for her wit and strong sense of individualism."
}

images = {
    "1": "https://www.pinterest.com/pin/cartman--33073378503342646/",
    "2": "https://www.pinterest.com/pin/141230138306880771/",
    "3": "https://www.pinterest.com/pin/604537949995175440/",
    "4": "https://www.pinterest.com/pin/south-park-in-2023--314337249005405425/",
    "5": "https://www.pinterest.com/pin/678284393903261096/",
    "6": "https://www.pinterest.com/pin/72690981479185097/"
}

science_content = ["Content for scientific books", "References", "glossary"]
scientific_book_builder = BookBuilder("Science Book")
scientific_book_builder.add_page(science_content)
scientific_book = scientific_book_builder.build()

novel_content = [f"{key}: {desc}" for key, desc in characters.items()]
novel_builder = NovelBuilder("Novel")
novel_builder.add_characters(novel_content)
novel_builder.add_character_ids_to_page_singleton()
novel = novel_builder.build()

manual_content = list(images.values())
manual_builder = ManualBuilder("Manual")
manual_builder.add_images(manual_content)
manual_builder.add_image_ids_to_page_singleton()
manual = manual_builder.build()

page_ids = PageSingleton.get_page_ids()

print("Science Book:")
print(vars(scientific_book))
print("\nNovel:")
print(vars(novel))
print("\nManual:")
print(vars(manual))
print("\nUnique Page IDs:", page_ids)
