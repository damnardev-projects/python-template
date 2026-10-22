def main(name: str) -> str:

    if name is None:
        raise ValueError("Name cannot be None")

    return f"Hello, {name}!"

def poetry() -> None:
    print(main("World"))

if __name__ == "__main__":
    poetry()
