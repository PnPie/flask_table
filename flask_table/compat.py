# coding:utf-8

# 用meta创建一个类
def with_metaclass(meta, base=object):
    return meta("NewBase", (base,), {})
