from apps.user_service import add_user
from apps.file_store import write_users

def reset():
    write_users([])

def test_add_user():
    reset()
    users = add_user("alice", "user")
    assert users[0]["username"] == "alice"

if __name__ == "__main__":
    test_add_user()
    print("Basic tests passed")
