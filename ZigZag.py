
# = fields/variables = #
s = "PAYPALISHIRING"
numRows = 4

# = methods = #
def convert(s, numRows):
    if numRows == 1 or len(set(s)) == 1 or len(s) <= numRows:
        return s

    result = [[s[i]] for i in range(numRows)]
    print(result)
    j = numRows - 2
    backward = True if j > 0 else False

    for i in range(numRows, len(s)):
        result[j].append(s[i])
        print(result)
        if backward:
            j -= 1
        else:
            j += 1

        if j == numRows - 1 or j == 0:
            backward = not backward

    return ''.join(list(map(''.join, result)))

print(convert(s, numRows))
