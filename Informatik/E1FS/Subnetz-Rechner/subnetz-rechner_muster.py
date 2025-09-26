def main():
    subnet = input("Bitte geben Sie IP und Subnetz in CIDR-Notation ein: ")
    ip, suffix = subnet.split('/')
    mask = int(suffix)
    split = ip.split('.')
    binary_split = []
    for i in split:
        binary_split.append(decimal_to_binary(i))
    binary_ipv4 = ''.join(binary_split)
    na = network_address_binary(binary_ipv4, suffix)
    ba = broadcast_address_binary(binary_ipv4, suffix)
    print(na)
    print(ba)
    ba_chunks = split_into_chunks(ba)
    print(network_address_decimal(na))
    print(broadcast_address_decimal(ba))

def network_address_decimal(network_address_binary):
    na_chunks = split_into_chunks(network_address_binary)
    na_decimal_chunks = []
    for i in range(0, 4):
        na_decimal_chunks.append(str(binary_to_decimal(na_chunks[i])))
    return '.'.join(na_decimal_chunks)

def broadcast_address_decimal(broadcast_address_binary):
    ba_chunks = split_into_chunks(broadcast_address_binary)
    ba_decimal_chunks = []
    for i in range(0, 4):
        ba_decimal_chunks.append(str(binary_to_decimal(ba_chunks[i])))
    return '.'.join(ba_decimal_chunks)

def network_address_binary(binary_ipv4, suffix):
    fixed_part = binary_ipv4[:int(suffix)]
    for i in range(0,32-int(suffix)):
        fixed_part += '0'
    return fixed_part

def broadcast_address_binary(binary_ipv4,suffix):
    fixed_part = binary_ipv4[:int(suffix)]
    for i in range(0,32-int(suffix)):
        fixed_part += '1'
    return fixed_part

def split_into_chunks(s):
    return [s[i:i+8] for i in range(0, len(s), 8)]

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(n):
    return bin(int(n))[2:].zfill(8)

if __name__ == "__main__":
    main()
