import redis
import time
import uuid
from typing import Optional, Dict

redis_server = redis.Redis(host="localhost", port=6379)


SESSION_TTL = 1800


def create_session(user_id: str) -> str:
    """Creates a new user session in Redis and sets the TTL."""

    session_token: str = str(uuid.uuid4())
    login_time: str = time.strftime('%Y-%m-%d %H:%M:%S')
    session_key: str = f"session:{session_token}"

    redis_server.hset(session_key, mapping={
        "user_id": user_id,
        "login_time": login_time,
        "last_activity": login_time
    })

    redis_server.expire(session_key, SESSION_TTL)

    return session_token


def get_session(session_token: str) -> Optional[Dict[str, str]]:
    """Gets session data by token."""

    session_key: str = f"session:{session_token}"
    session_data: Dict[str, str] = redis_server.hgetall(session_key)

    return session_data if session_data else None


def update_activity(session_token: str) -> bool:
    """Updates the last activity time and extends the session time to live (TTL)."""

    session_key: str = f"session:{session_token}"

    if redis_server.exists(session_key):
        new_time: str = time.strftime('%Y-%m-%d %H:%M:%S')
        redis_server.hset(session_key, "last_activity", new_time)
        redis_server.expire(session_key, SESSION_TTL)
        return True
    return False


def delete_session(session_token: str) -> None:
    """Deletes the user session from the database"""

    session_key: str = f"session:{session_token}"

    redis_server.delete(session_key)


token =create_session("user_001")
print("Created token", token)

session = get_session(token)
print("Data of session:", session)

update_activity(token)
print("Session updated successffuly.")

# delete_session(token)

