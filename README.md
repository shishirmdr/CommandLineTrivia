# CommandLineTrivia
Uses [Opentdb](https://opentdb.com/api_config.php)'s api to fetch questions.

## Requirements
Make sure you have python3 installed in your machine.
* [requests](https://pypi.org/project/requests/)
* [colorama](https://pypi.org/project/colorama/)

## Usage
    python main.py 
***Default**: 5 questions and easy difficulty*
 
## Config
Supply the following arguments to change the amount of questions to fetch and increase difficulty.

    -a, --amount    default: 5, max: 10

    -l, --level     default: 1, max: 3 (easy: 1, medium: 2, hard: 3)
