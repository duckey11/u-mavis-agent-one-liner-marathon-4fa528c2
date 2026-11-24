import os

JOKE = "My mechanic Sam charged me $600 for new brakes, then I opened my trunk and found my old brake pads in a sealed bag stamped 80% life left."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
