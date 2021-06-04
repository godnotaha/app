import sqlalchemy
from .db_session import SqlAlchemyBase



class All_music(SqlAlchemyBase):
    __tablename__ = 'all_music'


    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(120))
    name_author = sqlalchemy.Column(sqlalchemy.String(120))
    link = sqlalchemy.Column(sqlalchemy.String)
    link_img = sqlalchemy.Column(sqlalchemy.String)
    duration_of_music = sqlalchemy.Column(sqlalchemy.String(120))

    def get_id(self):
        return str(self.id)