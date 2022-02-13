import subprocess
import config
import argparse

GRAPHBLAST_PATH = config.DEPS / "graphblast"


def build(args):
    try:
        print(f"Build graphblast inside {GRAPHBLAST_PATH} directory")
        subprocess.check_call(["make", "-B", f"--directory={GRAPHBLAST_PATH}", f"-j{args.j}"])
    except subprocess.CalledProcessError as error:
        print("Failed to build graphblast. Error:", error)
        return 1

    print("Done!")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--j", default=4, help="Number of threads used to build")
    args = parser.parse_args()
    return build(args)


if __name__ == '__main__':
    exit(main())
