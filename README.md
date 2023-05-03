# Auto-ChatGPT

This Python project leverages Selenium to automate interactions with the browser-based ChatGPT. As a result, it enables efficient communication with the browser version of ChatGPT without using an API.

(Suggestions for a better project and package name are welcome, as the current ones do not seem quite appropriate.)

## Table of Contents

- [Auto-ChatGPT](#auto-chatgpt)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Environment Setup](#environment-setup)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contributing](#contributing-1)
  - [License](#license-1)

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

## Environment Setup

To securely store your email address and password, create a `.env` file in the project's root directory by copying the `.env.example` file:

```
cp .env.example .env
```

Edit the `.env` file and replace `YOUR_EMAIL_ADDRESS` and `YOUR_PASSWORD` with your actual email address and password.

## Usage

Set up a jupyter server or use vscode to run **autochat.ipynb**.

The email address and password are loaded from the `.env` file. This will open a Chrome window and navigate to the ChatGPT website. Follow the prompts in the terminal to start the conversation with ChatGPT.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue to discuss any potential improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue to discuss any potential improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
