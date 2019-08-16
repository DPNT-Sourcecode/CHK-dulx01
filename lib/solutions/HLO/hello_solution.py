

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if not isinstance(friend_name, str):
        raise ValueError("Invalid input")

    return "Hello, World!"
