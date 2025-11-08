import argparse
import sys
import os

def parse_arguments():
    parser = argparse.ArgumentParser(
    )

    parser.add_argument(
        "--package-name",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--repo-url",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--test-mode",
        type=str,
        choices=["local", "remote"],
        default="local",
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default="dependency_graph.png",
    )
    parser.add_argument(
        "--filter-substring",
        type=str,
        default="",
    )

    return parser.parse_args()


def validate_arguments(args):
    # Проверка, что package-name не пустой (и не состоит только из пробелов)
    if not args.package_name or not args.package_name.strip():
        print("Ошибка: --package-name не может быть пустым.", file=sys.stderr)
        sys.exit(1)  # Завершаем программу с кодом ошибки

    # Проверка, что repo-url не пустой
    if not args.repo_url or not args.repo_url.strip():
        print("Ошибка: --repo-url не может быть пустым.", file=sys.stderr)
        sys.exit(1)

    # Если выбран локальный режим, проверяем, существует ли указанный путь в файловой системе
    if args.test_mode == "local" and not os.path.exists(args.repo_url):
        print(f"Ошибка: путь '{args.repo_url}' не существует (режим local).", file=sys.stderr)
        sys.exit(1)


def print_configuration(args):
    print("Конфигурация приложения")
    print(f"package-name: {args.package_name}")
    print(f"repo-url: {args.repo_url}")
    print(f"test-mode: {args.test_mode}")
    print(f"output-file: {args.output_file}")
    print(f"filter-substring: '{args.filter_substring}'")


def main():
    args = parse_arguments()
    validate_arguments(args)
    print_configuration(args)
    print("\nЭтап 1 успешно завершён.")


if __name__ == "__main__":
    main()

# python main.py --package-name NuGetGallery --repo-url https://github.com/NuGet/NuGetGallery --test-mode local --output-file my_graph.png --filter-substring Json