def get_user_by_email(email, mongo):
    return mongo.db.users.find_one({"email": email})

def create_user(name, email, password, mongo):
    return mongo.db.users.insert_one({
        "name": name,
        "email": email,
        "password": password
    })
