import argparse


def run_app(debug=False):
    from nevua.app import main

    main(debug)


def cache_data(hp=None):
    from nevua.app import process_data

    if hp:
        print(f"Hyperparameters: {hp}")
    process_data(hp=hp)


def main():
    parser = argparse.ArgumentParser(
        description="Control the web application and data processing."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    up_parser = subparsers.add_parser("up", help="Run the web application")
    up_parser.add_argument("--debug", action="store_true", help="Enable debug mode")

    cache_parser = subparsers.add_parser(
        "cache", help="Cache the data without running the web app"
    )
    cache_parser.add_argument(
        "--hp", type=str, help="Hyperparameters for processing data"
    )

    args = parser.parse_args()

    if args.command == "up":
        run_app(debug=args.debug)
    elif args.command == "cache":
        cache_data(hp=args.hp)


if __name__ == "__main__":
    main()
