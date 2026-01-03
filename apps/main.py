from apps.user_manager import UserManager

if __name__ == "__main__":
    manager = UserManager()
    manager.create_user(1, "Alice", "admin")
    manager.create_user(2, "Bob", "user")
    print(manager.list_users())
