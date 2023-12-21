def extract_value(payload, byte_position, bit_position, size):
    byte_index = byte_position
    bit_index = bit_position
    mask = (1 << size) - 1

    value = int.from_bytes(payload[byte_index:byte_index + (size + 7) // 8])

    value >>= (bit_index - size + 1 ) % 8

    value &= mask

    return value

if __name__ == '__main__':
    payload1 = bytearray.fromhex("60 20 45 6C FE 3D 4B AA")

    clim_value_payload1 = extract_value(payload1, byte_position=5, bit_position=7, size=4)
    passenger_value_payload1 = extract_value(payload1, byte_position=0, bit_position=7, size=3)
    time_format_value_payload1 = extract_value(payload1, byte_position=5, bit_position=3, size=1)

    print("Payload 1:")
    print("ClimFPrightBlowingRequest:", clim_value_payload1)
    print("PassengerSeatMemoRequest:", passenger_value_payload1)
    print("TimeFormatDisplay:", time_format_value_payload1)

    payload2 = bytearray.fromhex("40 12 6C AF 05 78 4A 04")

    clim_value_payload2 = extract_value(payload2, byte_position=5, bit_position=7, size=4)
    passenger_value_payload2 = extract_value(payload2, byte_position=0, bit_position=7, size=3)
    time_format_value_payload2 = extract_value(payload2, byte_position=5, bit_position=3, size=1)


    print("\nPayload 2:")
    print("ClimFPrightBlowingRequest:", clim_value_payload2)
    print("PassengerSeatMemoRequest:", passenger_value_payload2)
    print("TimeFormatDisplay:", time_format_value_payload2)