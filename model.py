#
# model definitions
#


class Config:
    def __init__(self, path):
        self.path = path
        self.tmp_path = self.path + "/tmp"
        self.templates_path = self.path + "/templates"
        self.html_path = self.path + "/html"
        self.output_filepath = self.html_path + "/index.html"

    def __repr__(self):
        return "<Config()>"


class Card:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __repr__(self):
        return "<Card(name={self.name!r})>".format(self=self)


class Host:
    def __init__(self, name, cards, updated):
        self.name = name
        self.cards = cards
        self.updated = updated

    def __repr__(self):
        return "<Host(name={self.name!r}, updated={self.updated!r})>".format(self=self)


class Hosts:
    def __init__(self, hosts, updated):
        self.hosts = hosts
        self.updated = updated

    def __repr__(self):
        return "<Hosts(updated={self.updated!r})>".format(self=self)
