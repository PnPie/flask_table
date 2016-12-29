# coding:utf-8


def with_metaclass(meta, base=object):  # 用meta创建一个类
    return meta("NewBase", (base,), {})
