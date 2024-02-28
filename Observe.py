from abc import ABC, abstractmethod


class Observe(ABC):
    # Constructor for to observe
    def __init__(self):
        self.followers = set()  # who see you
    #add follower
    def add_follower(self, user):  # add to the list that followers(who see me)
        self.followers.add(user)

    #Remove follower
    def unfollower(self, user):  # remove from the list the followers(who see me)
        self.followers.remove(user)

    #update with massage
    def notify(self, msg):
        for member in self.followers:
            member.update(msg)
