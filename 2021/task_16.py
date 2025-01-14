import aoc
from functools import reduce
import operator

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 31, 54

# Common
input_bin_str = bin(int(lines[0], 16))[2:].zfill(len(lines[0]) * 4)
ops = {
    0: lambda x: sum(x),
    1: lambda x: reduce(operator.mul, x),
    2: lambda x: min(x),
    3: lambda x: max(x),
    4: None,
    5: lambda x: 1 if x[0] >  x[1] else 0, 
    6: lambda x: 1 if x[0] <  x[1] else 0, 
    7: lambda x: 1 if x[0] == x[1] else 0, 
}
VER_SIZE, TYPE_SIZE = 3, 3
BITLEN_SIZE, NUMPKT_SIZE = 15, 11
OPHDR_SIZE = VER_SIZE + TYPE_SIZE + 1

def process_literal_packet(bin_str):
    start_size = len(bin_str)
    num_bin = 0
    while True:
        info_bit, bin_str = popleft_n_bits(bin_str, 1)
        num_bits, bin_str = popleft_n_bits(bin_str, 4)
        num_bin = (num_bin << 4) + num_bits
        if info_bit == 0:
            return num_bin, start_size - len(bin_str), bin_str

def popleft_n_bits(bin_str, n):
    return int(bin_str[:n], base=2), bin_str[n:]

def process_packet(bin_str):
    pkt_ver, bin_str = popleft_n_bits(bin_str, VER_SIZE)
    pkt_type, bin_str = popleft_n_bits(bin_str, TYPE_SIZE)
    
    if pkt_type == 4:
        num, consumed, bin_str = process_literal_packet(bin_str)
        return pkt_ver, num, VER_SIZE + TYPE_SIZE + consumed, bin_str

    size_bit, bin_str = popleft_n_bits(bin_str, 1)
    nums = []
    cur_len = 0
    if size_bit == 0:
        len_subpackets, bin_str = popleft_n_bits(bin_str, BITLEN_SIZE)
        while cur_len != len_subpackets:
            ver, num, pkt_len, bin_str = process_packet(bin_str)
            pkt_ver += ver
            nums.append(num)
            cur_len += pkt_len
    elif size_bit == 1:
        num_subpackets, bin_str = popleft_n_bits(bin_str, NUMPKT_SIZE)
        for _ in range(num_subpackets):
            ver, num, pkt_len, bin_str = process_packet(bin_str)
            pkt_ver += ver
            nums.append(num)
            cur_len += pkt_len

    number = ops[pkt_type](nums)
    consumed = OPHDR_SIZE + (BITLEN_SIZE if size_bit == 0 else NUMPKT_SIZE)
    return pkt_ver, number, consumed + cur_len, bin_str

# Part 1
aoc.mark_task_start()
ver, num, *_ = process_packet(input_bin_str)
result1 = ver
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
result2 = num
aoc.print_result(2, result2, exp2)
