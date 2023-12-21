def extract_sequences(data):
    sequences = []

    index = 0
    while index < len(data):
        if index + 11 < len(data):
            if data[index] == 0x00:
                header = data[index + 1:index + 3]
                dcl = data[index + 3]
                pdu = data[index + 4:index + 12]
                sequences.append((header, dcl, pdu))
                index += 12
            else:
                index += 1
        else:
            break

    return sequences

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

def combine_payloads(payloads, headers, dcls, original_payload):
    combined_payload = bytearray()

    for i, (header, dcl, payload) in enumerate(zip(headers, dcls, payloads)):
        combined_payload.extend(bytes([0x00, *header, dcl]))

        combined_payload.extend(payload)


    missing_bytes = len(original_payload) - len(combined_payload)
    combined_payload.extend(original_payload[-missing_bytes:])

    return combined_payload

if __name__ == '__main__':
    data = bytearray.fromhex("00 06 02 08 80 00 00 00 00 00 00 00 00 05 D0 08 FF 60 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 00 00 00 00 10 C7 77 8A 70 AB AF 88 2A 8C")

    result = extract_sequences(data)

    print("Old Payload:", format_sequence(data))

    payload1 = result[0][2]
    payload2 = result[1][2]
    payload3 = result[2][2]

    old_payload1 = bytearray(payload1)
    old_payload2 = bytearray(payload2)
    old_payload3 = bytearray(payload3)

    set_value(payload1, byte_position=2, bit_position=5, size=2, new_value=2)
    set_value(payload2, byte_position=4, bit_position=7, size=6, new_value=45)
    set_value(payload3, byte_position=5, bit_position=2, size=1, new_value=1)


    combined_payload = combine_payloads([payload1, payload2, payload3, result[-1][2]],
                                        [header for header, _, _ in result[:-1]],
                                        [dcl for _, dcl, _ in result[:-1]],
                                        data)

    print("New Payload:", format_sequence(combined_payload))
