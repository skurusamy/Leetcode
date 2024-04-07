import base64

s = "hello"

s_bytes = s.encode("ascii")

b64_bytes = base64.b64encode(s_bytes)

b_64String = b64_bytes.decode("ascii")

print(f'Encode => {s_bytes},{b64_bytes},{b_64String}')

decode_byte = b_64String.encode("ascii")

decode_b4_byte = base64.b64decode(decode_byte)

original_string = decode_b4_byte.decode("ascii")


print(f'Decode => {decode_byte},{decode_b4_byte},{original_string}')