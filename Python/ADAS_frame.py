def set_value(payload, byte_position, bit_position, size, new_value):
    byte_index = byte_position
    bit_index = bit_position
    mask = (1 << size) - 1

    payload_value = int.from_bytes(payload[byte_index:byte_index + (size + 7) // 8])
    payload_value &= ~(mask << (bit_index - size + 1) % 8)

    new_value &= mask
    payload_value |= new_value << (bit_index - size + 1) % 8

    payload[byte_index:byte_index + (size + 7) // 8] = payload_value.to_bytes((size + 7) // 8)

def format_sequence(sequence):
    formatted_sequence = ' '.join(format(byte, '02X') for byte in sequence)
    return formatted_sequence


if __name__ == '__main__':
    data = bytearray.fromhex("00 06 02 08 80 00 00 00 00 00 00 00 00 05 D0 08 FF 60 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 00 00 00 00 10 C7 77 8A 70 AB AF 88 2A 8C")

    print("Old:", format_sequence(data))

    payload1 = data[4:12]
    payload2 = data[16:24]
    payload3 = data[28:36]

    set_value(payload1, byte_position=2, bit_position=5, size=2, new_value=2)
    set_value(payload2, byte_position=4, bit_position=7, size=6, new_value=45)
    set_value(payload3, byte_position=5, bit_position=2, size=1, new_value=1)

    data[4:12] = payload1
    data[16:24] = payload2
    data[28:36] = payload3

    print("New:", format_sequence(data))
