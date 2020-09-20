from abc import ABC, abstractmethod

"""
    다양한 제품군의 DB Connection 역할을 수행하는 메소드
    팩토리 메소드 패턴 및 클래스 다형성을 추가해서 적용한다
"""

# 파이썬 abstractmethod 데코레이터를 활용해서 추상 메소드 선언
class DBManager(ABC):
    @abstractmethod
    def connection(self):
        pass 

class SqlServer(DBManager):
    def connection(self):
        return ('Microsoft Database Connected...')

class Oracle(DBManager):
    def connection(self):
        return ('Oracle Database Connected...')

class MariaDB(DBManager):
    def connection(self):
        return ('Maria Database Connected...')

# DbConnFactory 클래스 인스턴스 생성

class DbConnFactory:
    def get_db_connection(self, db):
        return db.connection()

if __name__ == "__main__":
    db_factory = DbConnFactory()

    print(db_factory.get_db_connection(SqlServer()))
    print(db_factory.get_db_connection(Oracle()))
    print(db_factory.get_db_connection(MariaDB())) 
    