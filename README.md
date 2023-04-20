# Auto-ChatGPT

This is a Python project to automate the exchange of ChatGPT for the browser version using Selenium. This will allow efficient communication with the browser version of ChatGPT.

## Table of Contents

- [Auto-ChatGPT](#auto-chatgpt)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

To use this project, you need to install the dependencies by following these steps:

1. Make sure you have Python 3.10+ installed on your system. If not, download it from [here](https://www.python.org/downloads/).

2. Clone this repository:

   ```
   git clone https://github.com/ryuseisan/auto-chatgpt.git
   ```

   ```
   cd auto-chatgpt
   ```

3. Install the required dependencies using either Poetry or Pip:

- With Pip:

  ```
  pip install .
  ```

- With Poetry:

  ```
  poetry install
  ```

## Usage

Set up a jupyter server or use vscode to run **autochat.ipynb**.

Enter the appropriate email address and password in `login_openai()` or `login_google_account()` in your notebook.

This will open a Chrome window and navigate to the ChatGPT website. Follow the prompts in the terminal to start the conversation with ChatGPT.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue to discuss any potential improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
