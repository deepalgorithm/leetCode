import hashlib

input_data = input()

encode_data = input_data.encode()
result = hashlib.sha256(encode_data).hexdigest()
print(result)