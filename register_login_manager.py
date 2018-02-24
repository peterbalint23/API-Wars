import bcrypt
import database_common


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    print(hashed_bytes.decode('utf-8'))
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@database_common.connection_handler
def register(cursor, register, hash):
    cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (%(register)s, %(hash)s);
        """, {'hash': hash, 'register': register})


@database_common.connection_handler
def check_user(cursor,login):
    cursor.execute("""
            SELECT username FROM users
            WHERE  username= %(login)s;
            """, {'login': login})
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def login(cursor,user_name):
    cursor.execute("""
        SELECT password FROM users
        WHERE  username= %(login)s;
        """,{'login':user_name})
    data=cursor.fetchall()
    return data


@database_common.connection_handler
def get_id_by_user_name(cursor, user_name):
    cursor.execute("""
                    SELECT id FROM users
                    WHERE username = %(user_name)s; 
                   """,
                   {'user_name': user_name})
    received_id = cursor.fetchone()
    return received_id
