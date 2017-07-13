from pony import orm

class Database(object):

    db = None

    def __init__(self):
        self.db = orm.Database()


class Factoid(orm.Entity):
    keyword = orm.Required(str)
    info = orm.Required(str)
