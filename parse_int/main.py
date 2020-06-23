digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9}

teens = {"ten": 10,
            "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19}

tens = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}

nums = {**digits, **teens, **tens}

mag2str = {
    10: "ten",
    100: "hundred",
    1000: "thousand",
    1000000: "million"
}

next_mag = {
    1000000: 1000,
    1000: 100,
    100: 10
}

def parse_small(tokens):
    total = 0
    for token in tokens:
        if token in ('thousand', 'hundred', 'million'):
            continue
        elif "-" in token:
            total += parse_small(token.split("-"))
        else:
            total += nums[token]
    return total

def parse(tokens, magnitude):
    if magnitude <= 10:
        return parse_small(tokens)

    idx = 0
    for i, s in enumerate(tokens):
        if s == mag2str[magnitude]:
            idx = i
    return parse(tokens[:idx], next_mag[magnitude]) * magnitude + parse(tokens[idx:], next_mag[magnitude])

def parse_int(string):
    if string == "zero":
        return 0
    split = string.replace(" and ", " ").split()
    return parse(split, 1000000)

class Test:
    @staticmethod
    def assert_equals(a, b):
        assert a == b, "{} is not equal to {}".format(a, b)

if __name__ == '__main__':
    Test.assert_equals(parse_int('one'), 1)
    Test.assert_equals(parse_int('twenty'), 20)
    Test.assert_equals(parse_int('forty six'), 46)
    Test.assert_equals(parse_int('two hundred forty-six'), 246)
    Test.assert_equals(parse_int('three hundred thousand fifty-two'), 300052)
    Test.assert_equals(parse_int('six hundred fifty-seven'), 657)
    Test.assert_equals(parse_int('two million'), 2000000)
    Test.assert_equals(parse_int('one hundred twenty three thousand'), 123000)
    Test.assert_equals(parse_int('one hundred'), 100)
    Test.assert_equals(parse_int('zero'), 0)
    Test.assert_equals(parse_int('one hundred thousand'), 100000)
    Test.assert_equals(parse_int('one hundred and thirty thousand'), 130000)
    Test.assert_equals(parse_int('one hundred twenty three thousand'), 123000)
