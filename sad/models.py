
from sqlalchemy.ext.declarative import declarative_base
from pyramid.security import Allow, Everyone
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from sqlalchemy import Column, Integer, String, DateTime, BOOLEAN, Text
from sqlalchemy import Numeric, func, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass

# Primary Class


class User(Base):
    __tablename__ = 'Users'

    idUser = Column(Integer, primary_key=True)
    UserName = Column(String, nullable=False)
    UserPass = Column(String, nullable=False)
    LastName = Column(String)
    FirstName = Column(String)
    Email = Column(String)
    VKID = Column(String)
    TelNum = Column(String)

    password_hash = Column(Text)

    def set_password(self, pw):
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.password_hash = pwhash.decode('utf8')

    def check_password(self, pw):
        if self.password_hash is not None:
            expected_hash = self.password_hash.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False

    Child = Column(Integer, ForeignKey("Childs.idChild"))

    def __repr__(self):
        return "<User(%r)>" % (
            self.UserName
        )


class Group(Base):
    __tablename__ = 'Groups'

    idGroup = Column(Integer, primary_key=True)
    GroupName = Column(String, nullable=False)
    VospName = Column(String, nullable=False)

    Child = Column(Integer, ForeignKey("Childs.idChild"))
    Event = Column(Integer, ForeignKey("Events.idEvent"))

    def __repr__(self):
        return "<Group(%r)>" % (
            self.GroupName
        )


class Event(Base):
    __tablename__ = 'Events'

    idEvent = Column(Integer, primary_key=True)
    EventName = Column(String, nullable=False)
    EventDate = Column(DateTime, nullable=False)
    EventTime = Column(String)
    EventPlace = Column(String)

    def __repr__(self):
        return "<Event(%r, %r)>" % (
            self.EventName, self.EventDate
        )


class Child(Base):
    __tablename__ = 'Childs'

    idChild = Column(Integer, primary_key=True)
    Age = Column(String, nullable=False)
    Name = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<member(%r, %r)>" % (
            self.Name, self.Age
        )

if __name__ == '__main__':
    import codecs
    import sadisplay

    desc = sadisplay.describe(globals().values())

    with codecs.open('schema.plantuml', 'w', encoding='utf-8') as f:
        f.write(sadisplay.plantuml(desc))

    with codecs.open('schema.dot', 'w', encoding='utf-8') as f:
        f.write(sadisplay.dot(desc))
