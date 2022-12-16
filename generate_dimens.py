def generate_dimens(n_range, multiplier):
    with open("dimens.xml", 'w') as f:
        f.writelines("<resources>\n")
        for i in drange(1, n_range + 1, 0.5):
            print(round(i * multiplier, 1))
            f.writelines("\t<dimen name=\"dp_{origin}\">{converted}dp</dimen>\n".format(origin="{:g}".format(i),
                                                                                        converted=round(i * multiplier,
                                                                                                        1)))
        f.writelines("</resources>")


def input_range_and_multiplier():
    range = input("请输入range:")
    multiplier = input("请输入multiplier:")
    generate_dimens(int(range), float(multiplier))


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


if __name__ == '__main__':
    input_range_and_multiplier()
