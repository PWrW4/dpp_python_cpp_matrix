from ctypes import cdll
lib = cdll.LoadLibrary('./cygdpp_python_powerLibCPP.dll')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)





def main():
    f = Foo()
    f.bar()


main()
print("Guru99")