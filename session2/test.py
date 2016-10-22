import MyClass

def test_first_law():
    obj1 = MyClass.MyClass(4,8)
    obj1.count() == 0
    obj1.addCell(2,2)
    obj1.count() == 1
