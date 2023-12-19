import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 1, 1

# Common
workflows = {}
for line in lines:
    if line == '':
        break
    w_name, rules = line[:-1].split('{')
    rules = rules.split(',')
    w = []
    for r in rules:
        if ':' in r:
            cond, target = r.split(':')
            w.append((cond[0], cond[1], int(cond[2:]), target))
        else:
            w.append((None, None, None, r))
    workflows[w_name] = w
    # print(workflows[w_name])

ratings = []
for line in lines[len(workflows)+1:]:
    ratings_in_line = line[1:-1].split(',')
    r = {}
    for rat in ratings_in_line:
        name, number = rat.split('=')
        r[name] = int(number)
    ratings.append(r)
    # print(r)

# Part 1
aoc.mark_task_start()
accepted = 0
count = 0
print()
for rat in ratings:
    done = False
    cur_workf = 'in'
    # print(f'Rating: {rat}')
    while not done:
        # print(f'  cur_workf: {cur_workf}')
        if cur_workf == 'A':
            accepted += 1
            # print(f'Accepted: ', rat)
            count += sum(rat.values())
            break
        elif cur_workf == 'R':
            break
        conditions = workflows[cur_workf]
        for x, cond, num, next in conditions:
            # print(f'    ', x, cond, num, next)
            if x == None:
                if next in ['A', 'R']:
                    if next == 'A':
                        # print(f'Accepted: ', rat)
                        accepted += 1
                        count += sum(rat.values())
                    done = True
                    break
                else:
                    cur_workf = next
                    break
            else:
                cond_true = False
                if cond == '<':
                    if rat[x] < num:
                        cond_true = True
                if cond == '>':
                    if rat[x] > num:
                        cond_true = True
                if cond_true:
                    cur_workf = next
                    break

print(accepted)
print(count)

result1 = count
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
# accepted = 0
# count = 0
MAX_NUM = 4000
# for rat in ratings:
#     done = False
#     cur_workf = 'in'
#     # print(f'Rating: {rat}')
#     while not done:


all_ranges = []
grand_total = 0
def do_stuff(workf_list=None, next_line_workf=None, ranges=None):
    # print(f'  cur_workf: {cur_workf}')
    global all_ranges
    global grand_total
    if ranges is None:
        ranges = []
    rrr = 0
    next_line = None
    if next_line_workf:
        if next_line_workf == 'A':
            print(f'   >>> R is {ranges}')
            total = 1
            for ch in 'asxm':
                ss = [set(x) for c, x in ranges if c == ch]
                if ss:
                    s = set.intersection(*ss)
                    total *= len(s)
                    print(f'     len is {len(s)}')
                else:
                    total *= MAX_NUM
            print(f'        Total: {total}\n')
            grand_total += total

            all_ranges += ranges[:]
            return rrr
        elif next_line_workf == 'R':
            return 0
        next_line = workflows[next_line_workf]
    else:
        next_line = workf_list
    
    # print(f'Next line: {next_line}')
    x, cond, num, cur_workf = next_line[0]

    if x == None:
        if cur_workf == 'A':
            print(f'   >>> R is {ranges}')
            total = 1
            for ch in 'asxm':
                ss = [set(x) for c, x in ranges if c == ch]
                if ss:
                    s = set.intersection(*ss)
                    total *= len(s)
                    print(f'     len is {len(s)}')
                else:
                    total *= MAX_NUM
            print(f'        Total: {total}\n')
            grand_total += total

            all_ranges += ranges[:]
            return rrr
        elif cur_workf == 'R':
            return 0
        else:
            return do_stuff(None, next_line_workf=cur_workf, ranges=ranges)

    if cond == '<':
        # a<2006 ---> 1-2005
        r1 = (range(1, num))
        new_ranges = ranges[:]
        new_ranges.append((x, r1))
        rrr += do_stuff(next_line_workf, cur_workf, ranges=new_ranges)

        # not a<2006 ---> 2006-4000
        r2 = (range(num, MAX_NUM+1))
        new_ranges = ranges[:]
        new_ranges.append((x, r2))
        # print(f'< range: {r1} {r2}')
        rrr += do_stuff(workf_list=next_line[1:], next_line_workf=None, ranges=new_ranges)

    if cond == '>':
        # x>2662 ---> 2663-4000
        r1 = (range(num+1, MAX_NUM+1))
        new_ranges = ranges[:]
        new_ranges.append((x, r1))
        rrr += do_stuff(next_line_workf, cur_workf, ranges=new_ranges)
        
        # not x>2662 ---> 1-2662
        r2 = (range(1, num+1))
        new_ranges = ranges[:]
        new_ranges.append((x, r2))
        rrr += do_stuff(workf_list=next_line[1:], next_line_workf=None, ranges=new_ranges)
        # print(f'> range: {r1} {r2}')
    return rrr

rrr = do_stuff(next_line_workf='in')
print(rrr)
print(grand_total)
# for ch in 'asxm':
#     sets_for_ch = [x for c, x in all_ranges if c == ch]
#     print(f'sets for {ch}: {sets_for_ch}')
#     s = set.intersection(*[set(x) for c, x in all_ranges if c == ch])
#     print(f'len for {ch} is {len(s)}')

aoc.print_result(2, result2, exp2)
'''
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''