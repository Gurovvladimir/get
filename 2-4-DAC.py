def decimal2binary(value):
    return [int(x) for x in bin(value)[2:].zfill(10)]
print(decimal2binary(277))