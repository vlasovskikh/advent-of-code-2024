import collections
import heapq
import typing

from aoc24 import utils


MAX_BLOCKS = 9

DenseDisk = typing.NewType("DenseDisk", list[int])
Disk = typing.NewType("Disk", list[int])


def free_up_space(disk: DenseDisk) -> Disk:
    new: Disk = Disk([])
    spaces = collections.deque(disk[1::2])
    files = collections.deque(enumerate(disk[::2]))
    while files and spaces:
        fid, blocks = files.popleft()
        new.extend([fid] * blocks)
        space = spaces.popleft()
        while files and space > 0:
            fid, blocks = files.pop()
            if blocks <= space:
                new.extend([fid] * blocks)
            else:
                new.extend([fid] * space)
                files.append((fid, blocks - space))
            space -= blocks
    return new


def defragment(disk: DenseDisk) -> Disk:
    result: dict[int, list[int]] = collections.defaultdict(list)
    spaces = {i: space for i, space in enumerate(disk) if i % 2 == 1}
    files = [(i, blocks) for i, blocks in enumerate(disk) if i % 2 == 0]
    free: dict[int, list[int]] = collections.defaultdict(list)
    for i, space in spaces.items():
        heapq.heappush(free[space], i)
    while files:
        i, blocks = files.pop()
        sorted_free = sorted(
            (free[j][0], free[j])
            for j in range(blocks, MAX_BLOCKS + 1)
            if free[j] and free[j][0] < i
        )
        if sorted_free:
            _, heap = sorted_free[0]
            index = heapq.heappop(heap)
            space = spaces[index]
            left = space - blocks
            spaces[index] = left
            heapq.heappush(free[left], index)
        else:
            index = i
        fid = i // 2
        result[index].extend([fid] * blocks)
    for i, space in spaces.items():
        result[i].extend([0] * space)
    for i, x in enumerate(disk):
        if i not in result:
            result[i].extend([0] * x)
    new = Disk([])
    for _, xs in sorted(result.items()):
        new.extend(xs)
    return new


def checksum(disk: Disk) -> int:
    return sum(i * x for i, x in enumerate(disk))


def parse_input(lines: list[str]) -> DenseDisk:
    assert len(lines) == 1
    return DenseDisk([int(c) for c in lines[0]])


def main() -> None:
    disk = parse_input(utils.read_input_lines(__file__))
    print(checksum(free_up_space(disk)))
    print(checksum(defragment(disk)))


if __name__ == "__main__":
    main()
