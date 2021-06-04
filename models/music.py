import sqlalchemy
from .db_session import SqlAlchemyBase



class Music(SqlAlchemyBase):
    __tablename__ = 'music'


    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(120), index=True, unique=True)
    count = sqlalchemy.Column(sqlalchemy.Integer)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = sqlalchemy.orm.relation('User')


    def get_id(self):
        return str(self.id)
