class Flight(object):
    def __init__(self, aid, fid, fdestination):
        self.aid = aid
        self.fid = fid
        self.fdestination = fdestination

    def __str__(self):
        return "aid = %d, fid = %d, fdestination = %s" % (self.aid, self.fid, self.fdestination)

    def __eq__(self, o):
        return self.fid == o.fid


