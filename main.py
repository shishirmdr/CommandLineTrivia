import argparse
from trivia import Trivia


def main():
    parser = argparse.ArgumentParser('Just a simple command line trivia')

    parser.add_argument("-a", "--amount", type=int, default=5,
                        help="amount of questions to fetch (default 5, max 10)")
    parser.add_argument("-l", "--level", type=int, default=1,
                        help="set difficulty level (default 1, max 3)")

    args = parser.parse_args()

    if args.amount is not None:
        if args.amount == 0 or args.amount > 10:
            parser.error("Amount should be between 1 and 10 (inclusive)")

    if args.level is not None:
        if args.level == 0 or args.level > 3:
            parser.error('Level should be between 1 and 3 (inclusive)')

    difficulty = ["easy", "medium", "hard"]
    level = difficulty[args.level - 1]
    print(f"Difficulty level: {level}")

    trivia = Trivia(args.amount, level)
    trivia.begin()


if __name__ == '__main__':
    main()
