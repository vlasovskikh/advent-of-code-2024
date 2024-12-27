import itertools

from aoc24 import utils


type Graph = dict[str, set[str]]


def count_triples_starting_with_t(graph: Graph) -> int:
    filtered = [
        nodes
        for nodes in find_fully_connected(graph)
        if any(n.startswith("t") for n in nodes)
    ]
    return len(filtered)


def find_largeset_fully_connected(graph: Graph) -> str:
    maximum = max(len(v) + 1 for v in graph.values())
    size = maximum
    while size:
        subgraphs = find_fully_connected(graph, size)
        if len(subgraphs) == 1:
            subgraph = list(subgraphs)[0]
            return ",".join([n for n in sorted(subgraph)])
        elif len(subgraphs) > 1:
            raise ValueError(f"Found multiple largest: {subgraphs!r}")
        else:
            size -= 1
    raise ValueError("Not found any fully connected subgraphs")


def find_fully_connected(graph: Graph, size: int = 2) -> set[frozenset[str]]:
    result: set[frozenset[str]] = set()
    for node, neighbors in graph.items():
        for combs in itertools.combinations(neighbors, size):
            found = True
            for n in combs:
                nn = graph[n] | {n}
                if not nn.issuperset(combs):
                    found = False
                    break
            if found:
                result.add(frozenset(set(combs) | {node}))
    return result


def parse_input(lines: list[str]) -> Graph:
    result: Graph = {}
    for line in lines:
        n1, n2 = line.split("-")
        if n1 in result:
            result[n1].add(n2)
        else:
            result[n1] = {n2}
        if n2 in result:
            result[n2].add(n1)
        else:
            result[n2] = {n1}
    return result


def main() -> None:
    graph = parse_input(utils.read_input_lines(__file__))
    print(count_triples_starting_with_t(graph))
    print(find_largeset_fully_connected(graph))


if __name__ == "__main__":
    main()
