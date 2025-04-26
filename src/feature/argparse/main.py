import argparse


def main(args: argparse.Namespace) -> None:
    print(args)  # noqa: T201


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
    )

    # 位置引数. addする順番で位置が決まる
    parser.add_argument("input_filename")
    parser.add_argument("output_filename")

    # flag
    # 渡されればTrue, そうでなければFalse
    parser.add_argument("-v", "--verbose", action="store_true")
    # 渡されればFalse, そうでなければTrue
    parser.add_argument("-f", "--false", action="store_false")

    args = parser.parse_args()

    main(args)
