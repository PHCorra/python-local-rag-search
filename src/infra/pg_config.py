from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Embedding(Base):
    __tablename__ = "embeddings"
    id = Column(Integer, primary_key=True, index=True)
    embedding = Column(ARRAY(Integer), nullable=False)


Base.metadata.create_all(bind=engine)


def open_postgres_session():
    print("opening DB connection")
    return SessionLocal()


def test_add_data():
    session = open_postgres_session()
    try:
        vector_data = [0.5, 0.1, 0.9]
        new_embedding = Embedding(embedding=vector_data)
        session.add(new_embedding)
        session.commit()
        print("Data added successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error occured: {e}")
    finally:
        session.close()


def test_show_data():
    session = open_postgres_session()
    try:
        embeddings = session.query(Embedding).all()
        for embedding in embeddings:
            print(f"ID: {embedding.id}, Embedding: {embedding.embedding}")
    except Exception as e:
        print(f"Error ocurred: {e}")
    finally:
        session.close()
