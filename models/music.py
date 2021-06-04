import sqlalchemy
from .db_session import SqlAlchemyBase



class Music(SqlAlchemyBase):
    __tablename__ = 'music'


    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = sqlalchemy.orm.relation('User')
    music_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("all_music.id"))
    music = sqlalchemy.orm.relation('All_music')


    def get_id(self):
        return str(self.id)
