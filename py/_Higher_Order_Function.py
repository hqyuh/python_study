
# def loud(text):
#     return text.upper()
#
#
# def hello(func):
#     text = func("hello")
#     print(text)
#
#
# hello(loud)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))




