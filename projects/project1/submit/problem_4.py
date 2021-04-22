class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if user in group.users:
        return True
    else:
        for group in group.groups:
            if is_user_in_group(user, group):
                return True

    return False


def main():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    ### Should print True as sub_child_user is under parent
    print(is_user_in_group(sub_child_user, parent))

    ### Should print True as sub child user is under child
    print(is_user_in_group(sub_child_user, child))

    ### Should print true as sub_child_user is in sub_child group
    print(is_user_in_group(sub_child_user, sub_child))

    ### Should print false as no name is given
    print(is_user_in_group("", parent))


if __name__ == "__main__":
    main()