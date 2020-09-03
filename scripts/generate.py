import sys

from somafm import GenerateSomaFM
from liveatc import GenerateLiveATC

def generate(name):
    if name == "somafm":
        GenerateSomaFM().generate()
    elif name == "liveatc":
        GenerateLiveATC().generate()
    else:
        print(f"Unknown script {name}")


if __name__ == "__main__":
    generate(sys.argv[1])
