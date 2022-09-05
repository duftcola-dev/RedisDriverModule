from http import server
import redis
from driver.utils.commands import Commands
from driver.utils.client import Client
from driver.utils.users import Users
from driver.utils.test import Test
class Driver:

    __instance=None

    def __init__(self) -> None:
        self.__r=None
        if self.__instance is not None:
            raise Exception("Driver can only be instanciated once")
        Driver.__instance=self

    
    def connect(self,host:str="localhost",port:int=6379,password:str=None,db:int=0)->bool:
        try:
            self.__r=redis.Redis(host=host,port=port,password=password,db=db)
            self.commands=Commands(self.__r)
            self.client=Client(self.__r)
            self.users=Users(self.__r)
            self.test=Test(self.__r)
            if not self.__r.ping():
                print("Redis online but connection cannot be stablished")
                return False
            return True
        except Exception as err:
            print("Connection to Redis server failed")
            print(err)
            return False
      


    def close(self)->bool:
        if self.__r == None:
            print("Redis driver : No connection has been stablished with redis")
            return True
        result=self.__r.quit()
        if result:
            self.commands.close()
            self.client.close()
            self.users.close()
            self.test.close()
            self.__r=None
            return True
        return False


    @staticmethod
    def get_instance():
        if Driver.__instance is None:
            Driver()
        return Driver.__instance
