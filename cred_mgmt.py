import keyring
from getpass import getpass


def add_credentials():
    """
    Prompts the user for their Alpaca API key and secret, and stores them in the system's keyring.
    """
    api_key = getpass("Enter your Alpaca API key: ")
    api_secret = getpass("Enter your Alpaca API secret: ")
    keyring.set_password("python-alpaca", "api_key", api_key)
    keyring.set_password("python-alpaca", "api_secret", api_secret)


def get_credentials(cred_name: str):
    """
    Retrieves the stored Alpaca API key or secret from the system's keyring.

    Args:
        cred_name (str): The name of the credential to retrieve
    
    Returns:

    """
    try:
        cred = keyring.get_password("python-alpaca", cred_name)
        return cred
    except keyring.errors.KeyringError:
        print(f"Error: Unable to retrieve {cred_name} from keyring. Please add credentials first.")
        return None


def main():
    add_credentials()
    get_credentials("api_key")
    get_credentials("api_secret")


if __name__ == "__main__":
    main()
