"""Script for printing hello world."""


def hello_world(name: str = "Player") -> None:
    """Print a personalized 'Hello World!' message to the console.

    Args:
        name (str): The name of the person to greet. Defaults to "Player".

    This function demonstrates a basic personalized greeting using a formatted string.
    """
    print(f"Hello World, {name}!")  # Output a personalized greeting message


if __name__ == "__main__":
    # Execute the hello_world function with the default name when run as a script
    hello_world()
