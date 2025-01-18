# PathBreaker

**PathBreaker** is a penetration testing tool that generates payloads to test for **path normalization vulnerabilities** in web applications. Path normalization vulnerabilities occur when web applications fail to sanitize user input in file paths properly.


## Features

- **Basic Path Traversal**: Generates payloads that attempt basic directory traversal attacks.
- **Encoded Variants**: Tests URL encoding techniques to bypass path restrictions, such as encoding `/` as `%2f`.
- **Double Encoding**: Attempts double URL encoding (e.g., `%252f` for `/`) to test for misconfigurations in path normalization.
- **Unicode Encodings**: Tests for Unicode path encodings (e.g., `%c0%af`) that may bypass filters.
- **Mixed Encoding**: Combines multiple encoding methods (e.g., `%2e%2e/%2e%2e/`) to test path normalization flaws.
- **Semicolon and Path Tricks**: Includes payloads with semicolons and other unconventional path separators to test for weak path handling.


## Usage
1-Provide the Input: The script will prompt you to enter two paths:

**Accessible Path**: The path that you can normally access (e.g., /api/user).

**Restricted Path**: The path that you want to test for unauthorized access (e.g., /admin/users, /internal-api).

2-Payload Generation: The tool will output a list of payloads that you can use to test for path normalization vulnerabilities. These payloads help you determine if the web application fails to properly handle path traversal.

## Acknowledgment
This tool was designed based on the research by Orange Tsai, who presented groundbreaking work on path normalization vulnerabilities. The research highlights how improperly handled path parsers can lead to vulnerabilities that allow attackers to break out of intended directories. You can read more about it in the research paper:
[Breaking Parser Logic: Take Your Path Normalization Off And Pop 0days Out - Black Hat 2018.](https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf)

## Contributing
If you'd like to contribute to the project, feel free to fork the repository, submit issues, or create pull requests. Please follow the usual GitHub contribution guidelines.
