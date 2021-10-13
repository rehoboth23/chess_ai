def test_dump_files():
    f1 = open("alpha_beta", "r+")
    f2 = open("minmax", "r+")
    l1 = f1.readlines()
    l2 = f2.readlines()
    print(l1)
    print(l2)
    print(l1 == l2)
    f1.truncate(0)
    f2.truncate(0)
    f1.close()
    f2.close()


test_dump_files()
