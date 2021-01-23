import os

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

password = os.environ["PASSWORD"]

url = f'mysql://root:{password}@127.0.0.1:3306/krolewstwo'

engine = sqlalchemy.create_engine(url)

Session = sessionmaker(engine)

if __name__ == '__main__':
    print(list(engine.execute("SHOW TABLES;")))
