import hashlib

# primer mensaje
message1 = "Python es genial"

hash1 = hashlib.sha256(message1.encode())

digest1 = hash1.hexdigest()
print(f"Hash para '{message1}': {digest1}")

# segundo mensaje
message2 = "Python no es genial"

hash2 = hashlib.sha256(message2.encode())

digest2 = hash2.hexdigest()
print(f"Hash para '{message2}': {digest2}")
