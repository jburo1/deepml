class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += 1 * out.grad
            other.grad += 1 * out.grad
        out._backward = _backward

        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward

        return out

    def relu(self):
        val = 0
        if self.data > 0:
            val = self.data
        out = Value(val, (self, ), 'relu')

        def _backward():
            if self.data > 0:
                self.grad += 1 * out.grad
            else:
                self.grad += 0
        out._backward = _backward

        return out

    # topological sort
    def backward(self):
        topo = []
        visited = set()

        def build_topo(v):
            if v not in visited:
                visited.add(v)
            for child in v._prev:
                build_topo(child)
            topo.append(v)

        self.grad = 1

        build_topo(self)

        for node in reversed(topo):
            node._backward()

# a = Value(2)
# b = Value(-3)
# c = Value(10)
# d = a + b * c
# e = d.relu()
# e.backward()
# print(a, b, c, d, e)


a = Value(2)
b = Value(3)
c = Value(10)
d = a + b * c
e = Value(7) * Value(2)
f = e + d
g = f.relu()
g.backward()
print(a, b, c, d, e, f, g)
