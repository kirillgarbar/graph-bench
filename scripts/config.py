import pathlib
import platform

__all__ = [
    "ROOT",
    "DATASET",
    "DEPS",
    "SYSTEM",
    "EXECUTABLE_EXT",
    "LIBRARY_EXT",
    "DEFAULT_SOURCE_VERTEX",
    "DEFAULT_NUM_ITERATIONS",
    "GRAPHS_NAMES",
    "GRAPHS_DATA",
    "Graph"
]

from dataclasses import dataclass

ROOT = pathlib.Path(__file__).parent.parent
DATASET = ROOT / "dataset"
DEPS = ROOT / "deps"

SYSTEM = {'Darwin': 'macos', 'Linux': 'linux', 'Windows': 'windows'}[platform.system()]
EXECUTABLE_EXT = {'macos': '', 'windows': '.exe', 'linux': ''}[SYSTEM]
LIBRARY_EXT = {'macos': '.dylib', 'linux': '.so', 'windows': '.dll'}[SYSTEM]

DEFAULT_NUM_ITERATIONS = 10
DEFAULT_SOURCE_VERTEX = 0

GRAPHS_NAMES = [
    'coAuthorsCiteseer',
    'coPapersDBLP',
    'hollywood-2009',
    'roadNet-CA',
    'cit-Patents'
    'soc-LiveJournal',
    'indochina-2004'
]


@dataclass
class Graph:
    file: str

    def path(self):
        return DATASET / self.file


GRAPHS_DATA = {name: Graph(f"{name}.mtx") for name in GRAPHS_NAMES}
