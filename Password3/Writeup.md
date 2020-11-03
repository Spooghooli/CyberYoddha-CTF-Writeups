# Password3 Challenge

We are given the file password3.py which looks like this:

```python
import base64

def checkPassword(password):
  if(len(password) != 40):
    return False
  newPass = list(password)
  for i in range(0,40):
    newPass[i] = chr(ord(newPass[i]) ^ 0x55)
  finalPass = "".join(newPass)
  passBytes = finalPass.encode("ascii")
  base64_bytes = base64.b64encode(passBytes) 
  base64_string = base64_bytes.decode("ascii")
  return base64_string == "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="

password = input("Enter password: ")
if(checkPassword(password)):
  print("PASSWORD ACCEPTED\n")
else:
  print("PASSWORD DENIED\n")
```

Looks like some simple obfuscation so I just rewrite the script essentially backwards in order to output the flag:

```python
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
```

Now running this script on IDLE we get the flag: CYCTF{B0th_x0r_@nd_b@s3_64?_th@ts_g0dly}
