from Post import PostFactory
from Observe import Observe
from Member import Member


class User(Observe, Member):
    #Constructor for the user
    def __init__(self, name, password):
        Observe.__init__(self)
        self.__name = name
        self.password = password
        self.__followers = set()
        self.__posts = []
        self.online = True
        self.notifications = []

    # *args solution the problem of how much arguments this function receive
    #This function responsible to publish post used post factory
    def publish_post(self, type, *args):
        post_factory = PostFactory()
        new_post = post_factory.create_post(self, type, *args)
        self.__posts.append(new_post)

        self.notify(f"{self.str_name()} has a new post")
        return new_post

    #This function print notifications for the user
    def print_notifications(self):
        print(self.str_name() + "'s notifications:")
        for x in self.notifications:
            print(x)

    #User follow another users
    def follow(self, user):
        if user == self:
            raise ValueError("Cannot follow yourself")
        user.__followers.add(self)
        user.add_follower(self)
        print(self.__name + " started following " + user.__name)

    #User unfollow another users
    def unfollow(self, user):
        user.__followers.remove(self)
        user.unfollower(self)
        print(self.__name + " unfollowed " + user.__name)

    #update for users
    def update(self, msg):
        self.notifications.append(msg)

    #string to string function to user
    def __str__(self):
        return (f"User name: {self.__name},"
                f" Number of posts: {len(self.__posts)}, Number of followers: {len(self.__followers)}")

    #Give me the name of user with function
    def str_name(self):
        return (f"{self.__name}")
