# dependency:
# uv pip install pycryptodome
from aes_cbc_with_iv import decrypt

key = "8056483646328763"
iv = "6852612370185273".encode("utf-8")
input_path = "/home/egrove/Downloads/drama/Hidden Love/Hidden-Love.Ep3.srt.txt"
output_path = "/home/egrove/Downloads/drama/Hidden Love/Hidden-Love.Ep3.srt"
output = ""

with open(input_path, "r") as f:
    while line := f.readline():
        # print(line)
        try:
            if (
                line == "\n"
                or line.strip().isdigit()
                or (
                    len(line) > 2
                    and line[0].isdigit()
                    and line[1].isdigit()
                    and line[2] == ":"
                )
            ):
                output += str(line)
                continue
            output += decrypt(str(line), key, iv).decode("utf-8") + "\n"
        except Exception as e:
            print(f"Error processing line: {line}")
            print(e)
            # raise

with open(output_path, "w+") as f:
    f.write(output)

# print(f"lines: {lines}")
