class UserManager:
    def __init__(self):
        self._users = {}

    def create_user(self, user_id, name, role):
        if not user_id or not name:
            raise ValueError("User ID and name are required")

        if role not in ("admin", "user"):
            raise ValueError("Invalid role")

        if user_id in self._users:
            raise ValueError("User already exists")

        self._users[user_id] = {
            "name": name,
            "role": role
        }

    def delete_user(self, user_id):
        if user_id not in self._users:
            raise ValueError("User not found")

        del self._users[user_id]

    def list_users(self):
        return self._users
