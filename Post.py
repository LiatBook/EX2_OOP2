from abc import ABC
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Observe import Observe


class Post(ABC):
    obs = Observe()

    def __init__(self, creator):
        self._likes = set()
        self.comments = []
        self._creator = creator
        if not self._creator.online:
            raise Exception("user can't create post without log in")

    def get_creator(self):
        return self._creator

    # def get_user(self):
    #     return self._creator

    def like(self, user):
        if not user.online:
            raise Exception("user can't do like without log in")
        if self._creator.str_name() != user.str_name():
            self._likes.add(user)
            msg = user.str_name() + " liked your post"
            self._creator.update(msg)
            print(f"notification to {self._creator.str_name()}: {user.str_name()} liked your post")

    def comment(self, user, msg):
        if not user.online:
            raise Exception("user can't do comment without log in")
        new_comment = (user, msg)
        self.comments.append(new_comment)
        msg1 = user.str_name() + " commented on your post"
        self._creator.update(msg1)
        print("notification to " + self._creator.str_name() + ": " +
              user.str_name() + " commented on your post: " + msg)


class PostFactory:

    def create_post(self, user, post_type, *args):
        if post_type == "Text":
            return TextPost(user, *args)
        elif post_type == "Image":
            return ImagePost(user, *args)
        elif post_type == "Sale":
            return SalePost(user, *args)
        else:
            raise ValueError("Invalid post type")


class TextPost(Post):
    def __init__(self, user, content):
        super().__init__(user)
        self._content = content
        print(self._creator.str_name() + " published a post:\n" + '"' + self._content + '"' + "\n")

    def __str__(self):
        return self._creator.str_name() + " published a post:\n" + '"'+ self._content + '"'+ "\n"


class ImagePost(Post):
    def __init__(self, user, path):
        super().__init__(user)
        self._path = path
        print(user.str_name() + " posted a picture""\n")

    def __str__(self):
        return self._creator.str_name() + " posted a picture\n"

    def display(self):
        img = mpimg.imread(self._path)
        imgplot = plt.imshow(img)
        plt.show()
        print("Shows picture")


class SalePost(Post):
    def __init__(self, user, cur_product, price, place):
        super().__init__(user)
        # self._product = []
        self._cur_product = cur_product
        self._price = price
        self._place = place

        print(user.str_name() + " posted a product for sale:\n" + "For sale! " + self._cur_product +
              ", price: " + str(self._price) + ", pickup from: " + self._place + "\n")

    def discount(self, rebate, password):
        if password == self.get_creator().password:
            self._price = self._price * (1 - rebate / 100)
            print("Discount on " + self.get_creator().str_name() + " product! the new price is: 37800.0")

    def sold(self, password):
        if password == self.get_creator().password:
            _cur_product = None
            print(self.get_creator().str_name() + "'s product is sold")

    def __str__(self):
        if self._cur_product is not None:
            return (self.get_creator().str_name() + " posted a product for sale:\n"
                    + "Sold! " + self._cur_product +
                    ", price: " + str(self._price) + ", pickup from: " + self._place + "\n")
        else:
            return (self.get_creator().str_name() + " posted a product for sale:\n"
                                                     "For sale! " + self._cur_product +
                    ", price: " + str(self._price) + ", pickup from: " + self._place + "\n")

# if self._creator._strname_() !=user._strname_():
