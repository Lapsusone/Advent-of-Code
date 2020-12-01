import os

lines = (
    int(x)
    for x in open(os.path.join(os.path.dirname(__file__), "input_test.txt"))
    .read()
    .splitlines()
)

for a in lines:
    if (2020 - a) in lines:
        print((2020 - a) * a)
