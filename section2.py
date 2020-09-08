a = 1 + 2

# aの値を標準出力に出力します。
print(a)
# => a

# idはpythonのbuilt-in functionです。
# Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
# オブジェクトとしての固有値を出力してくれる、という理解でいいのかな。
print(id(a))
# => 4545919968
# 実行するごとに変化します。

# typeもpythonのbuilt-in functionで、
# With one argument, return the type of an object. The return value is a type object and generally the same object as returned by object.__class__.
# だそうです。つまり、
print(type(a))
# => <class 'int'>
# は、
print(a.__class__)
# => <class 'int'>
# と同値になるということですね。
