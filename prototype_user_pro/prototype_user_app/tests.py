import unittest
from enum import Enum


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

class TestUser(unittest.TestCase):

    def test_user_implements_clonable_object(self):
        user = User(1, "testuser", "test@example.com", "Test User", 25, UserType.ADMIN)
        self.assertIsInstance(user, ClonableObject, "If the prototype pattern is implemented correctly, the User class should implement the ClonableObject interface")

    def test_user_clone_method_creates_distinct_object(self):
        user = User(1, "testuser", "test@example.com", "Test User", 25, UserType.ADMIN)
        cloned_user = user.cloneObject()
        self.assertIsNot(user, cloned_user, "If the clone method is implemented correctly, it should return a new object")

    def test_registry(self):
        registry = UserPrototypeRegistry()
        self.assertIsNotNone(registry, "If the registry pattern is implemented correctly, the registry should not be None")

        user = User(1, "testuser", "test@example.com", "Test User", 25, UserType.ADMIN)
        registry.addPrototype(user)

        prototype = registry.getPrototype(user.getType())
        self.assertIsNotNone(prototype, "If the clone method is implemented correctly, it should return a non-null object")
        self.assertIs(user, prototype, "If the registry pattern is implemented correctly, the registry should return the same object that was added")

    def test_registry_clone(self):
        user = User(1, "testuser", "test@example.com", "Test User", 25, UserType.ADMIN)
        registry = UserPrototypeRegistry()
        self.assertIsNotNone(registry, "If the registry pattern is implemented correctly, the registry should not be None")

        registry.addPrototype(user)

        # Clone the prototype and validate it's a distinct object with the same values
        cloned_user = registry.clone(user.getType())
        self.assertIsNotNone(cloned_user, "If the clone method is implemented correctly, it should return a non-null object")
        self.assertIsNot(user, cloned_user, "If the clone method is implemented correctly, it should return a new object")
        
        self.assertEqual(user.getUserId(), cloned_user.getUserId(), "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(user.getUsername(), cloned_user.getUsername(), "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(user.getEmail(), cloned_user.getEmail(), "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(user.getDisplayName(), cloned_user.getDisplayName(), "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(user.getAge(), cloned_user.getAge(), "If the clone method is implemented correctly, it should return a new object with the same values as the original object")

if __name__ == '__main__':
    unittest.main()
