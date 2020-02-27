from stack import Stack

def convert_int_to_bin(dec_num):
    s = Stack()
    while dec_num > 0:
        s.push(str(dec_num % 2))
        dec_num = dec_num // 2

    bits = ""
    while not s.is_empty():
        bits += s.pop()

    print(bits)


convert_int_to_bin(242)