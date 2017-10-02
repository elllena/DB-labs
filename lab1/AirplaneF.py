class Airplane(object):
    def __init__(self, aid, aname, amodel):
        self.aid = aid
        self.aname = aname
        self.amodel = amodel
    def __str__(self):
        return "aid = %d,aname = %s, amodel = %s" % (self.aid, self.aname, self.amodel)
    def __eq__(self, o):
        return self.aid == o.aid
