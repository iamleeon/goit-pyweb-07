from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///faculty.db")
Session = sessionmaker(bind=engine)
session = Session()
