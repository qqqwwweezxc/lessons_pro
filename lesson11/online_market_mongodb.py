import datetime
from pymongo import MongoClient, ASCENDING


client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

collection_products = db["products"]
collection_orders = db["orders"]


collection_products.delete_many({})
collection_orders.delete_many({})


collection_products.insert_many([
    {"name": "Iphone", "price": 2000, "category": "Electronics", "stock": 150},
    {"name": "AirPods", "price": 500, "category": "Electronics", "stock": 300},
    {"name": "Office chair", "price": 150, "category": "Furniture", "stock": 10},
    {"name": "Bookshelf", "price": 100, "category": "Furniture", "stock": 50},
    {"name": "Macbook", "price": 3500, "category": "Electronics", "stock": 0}
])


collection_orders.insert_many([
    {
        "orderID": "10001",
        "customer": "Ivan Ivanov",
        "products": [
            {"productName": "Iphone", "quantity": 3},
            {"productName": "AirPods", "quantity": 1}
        ],
        "totalAmount": 6500,
        "orderDate": datetime.datetime.now()
    },
    {
        "orderID": "10002",
        "customer": "Anna Ivanovna",
        "products": [
            {"productName": "Office chair", "quantity": 4},
            {"productName": "Bookshelf", "quantity": 2}
        ],
        "totalAmount": 800,
        "orderDate": datetime.datetime.now() - datetime.timedelta(days=50)
    },
    {
        "orderID": "10003",
        "customer": "Petya Petrov",
        "products": [
            {"productName": "Iphone", "quantity": 1},
            {"productName": "AirPods", "quantity": 2}
        ],
        "totalAmount": 3000,
        "orderDate": datetime.datetime.now()
    }
])


thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
recent_orders = collection_orders.find({
    "orderDate": {"$gte": thirty_days_ago}
})

print("Orders in the last 30 days:")
for order in recent_orders:
    print(f"- {order['orderID']} from {order['customer']} "
          f"for the amount {order['totalAmount']}")


collection_products.update_one({"name": "Iphone"}, {"$inc": {"stock": -3}})
collection_products.update_one({"name": "AirPods"}, {"$inc": {"stock": -1}})

updated_product_iphone = collection_products.find_one({"name": "Iphone"})
updated_product_airpods = collection_products.find_one({"name": "AirPods"})

print(f"The remaining Iphones in stock: {updated_product_iphone['stock']} pcs.")
print(f"The remaining AirPodses in stock: {updated_product_airpods['stock']} pcs.")


deleted_result = collection_products.delete_many({"stock": 0})
print(f"Removed products (out of stock): {deleted_result.deleted_count}")


pipeline_total_products = [
    {"$match": {"orderDate": {"$gte": thirty_days_ago}}},
    {"$unwind": "$products"},
    {"$group": {
        "_id": None,
        "totalProductsSold": {"$sum": "$products.quantity"}
    }}
]
total_products = list(collection_orders.aggregate(pipeline_total_products))
if total_products:
    print(f"Total items sold in 30 days: {total_products[0]['totalProductsSold']}")


pipeline_customer_spent = [
    {"$match": {"customer": "Anna Ivanovna"}},
    {"$group": {
        "_id": "$customer",
        "totalSpent": {"$sum": "$totalAmount"},
        "ordersCount": {"$sum": 1}
    }}
]
customer_spent = list(collection_orders.aggregate(pipeline_customer_spent))
if customer_spent:
    data = customer_spent[0]
    print(f"Customer {data['_id']} spent {data['totalSpent']} UAH "
          f"(Number of orders: {data['ordersCount']})")


collection_products.create_index([("category", ASCENDING)])
indexes = collection_products.index_information()

print("Existing indexes in the products collection:")
for key, value in indexes.items():
    print(f"- {key}: {value}")