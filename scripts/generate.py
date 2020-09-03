import sys

from somafm import GenerateSomaFM


def generate(name):
    if name == "somafm":
        GenerateSomaFM().generate()
    else:
        print(f"Unknown script {name}")


if __name__ == "__main__":
    generate(sys.argv[1])
