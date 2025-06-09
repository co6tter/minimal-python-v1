class Post:
    _count = 0

    def __init__(self, text):
        self._text = text
        self._likes = 0
        Post._count += 1

    @classmethod
    def show_count(cls):
        print(f"{cls._count} instances created")

    def show(self):
        print(f"{self._text} - {self._likes}")

    def like(self):
        self._likes += 1

    # def set_likes(self, num):
    #     self._likes = num

    # def get_likes(self):
    #     return self._likes

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, num):
        self._likes = num


class SponsoredPost(Post):
    def __init__(self, text, sponsor):
        super().__init__(text)
        self._sponsor = sponsor

    def show(self):
        print(f"{self._text} - {self._likes} sponsored by {self._sponsor}")


posts = [
    Post("Hello"),
    Post("Hi"),
    SponsoredPost("Hey", "hello-newworld")
]

# posts[0].set_likes(100)
# print(posts[0].get_likes())

# @propertyを使うことで直接プロパティにアクセスしているように書ける
posts[0].likes = 100
print(posts[0].likes)

for post in posts:
    post.show()

Post.show_count()


class HtmlHelper:
    @staticmethod
    def to_h1(str):
        return f"<h1>{str}</h1>"

    @staticmethod
    def to_p(str):
        return f"<p>{str}</p>"


print(HtmlHelper.to_h1("Hello"))
print(HtmlHelper.to_p("Wow"))
