from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

convention = {
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
}

metadata = MetaData( naming_convention = convention)

Base = declarative_base(metadata = metadata) # metadata = md

engine = create_engine('sqlite:///puzzle.db')
Session = sessionmaker( bind = engine)

session = Session()


class Puzzle(Base):

    __tablename__ = 'puzzles'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    question = Column(String())

    choices = relationship('Choice', back_populates = 'puzzle')

    outcomes = relationship('Outcome', back_populates = 'puzzle')
    

    def __repr__(self):
        return f'<Puzzle id: {self.id} name: {self.name} question: {self.question}>'
    

        
class Choice(Base):

    __tablename__ = 'choices'

    id = Column(Integer(), primary_key=True)
    puzzle_id = Column(Integer(), ForeignKey('puzzles.id'))
    outcome_id = Column(Integer(), ForeignKey('outcomes.id'))
    answer = Column(String())
    #situaton.id = Column(Integer(), ForeignKey('situations.id'))

    puzzle = relationship('Puzzle', back_populates = 'choices')

    outcome = relationship('Outcome', back_populates = 'choices')

    def __repr__(self):
        return f'<Choice id: {self.id}'

class Outcome(Base):
    
    __tablename__ = 'outcomes'

    id = Column(Integer(), primary_key=True)
    puzzle_id = Column(Integer(), ForeignKey('puzzles.id'))
    name = Column(String())

    choices = relationship('Choice', back_populates = 'outcome')

    puzzle = relationship('Puzzle', back_populates = 'outcomes')

    def __repr__(self):
        return f'<Outcome id: {self.id}'

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///puzzle.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker( bind = engine)

    session = Session()

    puzzle_one = Puzzle(
        name = 'puzzle_one',
        question = 'I am a question',
    )
    session.add(puzzle_one)
    session.commit()