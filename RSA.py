import random


class RSA:
    # initialize needed parameters
    P = 0
    Q = 0
    N = 0
    AlphaN = 0
    e = 0
    d = 0
    # use this table to map given letters
    characters = [['a', 0], ['b', 1], ['c', 2], ['d', 3], ['e', 4], ['f', 5], ['g', 6], ['h', 7], ['i', 8],
                  ['j', 9], ['k', 10], ['l', 11], ['m', 12], ['n', 13], ['o', 14], ['p', 15], ['q', 16], ['r', 17],
                  ['s', 18], ['t', 19], ['u', 20], ['v', 21], ['w', 22], ['x', 23], ['y', 24], ['z', 25],
                  ['A', 26], ['B', 27], ['C', 28], ['D', 29], ['E', 30], ['F', 31], ['G', 32], ['H', 33], ['I', 34],
                  ['J', 35], ['K', 36], ['L', 37], ['M', 38], ['N', 39], ['O', 40], ['P', 41], ['Q', 42], ['R', 43],
                  ['S', 44], ['T', 45], ['U', 46], ['V', 47], ['W', 48], ['X', 49], ['Y', 50], ['Z', 51], [' ', 52]
                  ]
    e_possible_values = []

    def __init__(self, p, q):
        self.P = p
        self.Q = q
        self.N = self.P * self.Q
        self.AlphaN = (self.P - 1) * (self.Q - 1)

    def ComputeE(self):
        # compute all possible values of e:
        for a in range(2, self.AlphaN - 1):
            if self.computeGCD(a, self.AlphaN) == 1:
                self.e_possible_values.append(a)

        return self.e_possible_values

    def KeyGeneration(self, i):
        if i == 0:
            self.e = random.choice(self.e_possible_values)
        elif i in self.e_possible_values:
            self.e = i
        else:
            print("unaccepted input")

        # compute d:
        self.d = pow(self.e, -1, self.AlphaN)
        return [self.e, self.N]

    # resulted values from encryption
    resulted_nums = []

    def Encryption(self, l):
        nums = list()
        for w in l:
            for r in self.characters:
                if w == r[1]:
                    # first: we take M, the value of the letter from the characters list
                    temp = pow(r[1], self.e) % self.N
                    self.resulted_nums.append(temp)
                    # second: we use the result to get the new letter with encryption
                    c = temp % 52
                    for t in self.characters:
                        if c == t[1]:
                            nums.append(t[0])
        return nums

    def Decryption(self):
        nums = list()
        for w in self.resulted_nums:
            # first: we take C, the value of the letter
            temp = pow(w, self.d) % self.N
            # second: we use the result to get the letter encrypted
            for t in self.characters:
                if temp == t[1]:
                    nums.append(t[0])
        return nums

    # a helper method to calculate gcd.
    @staticmethod
    def computeGCD(x, y):

        if x > y:
            small = y
        else:
            small = x
        for i in range(1, small + 1):
            if (x % i == 0) and (y % i == 0):
                gcd = i

        return gcd
