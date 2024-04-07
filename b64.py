import base64

s = "Python"
str_byte = s.encode("ascii")
b64_byte = base64.b64encode(str_byte)

b64_string = b64_byte.decode("ascii")


print(b64_byte,b64_string)

orig_string_byte = base64.b64decode(b64_byte)
orig_string = orig_string_byte.encode("ascii")
print(orig_string_byte,orig_string)