import json
import random
import requests
import time

DATA = {"users": [], "orders": []}
CACHE = {}

LOG_FILE = "system.log"
API = "https://example.com/notify"


def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.time()} {message}\n")


def validate_user(data):
    if "name" not in data or "email" not in data:
        print("Invalid user data")
        return False
    return True


def create_user(data):
    uid = random.randint(1, 999999)

    user = {
        "id": uid,
        "name": data["name"],
        "email": data["email"]
    }

    DATA["users"].append(user)
    log_message(f"user created {user['name']}")

    return user


def calculate_discount(amount):
    if amount > 1000:
        return amount * 0.1
    elif amount > 500:
        return amount * 0.05
    else:
        return 0


def create_order(user_id, amount):
    discount = calculate_discount(amount)

    order = {
        "user_id": user_id,
        "amount": amount,
        "discount": discount,
        "ts": time.time()
    }

    DATA["orders"].append(order)
    log_message(f"order created {user_id}")

    return order


def save_data():
    with open("users.json", "w") as f:
        json.dump(DATA["users"], f)

    with open("orders.json", "w") as f:
        json.dump(DATA["orders"], f)


def notify_user(email):
    try:
        requests.post(API, json={"email": email, "msg": "order"})
    except requests.RequestException:
        pass
def process_user(data, cache_key=None, notify=True):

    if data is None:
        return

    if isinstance(data, list):
        for item in data:
            process_user(item)
        return

    if not validate_user(data):
        return

    user = create_user(data)

    amount = data.get("amount", 0)

    order = create_order(user["id"], amount)

    if notify:
        notify_user(user["email"])

    save_data()

    if cache_key:
        CACHE.setdefault(cache_key, []).append(user)

    if user["id"] % 2 == 0:
        log_message("even user")
    else:
        log_message("odd user")

    CACHE[str(user["id"])] = amount * 2

    return user, order


def show_data(option=None):

    if option == "users":
        for user in DATA["users"]:
            print(user)

    elif option == "orders":
        for order in DATA["orders"]:
            print(order)

    else:
        for user in DATA["users"]:
            print(user)

        for order in DATA["orders"]:
            print(order)


def load_data():

    try:
        with open("users.json") as f:
            DATA["users"] = json.load(f)
    except:
        print("Error")

    try:
        with open("orders.json") as f:
            DATA["orders"] = json.load(f)
    except:
        print("Error")


def random_task():

    for i in range(5):

        if i % 2 == 0:
            amount = i * 200
        else:
            amount = i * 50

        process_user({
            "name": f"User{i}",
            "email": f"u{i}@test.com",
            "amount": amount
        })


load_data()

data = [
    {"name": "John", "email": "john@test.com", "amount": 1200},
    {"name": "Alice", "email": "alice@test.com", "amount": 300},
]

process_user(data)

random_task()

show_data()    


