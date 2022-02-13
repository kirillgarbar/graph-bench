import subprocess

import config

SPLA = config.DEPS / "spla"
SPLA_BUILD = SPLA / "build"
SPLA_DATA_TOOL = SPLA_BUILD / "spla_data"


def main():
    print("Convert graphs:")
    for graph in config.GRAPHS_DATA.values():
        subprocess.call([str(SPLA_DATA_TOOL), f"--mtxpath={graph.path_original()}"])
        print(f" Output graph to {graph.path()}")


if __name__ == '__main__':
    main()
