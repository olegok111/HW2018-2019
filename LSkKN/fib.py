s = input()
beg_on_max_len = 1
max_len_fib = 1
for beg in range(len(s)-1):
    if s[beg] == s[beg+1]:
        continue
    prev_fib = s[beg]
    cur_fib = s[beg] + s[beg+1]
    while s[beg:beg+len(cur_fib)] == cur_fib:
        tmp = cur_fib
        cur_fib += prev_fib
        prev_fib = tmp
    if max_len_fib < len(prev_fib):
        max_len_fib = len(prev_fib)
        beg_on_max_len = beg
print(beg_on_max_len+1, beg_on_max_len + max_len_fib)