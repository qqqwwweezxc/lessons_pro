from user_manager import UserManager
import pytest

@pytest.fixture
def user_manager():
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um

def test_add_user(user_manager):
    user_manager.add_user("Petya", 20)
    users = user_manager.get_all_users()
    assert any(u["name"] == "Petya" and u["age"] == 20 for u in users)
    assert len(users) == 3

def test_remove_user(user_manager):
    user_manager.remove_user("Alice")
    users = user_manager.get_all_users()
    assert all(u["name"] != "Alice" for u in users)
    assert len(users) == 1

def test_get_all_users(user_manager):
    users = user_manager.get_all_users()
    assert len(users) == 2
    names = [u["name"] for u in users]
    assert "Alice" in names and "Bob" in names

def test_skip_condition(user_manager):
    if len(user_manager.get_all_users()) < 3:
        pytest.skip("Skipping test because there are less than 3 users")
    assert len(user_manager.get_all_users()) >= 3

