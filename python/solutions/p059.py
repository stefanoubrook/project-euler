def load_encrypted_ints(path: str) -> list[int]:
    with open(path, "r") as f:
        return [int(x) for x in f.read().split(",")]


def unencrypt(list: list[int]) -> tuple[str, bool]:
    encrypted_bytes = bytes(list)
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                unencrypted_chars = []
                key = bytes((i, j, k))
                print(key)
                for n, bit in enumerate(encrypted_bytes):
                    unencrypted_byte = bit ^ (key[n % 3])
                    unencrypted_chars.append(chr(unencrypted_byte))

                text = "".join(unencrypted_chars)

                if " the " in text:
                    return (text, True)
    return ("", False)


def solve(text: tuple[str, bool]) -> int:
    if text[1]:
        return sum([ord(x) for x in text[0]])
    else:
        return -1


if __name__ == "__main__":
    print(solve(unencrypt(load_encrypted_ints("inputs/059_cipher.txt"))))
