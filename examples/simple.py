from flask_table import Table, DatetimeCol

from datetime import datetime

"""Lets suppose that we have a class that we get an iterable of from
somewhere, such as a database. We can declare a table that pulls out
the relevant entries, escapes them and displays them.

"""


class Item(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class ItemTable(Table):
    datetime = DatetimeCol('Time')


def main():
    items = [
        Item(datetime=datetime(2014, 1, 1, 10, 20, 30)),
        Item(datetime=None)]

    table = ItemTable(items)

    # or {{ table }} in jinja
    print(table.__html__())

    """Outputs:

    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Name1</td>
          <td>Description1</td>
        </tr>
        <tr>
          <td>Name2</td>
          <td>Description2</td>
        </tr>
        <tr>
          <td>Name3</td>
          <td>Description3</td>
        </tr>
      </tbody>
    </table>

    Except it doesn't bother to prettify the output.
    """


if __name__ == '__main__':
    main()
