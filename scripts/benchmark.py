import config
import driver_graphblast
import driver_gunrock
import driver_lagraph
import driver_spla
import argparse
import csv
from datetime import datetime
import re

LaGRAPH_PATH = config.DEPS / "lagraph" / "build_git"
OUTPUT_PATH = config.ROOT / "docs"

DRIVERS = {
    "graphblast": driver_graphblast.DriverGraphBLAST(),
    "gunrock": driver_gunrock.DriverGunrock(),
    "lagraph": driver_lagraph.DriverLaGraph(LaGRAPH_PATH),
    "spla": driver_spla.DriverSpla()
}


def print_table(table):
    for row in table:
        print(", ".join([str(v) for v in row]))


def build_table(cols: dict, prop):
    header = ["graph"]
    rows = dict()

    for col in cols.values():
        for row_name in col.keys():
            if row_name not in rows:
                rows[row_name] = []

    for name, col in cols.items():
        header.append(name)
        for row_name in rows:
            if row_name in col:
                rows[row_name].append(prop(col[row_name]))
            else:
                rows[row_name].append("none")

    return [header] + [[row_name] + row_data for row_name, row_data in rows.items()]


def output_stats(run_stats: dict):
    for algo, stats in run_stats.items():
        print("-" * 40 + f" {algo} " + "-" * 40)
        print_table(build_table(stats, lambda x: x.avg()))


def get_time_stamp():
    current_time = datetime.now()
    time_stamp = current_time.timestamp()
    date_time = datetime.fromtimestamp(time_stamp)
    return date_time.strftime("%d-%m-%Y-%H:%M:%S")


def store_stats(run_stats: dict):
    header = ["MATRIX", "MEAN", "SD", "MIN", "MAX"]
    output_file = open(OUTPUT_PATH / (get_time_stamp() + ".csv"), "w")
    writer = csv.writer(output_file)

    for algo in run_stats:
        writer.writerow([f"{algo}"])

        for tool in run_stats[algo]:
            writer.writerow([f"{tool}"])
            writer.writerow(header)

            for graph in run_stats[algo][tool]:
                stats = f"{run_stats[algo][tool][graph]}"
                stat_list = [graph] + [re.sub("[^\d\.]", "", stat) for stat in stats.split(',')[1:]]
                del stat_list[3]
                writer.writerow(stat_list)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", default="all", help="Algorithm to test [all, bfs, sssp, tc]")
    parser.add_argument("--tool", default="all", help="Tool to test [all, graphblast, gunrock, lagraph, spla]")
    parser.add_argument("--num-iterations", default=10, help="Number of iteration to run each test")
    parser.add_argument("--source", default=config.DEFAULT_SOURCE_VERTEX, help="Source vertex for bfs, sssp, etc.")
    parser.add_argument("--graph", help="Graph to run algorithms")
    parser.add_argument("--platform", default="", help="OpenCL platform to run (for OpenCL-based tools)")
    args = parser.parse_args()

    if args.algo == 'all':
        algos = config.ALGORITHMS
    else:
        algos = [args.algo]

    if args.tool == 'all':
        tools = list(DRIVERS.values())
    else:
        tools = [DRIVERS[tool.strip()] for tool in args.tool.strip("[]").split(",")]

    if args.graph is None:
        graphs = config.GRAPHS
    else:
        graphs = {algo: [config.GRAPHS_DATA[args.graph]] for algo in algos}

    params = {
        "num_iterations": int(args.num_iterations),
        "source": int(args.source),
        "platform": str(args.platform)
    }

    print("Run benchmarks:")
    print(f" algos: {repr(algos)}")
    print(f" tools: {repr(tools)}")
    print(f" graphs: {repr(graphs)}")
    print(f" params: {repr(params)}")

    run_stats = dict()

    for algorithm in algos:
        print(f"Execute: {algorithm}")
        algo_stats = run_stats[algorithm] = dict()
        for tool in tools:
            print(f" Tool: {tool}")
            tool_stats = algo_stats[tool.name()] = dict()
            for graph in graphs[algorithm]:
                print(f"  Graph: {graph}")
                try:
                    res = tool_stats[graph.id] = tool.run(graph, algorithm, params)
                    print(f"  Result: {res}")
                except Exception as e:
                    print(f"  Failed due {e}")

    output_stats(run_stats)
    store_stats(run_stats)


if __name__ == '__main__':
    main()
