def test():
    string = "中文"
    utf_8_bytes = string.encode(encoding="utf-8")
    gbk_bytes = string.encode(encoding='gbk')
    print('utf-8 bytes ', utf_8_bytes)
    print('gbk bytes ', gbk_bytes)


if __name__ == '__main__':
    test()
