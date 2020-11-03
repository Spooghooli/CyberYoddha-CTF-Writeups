import base64

base64_string = "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="
base64_bytes = base64_string.encode("ascii")
base64_string = base64.b64decode(base64_bytes) 
base64_string = base64_string.decode("ascii")
base64_string = list(base64_string)
for i in range(0,40):
    base64_string[i] = chr(ord(base64_string[i]) ^ 0x55)
base64_string = "".join(base64_string)
print(base64_string)
