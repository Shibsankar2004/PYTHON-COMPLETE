class Vector:
    def __init__(self, l):
        self.l = l

    def __add__(self, other):
        result = []
        for i in range(len(self.l)):
            result.append(self.l[i] + other.l[i])
        return Vector(result)

    def __mul__(self, other):
        dot = 0
        for i in range(len(self.l)):
            dot += self.l[i] * other.l[i]
        return dot

    def __str__(self):
        return str(self.l)


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Sum =", v1 + v2)
print("Dot Product =", v1 * v2)
