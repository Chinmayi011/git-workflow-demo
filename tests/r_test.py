from app.user_manager import UserManager

def run_tests():
    manager = UserManager()

    manager.create_user(1, "Alice", "admin")
    manager.create_user(2, "Bob", "user")

    users = manager.list_users()
    assert len(users) == 2

    try:
        manager.create_user(1, "Duplicate", "user")
        assert False
    except ValueError:
        pass

    manager.delete_user(1)
    assert 1 not in manager.list_users()

    print("User management tests passed")

if __name__ == "__main__":
    run_tests()
