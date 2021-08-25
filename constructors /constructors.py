class const:
    def __init__(self):
        self.num = 100
        self.name = 'sameer'
        self.lastname = 'mohd'

    def read_number(self):
        __priv="This is from private variable"
        _proc="This is from protected variable"
        print(self.num)
        print(__priv+" "+_proc)

    def read_name(self):
        print(self.name, self.lastname)

    def arg_const(self, address, company):
        print(address + " " + company)


obj = const()

obj.read_number()
obj.read_name()


class subclass(const):
    ob1 = const()
    ob1.arg_const("warangal", 'SGTS')
