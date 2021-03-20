import random

out_test_boys = open("boys.test.split", "w+")
out_train_boys = open("boys.train.split", "w+")

with open("boys.train") as boys:
    boy_lines = boys.read().splitlines()
    num_boys = len(boy_lines)
    test_inds = set(random.sample(list(range(num_boys)), int(0.2*num_boys)))
    num_train = 0
    num_test = 0
    for i, line in enumerate(boy_lines):
        if line == "":
            continue
        if i in test_inds:
            if num_test > 0:
                out_test_boys.write("\n")
            num_test += 1
            out_test_boys.write(line)
        else:
            if num_train > 0:
                out_train_boys.write("\n")
            num_train += 1
            out_train_boys.write(line)

out_test_girls = open("girls.test.split", "w+")
out_train_girls = open("girls.train.split", "w+")

with open("girls.train") as girls:
    girls_lines = girls.read().splitlines()
    num_girls = len(girls_lines)
    test_inds = set(random.sample(range(num_girls), int(0.2*num_girls)))
    num_train = 0
    num_test = 0
    for i, line in enumerate(girls_lines):
        if line == "":
            continue
        if i in test_inds:
            if num_train > 0:
                out_test_girls.write("\n")
            num_train += 1
            out_test_girls.write(line)
        else:
            if num_test > 0:
                out_train_girls.write("\n")
            num_test += 1
            out_train_girls.write(line)