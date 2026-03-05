from database import create_connection
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def signup(name,email,password):

    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
        "INSERT INTO users(name,email,password) VALUES(?,?,?)",
        (name,email,hash_password(password))
        )

        conn.commit()
        conn.close()
        return True

    except:
        return False


def login(email,password):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
    "SELECT * FROM users WHERE email=? AND password=?",
    (email,hash_password(password))
    )

    user = cursor.fetchone()

    conn.close()

    return user