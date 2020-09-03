import inspect
import sys


def generate(name):
    try:
        mod = __import__(name)
        members = inspect.getmembers(mod)
        for _name, member in members:
            if getattr(member, "NAME", None) == name:
                print(f"Invoking {name} with module {member}")
                member().generate()
                break
        else:
            print(f"Cannot find generator named class in module {name}")
    except ModuleNotFoundError:
        print(f"Cannot find generator module {name}")



if __name__ == "__main__":
    generate(sys.argv[1])
