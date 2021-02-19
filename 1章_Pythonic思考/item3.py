a = b'h\x65llo\x3f'
print(list(a))
print(a)

"""
[104, 101, 108, 108, 111, 63]
b'hello?'
"""

a = 'a\u0300 propos'
print(list(a))
print(a)

"""
['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']
à propos
"""


"""メモ
エンコード：人語 ⇒ 機械語
デコード：機械語 ⇒ 人語
en = make: ～にする
de = down: 下に

ここで言いたいのはバイナリデータ、テキストデータは自動的には変換されず、
変換するためにはdecodeしなければならない。
"""


def to_Str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_Str(b'foo')))
print(repr(to_Str('bar')))
print(to_Str(b'foo'))
print(to_Str('bar'))


"""
'foo'
'bar'
foo
bar
"""

print(b'red' > b'blue')
print('red' > 'blue')

"""
True
True
"""

assert b'red' > b'blue'
assert 'red' > 'blue'

"""
"""
