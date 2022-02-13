import abc
import statistics
import config
from dataclasses import dataclass
from typing import List


@dataclass
class ExecutionResult:
    """
    Result of the execution of the single algorithm benchmark run
    """
    warm_up: float
    times: List[float]

    def avg(self):
        return statistics.mean(self.times)

    def median(self):
        return statistics.median(self.times)

    def sd(self):
        return statistics.stdev(self.times)

    def brief_str(self) -> str:
        return f'warm_up={self.warm_up:.2f}ms, avg={self.avg():.2f}ms, ' \
               f'median={self.median():.2f}ms, sd={self.sd():.2f}'

    def __str__(self) -> str:
        return self.brief_str()

    def __repr__(self) -> str:
        return self.brief_str()


class Driver:
    """
    Base class for any driver, which is responsible for running
    algorithm benchmarks for third-party tools from stand-alone
    executable files.

    Algorithms:
        * bfs
        * sssp
        * tc
        * [future] cc
        * [future] page rank
    """

    @abc.abstractmethod
    def name(self) -> str:
        """
        Retrieve driver name
        :return: Driver name
        """
        pass

    @abc.abstractmethod
    def run_bfs(self, graph: config.Graph, source_vertex: int, num_iterations: int) -> ExecutionResult:
        """
        Run bfs algorithm benchmark.
        :param graph: Graph with its properties to run on
        :param source_vertex: Source vertex to start algorithm
        :param num_iterations: Number of iteration to run
        :return: execution results
        """
        pass

    @abc.abstractmethod
    def run_sssp(self, graph: config.Graph, source_vertex: int, num_iterations: int) -> ExecutionResult:
        """
        Run sssp algorithm benchmark.
        :param graph: Graph with its properties to run on
        :param source_vertex: Source vertex to start algorithm
        :param num_iterations: Number of iteration to run
        :return: execution results
        """
        pass

    @abc.abstractmethod
    def run_tc(self, graph: config.Graph, num_iterations: int) -> ExecutionResult:
        """
        Run tc algorithm benchmark.
        :param graph: Graph with its properties to run on
        :param num_iterations: Number of iteration to run
        :return: execution results
        """
        pass

    def run(self, graph: config.Graph, algo: str, params: dict) -> ExecutionResult:
        """
        Execute driver benchmark with specified params
        :param graph: Graph to analyse
        :param algo: Algorithm name to run
        :param params: Additional params
        :return: execution result
        """
        if algo == 'bfs':
            result = self.run_bfs(graph, int(params['source']), int(params['num_iterations']))
        elif algo == 'sssp':
            result = self.run_sssp(graph, int(params['source']), int(params['num_iterations']))
        elif algo == 'tc':
            result = self.run_tc(graph, int(params['num_iterations']))
        else:
            raise Exception(f"Unknown algorithm {algo}")

        print(f"Run {self.name()} result: {result}")
        return result
