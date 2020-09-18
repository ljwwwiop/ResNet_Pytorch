class Person:
    def __init__(self,name= "Lian"):
        self.name = name

class Puple(Person):
    pass

class Puple_init(Person):
    def __init__(self,age):
        super(Puple_init, self).__init__()
        self.age = age

p = Puple()
p2 = Puple_init(20)
# print(p.name)
# print(p2.name,p2.age)


class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C(A):
    def __init__(self):
        print('C')
        super().__init__()


class D(A):
    def __init__(self):
        print('D')
        super().__init__()


class E(B, C):
    def __init__(self):
        print('E')
        super().__init__()


class F(C, D):
    def __init__(self):
        print('F')
        super().__init__()


class G(E, F):
    def __init__(self):
        super().__init__()
        print('G')


g = G()


