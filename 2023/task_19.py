import aoc

lines = aoc.get_lines(__file__)
result1, result2 = 0, 0
exp1, exp2 = 19114, 167409079868000

# Common
STARTING_WORKFLOW = 'in'
REJECTED, ACCEPTED = 'R', 'A'
workflows = {}
for line in lines:
    if line == '':
        break
    w_name, rules = line[:-1].split('{')
    rules = rules.split(',')
    w = []
    for r in rules:
        if ':' in r:
            op, target = r.split(':')
            w.append((op[0], op[1], int(op[2:]), target))
        else:
            w.append((None, None, None, r))
    workflows[w_name] = w
    # print(workflows[w_name])

ratings = []
for line in lines[len(workflows)+1:]:
    ratings_in_line = line[1:-1].split(',')
    r = {}
    for rating in ratings_in_line:
        name, number = rating.split('=')
        r[name] = int(number)
    ratings.append(r)
    # print(r)

# Part 1
aoc.mark_task_start()
total_rating = 0
for rating in ratings:
    done = False
    curr_workflow = 'in'
    while not done:
        if curr_workflow == REJECTED:
            break
        elif curr_workflow == ACCEPTED:
            total_rating += sum(rating.values())
            break
        conditions = workflows[curr_workflow]
        for cat, op, number, next_workflow in conditions:
            if cat == None:
                if next_workflow == REJECTED:
                    done = True
                elif next_workflow == ACCEPTED:
                    total_rating += sum(rating.values())
                    done = True
                else:
                    curr_workflow = next_workflow
                    break
            elif op == '<' and rating[cat] < number or op == '>'and rating[cat] > number:
                curr_workflow = next_workflow
                break

result1 = total_rating
aoc.print_result(1, result1, exp1)

# Part 2
aoc.mark_task_start()
MAX_NUM = 4000
CATEGORIES = 'asxm'
total_combinations = 0

def compute_combinations(ranges):
    # print(f'Possible ranges: {ranges}')
    combinations = 1
    for category in 'asxm':
        set_of_ranges = [set(r) for cat, r in ranges if cat == category]
        # if there is no ranges for given category, it means it can have all values from <1-4000>
        combinations *= len(set.intersection(*set_of_ranges)) if set_of_ranges else MAX_NUM
    return combinations

def process_workflows(ranges, workflow_rules, workflow):
    global total_combinations

    if workflow == ACCEPTED:
        total_combinations += compute_combinations(ranges)
        return
    elif workflow == REJECTED:
        return
    
    next_line = workflows[workflow] if workflow else workflow_rules
    first_rule, remaining_rules = next_line[0], next_line[1:]
    cat, op, number, next_workflow = first_rule

    if cat == None:
        if next_workflow == ACCEPTED:
            total_combinations += compute_combinations(ranges)
        elif next_workflow != REJECTED:
            process_workflows(ranges, None, next_workflow)
        return

    if op == '<':
        # Example: a<2006  =>  range <1-2005> if condition met, <2006-4000> if not
        r1, r2 = range(1, number), range(number, MAX_NUM + 1)
        # Branch for condition met - pass name of next workflow
        process_workflows(ranges + [(cat, r1)], None, next_workflow)
        # Branch for condition not met - pass remaining rules from current line
        process_workflows(ranges + [(cat, r2)], remaining_rules, None)
    elif op == '>':
        # Example: x>2662  =>  range <2663-4000> if condition met, <1-2662> if not
        r1, r2 = range(number + 1, MAX_NUM + 1), range(1, number + 1)
        # Branch for condition met - pass name of next workflow
        process_workflows(ranges + [(cat, r1)], None, next_workflow)
        # Branch for condition not met - pass remaining rules from current line
        process_workflows(ranges + [(cat, r2)], remaining_rules, None)

process_workflows([], None, 'in')
result2 = total_combinations
aoc.print_result(2, result2, exp2)
