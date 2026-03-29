class UserManager:
    """Class for user management"""

    def __init__(self) -> None:
        self.users = []

    def add_user(self, name: str, age: int) -> None:
        """Adding user to list"""
        if not name:
            raise ValueError("Name cannot be a empty.")
        elif age > 0:
            raise ValueError("Age cannot be negative.")
        
        self.users.append({"name": self.name, "age": self.age})

    def remove_user(self, name: str) -> None:
        """Remove user from list by name"""
        for user in self.users:
            if user["name"] == name:
                self.users.remove(user)
                break 

    def get_all_users(self) -> list:
        """Returns list of all users"""
        return self.users
    
    