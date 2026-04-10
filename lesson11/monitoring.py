from pymongo import MongoClient
import time

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["products"]


status = client.admin.command("serverStatus")
print("=== Server Status ===")
print(f"MongoDB version: {status['version']}")
print(f"Uptime: {status['uptime']}s")
print(f"Connections: {status['connections']['current']}")


stats = db.command("dbStats")
print("\n=== DB Stats ===")
print(f"Collections: {stats['collections']}")
print(f"Documents: {stats['objects']}")
print(f"Data size: {stats['dataSize']} bytes")
print(f"Indexes: {stats['indexes']}")


ops = client.admin.current_op()
print("\n=== Current Operations ===")
for op in ops.get("inprog", [])[:5]:
    print(f"  {op.get('op', '?')} on {op.get('ns', '?')}")


db.command("profile", 1, slowms=100)
print("\n=== Profiling enabled (slowms=100) ===")


start = time.time()
collection.insert_many([
    {"name": f"User_{i}", "email": f"u{i}@test.com", "age": 20 + i}
    for i in range(1000)
])
elapsed = time.time() - start
print(f"Insert 1000 docs: {elapsed:.3f}s")


collection.create_index("email")
plan = collection.find({"email": "u500@test.com"}).explain("executionStats")
print(f"\n=== Query Explain ===")
print(f"Documents examined: {plan['executionStats']['totalDocsExamined']}")
print(f"Execution time: {plan['executionStats']['executionTimeMillis']}ms")


cstats = db.command("collStats", "users")
print(f"\n=== Collection 'users' Stats ===")
print(f"Documents: {cstats['count']}")
print(f"Indexes: {len(cstats['indexSizes'])}")
for idx, size in cstats['indexSizes'].items():
    print(f"  {idx}: {size} bytes")

client.close()

