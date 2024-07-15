class Grammar:
    def __init__(self, rules):
        self.rules = rules
        self.patterns = dict()
        for rule, values in rules.items():
            print(rule)
            print(values)
            for value in values:
                self.patterns[value] = rule

    def get_rule(self, pattern):
        while len(pattern) > 0:
            if pattern in self.patterns:
                return self.patterns[pattern], len(pattern)
            pattern = pattern[1:]
        return None, 0
