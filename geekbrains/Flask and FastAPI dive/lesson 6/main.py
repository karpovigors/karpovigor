import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# Настройка БД
def init_db():
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            product_id INTEGER,
            order_date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
        """)

        conn.commit()

init_db()

# Модели Pydantic
class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class Product(BaseModel):
    name: str
    description: str
    price: float

class Order(BaseModel):
    user_id: int
    product_id: int
    order_date: str
    status: str

# CRUD операции
def create_user(user: User):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)", 
                       (user.first_name, user.last_name, user.email, user.password))
        conn.commit()

def create_product(product: Product):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", 
                       (product.name, product.description, product.price))
        conn.commit()

def create_order(order: Order):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (user_id, product_id, order_date, status) VALUES (?, ?, ?, ?)", 
                       (order.user_id, order.product_id, order.order_date, order.status))
        conn.commit()

def get_user(user_id: int):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = cursor.fetchone()
        return user

def get_product(product_id: int):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
        product = cursor.fetchone()
        return product

def get_order(order_id: int):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
        order = cursor.fetchone()
        return order

def update_user(user_id: int, user: User):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET first_name=?, last_name=?, email=?, password=? WHERE id=?", 
                       (user.first_name, user.last_name, user.email, user.password, user_id))
        conn.commit()

def update_product(product_id: int, product: Product):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET name=?, description=?, price=? WHERE id=?", 
                       (product.name, product.description, product.price, product_id))
        conn.commit()

def update_order(order_id: int, order: Order):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET user_id=?, product_id=?, order_date=?, status=? WHERE id=?", 
                       (order.user_id, order.product_id, order.order_date, order.status, order_id))
        conn.commit()

def delete_user(user_id: int):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()

def delete_product(product_id: int):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        conn.commit()

def delete_order(order_id: int):
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orders WHERE id=?", (order_id,))
        conn.commit()

# FastAPI приложение
app = FastAPI()

@app.post("/users/")
def create_user_endpoint(user: User):
    create_user(user)
    return {"message": "User created successfully"}

@app.get("/users/{user_id}")
def get_user_endpoint(user_id: int):
    return get_user(user_id)

@app.put("/users/{user_id}")
def update_user_endpoint(user_id: int, user: User):
    update_user(user_id, user)
    return {"message": "User updated successfully"}

@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int):
    delete_user(user_id)
    return {"message": "User deleted successfully"}

@app.post("/products/")
def create_product_endpoint(product: Product):
    create_product(product)
    return {"message": "Product created successfully"}

@app.get("/products/{product_id}")
def get_product_endpoint(product_id: int):
    return get_product(product_id)

@app.put("/products/{product_id}")
def update_product_endpoint(product_id: int, product: Product):
    update_product(product_id, product)
    return {"message": "Product updated successfully"}

@app.delete("/products/{product_id}")
def delete_product_endpoint(product_id: int):
    delete_product(product_id)
    return {"message": "Product deleted successfully"}

@app.post("/orders/")
def create_order_endpoint(order: Order):
    create_order(order)
    return {"message": "Order created successfully"}

@app.get("/orders/{order_id}")
def get_order_endpoint(order_id: int):
    return get_order(order_id)

@app.put("/orders/{order_id}")
def update_order_endpoint(order_id: int, order: Order):
    update_order(order_id, order)
    return {"message": "Order updated successfully"}

@app.delete("/orders/{order_id}")
def delete_order_endpoint(order_id: int):
    delete_order(order_id)
    return {"message": "Order deleted successfully"}
