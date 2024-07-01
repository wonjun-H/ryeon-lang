
import sys

from lang.Ryeon import Ryeon

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            data = file.read()
            bf = Ryeon()
            bf.load(data)
            bf.run()
            sys.stdout.write("\n")
    except Exception as e:
        print(f"Error: {e}")
