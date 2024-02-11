from enum import Enum
from copy import deepcopy

class UserType(Enum):
    ADMIN = 1
    READER = 2
    WRITER = 3

class ClonableObject:
    def cloneObject(self):
        return deepcopy(self)

class User(ClonableObject):
    def __init__(self, userId, username, email, displayName, age, type):
        self.userId = userId
        self.username = username
        self.email = email
        self.displayName = displayName
        self.age = age
        self.type = type

    def getUserId(self):
        return self.userId

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def getDisplayName(self):
        return self.displayName

    def getAge(self):
        return self.age

    def getType(self):
        return self.type

    def cloneObject(self):
        return User(self.userId, self.username, self.email, self.displayName, self.age, self.type)

class UserPrototypeRegistry:
    def __init__(self):
        self.users = {}

    def addPrototype(self, user):
        self.users[user.getType()] = user

    def getPrototype(self, type):
        return self.users.get(type)

    def clone(self, type):
        return self.users[type].cloneObject()
