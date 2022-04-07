def permute(inp):
    n = len(inp)

    # Number of permutations is 2^n
    mx = 1 << n

    # Converting string to lower case
    inp = inp.lower()
    a = []
    # Using all subsequences and permuting them
    for i in range(mx):
        # If j-th bit is set, we convert it to upper case
        combination = [k for k in inp]
        for j in range(n):
            if ((i >> j) & 1) == 1:
                combination[j] = inp[j].upper()

        temp = ""
        # Printing current combination
        for i in combination:
            temp += i
        # print(temp)
        a.append(temp)
    bye = '$Nayeon is hot'
    for i in a:
        if i in bye:
            hi = bye.replace(i, 'Dahyun')
    print(hi)

# Driver code
permute("$nayeon")
