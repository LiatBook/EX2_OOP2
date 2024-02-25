from abc import ABC, abstractmethod


class Observe(ABC):
    def __init__(self):
        self.followers = set()  # who see you

    def add_follower(self, user):  # add to the list that followers(who see me)
        self.followers.add(user)

    def unfollower(self, user):  # remove from the list the followers(who see me)
        self.followers.remove(user)

    def notify(self, msg):
        for member in self.followers:
            member.update(msg)
