from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

convention = {
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
}

metadata = MetaData( naming_convention = convention)

Base = declarative_base() # metadata = md

engine = create_engine('sqlite:///puzzle.db')
Session = sessionmaker( bind = engine)

session = Session()

class Puzzle(Base):

    __tablename__ = 'puzzles'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'<Puzzle id: {self.id} name: {self.name}>'

class Choice(Base):
    __tablename__ = 'choices'

    id = Column(Integer(), primary_key=True)
    puzzle_id = Column(Integer(), ForeignKey('puzzles.id'))
