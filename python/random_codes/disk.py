from os import statvfs as stat
from re import compile, search
from bisect import bisect
from pathlib import Path

class diskUsage:
    def __init__(self, file):
        self.IO_Block = stat(file).f_bsize
        self.f_blocks = stat(file).f_blocks
        self.f_bfree = stat(file).f_bfree

    def convert(self, bytes):
        size = [1, 2**10, 2**20, 2**30, 2**40]
        unit = ['B', 'K', 'M', 'G', 'T']
        index = bisect(size, bytes) - 1
        return f"{bytes/size[index]:.0f}{unit[index]}"

    def size(self):
        return self.convert(self.f_blocks*self.IO_Block)

    def free(self):
        return self.convert(self.f_bfree*self.IO_Block)

    def used(self):
        used = self.f_blocks - self.f_bfree
        return self.convert(used*self.IO_Block)

    def user(self):
        return f"{(self.f_blocks - self.f_bfree) / self.f_blocks:.0%}"

comp = compile(r'^/dev(?!.*snap)')
mline = Path('/proc/mounts').read_text().splitlines()
fs = [i.split()[:2] for i in mline if comp.search(i)]

print(f'{"File system":>} \t{"Size":>} {"Used":>}', end = ' ')
print(f'{"Avail":>} {"Use%":>} {"Mounted on":>}')
print('='*47)

for x in fs:
    disk = diskUsage(x[1])
    print(f'{x[0]} \t{disk.size():4} {disk.used():4}', end = ' ')
    print(f'{disk.free():5} {disk.user():4} {x[1]}')
