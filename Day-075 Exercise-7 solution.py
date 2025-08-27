import os

files = os.listdir("clutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        # print(file)
        os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
        print(file)
        i = i + 1

# os.rename(f"clutteredFolder/file.txt", "clutteredFolder/6.txt")