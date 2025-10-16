#!/usr/bin/env python3
import sys
# XX XX XX XX 74 ?? > XX XX XX XX EB ?? # JE short jump
# XX XX XX XX 75 ?? > XX XX XX XX 90 90 # JNE short jump
# XX XX XX XX 0F 84 ?? ?? ?? ?? > XX XX XX XX 90 E9 ?? ?? ?? ?? # JE near jump
# XX XX XX XX 0F 85 ?? ?? ?? ?? > XX XX XX XX 90 90 90 90 90 90 # JNE near jump
# 81 F3 XX XX XX XX > 31 DB 90 90 90 90 # XOR EBX
# 81 F1 XX XX XX XX > 31 C9 90 90 90 90 # XOR ECX
# 81 F2 XX XX XX XX > 31 D2 90 90 90 90 # XOR EDX

def main():
    path = sys.argv[1]

    with open(path, "rb") as f:
        data = bytearray(f.read())

    for pattern in [b"Genu", b"ineI", b"ntel"]:
        i = 0
        plen = len(pattern)
        while True:
            idx = data.find(pattern, i)
            if idx == -1:
                break
            after = idx + plen
            # This will break Clang's architecture detection functionality.
            # You may uncomment these codes if you do not intend to apply it to the Intel toolchain.
            # if data[after] == 0x74:
            #     data[after] = 0xEB
            # elif data[after] == 0x75:
            #     data[after:after+2] = b"\x90" * 2
            if data[after] == 0x0F:
                if data[after+1] == 0x84:
                    data[after:after+2] = b"\x90\xE9"
                elif data[after+1] == 0x85:
                    data[after:after+6] = b"\x90" * 6
            elif data[idx-2] == 0x81:
                if data[idx-1] == 0xF3:
                    data[idx-2:after] = b"\x31\xDB" + b"\x90" * plen
                elif data[idx-1] == 0xF1:
                    data[idx-2:after] = b"\x31\xC9" + b"\x90" * plen
                elif data[idx-1] == 0xF2:
                    data[idx-2:after] = b"\x31\xD2" + b"\x90" * plen
            i = idx + 1

    with open(path, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    main()
