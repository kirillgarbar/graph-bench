import pathlib
import platform

from dataclasses import dataclass

ROOT = pathlib.Path(__file__).parent.parent
DATASET = ROOT / "dataset"
DEPS = ROOT / "deps"
MATRICES = ROOT / "scripts" / "matrices.txt"

SYSTEM = {'Darwin': 'macos', 'Linux': 'linux', 'Windows': 'windows'}[platform.system()]
EXECUTABLE_EXT = {'macos': '', 'windows': '.exe', 'linux': ''}[SYSTEM]
LIBRARY_EXT = {'macos': '.dylib', 'linux': '.so', 'windows': '.dll'}[SYSTEM]
DATASET_SUFFIX = ""

DEFAULT_NUM_ITERATIONS = 10
DEFAULT_SOURCE_VERTEX = 0

GRAPHS_NAMES = open(MATRICES, 'r').readlines()


@dataclass
class Graph:
    id: str

    def path_original(self):
        return DATASET / f"{self.id}.mtx"

    def path(self):
        return DATASET / f"{self.id}.mtx{DATASET_SUFFIX}"

    def about(self):
        return self.id

    def __str__(self):
        return self.about()

    def __repr__(self):
        return self.about()


GRAPHS_DATA = {name: Graph(name) for name in GRAPHS_NAMES}

GRAPHS_BFS = [ GRAPHS_DATA[name] for name in GRAPHS_DATA ]

GRAPHS_SSSP = [ GRAPHS_DATA[name] for name in GRAPHS_DATA ]

GRAPHS_TC = [ GRAPHS_DATA[name] for name in GRAPHS_DATA ]

ALGORITHMS = ["bfs", "sssp", "tc"]
GRAPHS = {"bfs": GRAPHS_BFS, "sssp": GRAPHS_SSSP, "tc": GRAPHS_TC}
