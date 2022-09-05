from redis import Redis

class Commands:

    """Contains the most basic implementation of Redis functions
    and commands like 
        - set : set key - value with optional expiration settings
        - get : search and get value by key
        - append : append/add elements on existing value
        - mset : set a collection of key - value items
        - mget : get a list of values from a list of keys
        - getdel : find, get and delete item (in that specific order)
    """

    def __init__(self,r:Redis) -> None:
        self.__r=r


    def close(self):
        self.__r.quit()
        self.__r=None
        

    def __validate_key_value(self,key:str,value:str)->bool:
        """_summary_

        Args:
            key (str): _description_
            value (str): _description_

        Returns:
            bool: False if key and value are not (str)
        """
        if not isinstance(key,str) or not isinstance(value,str):
            print("Redis set operation : key and value must be strings")
            return False 
        return True


    def get(self,key:str)->str:
        """Returns the value of the key if exists.
        If the key does not exists returns None.

        Args:
            key (str): key

        Returns:
            str: value of (key)
            None: If the key does no exists or error
        """
        if not self.__validate_key_value(key,"value"):
            return None
        try:
            return self.__r.get(key).decode("utf-8")
        except Exception as err:
            print(f"Redis get operation : {err}")
            return None

    
    def set(self,key:str,value:str,**kargs)->bool:
        """Set the a key value pair. If the key already exists,
        the old value is replaced for the new value.
        The value must be a string.
        Additional parameters can be specified like : 

            - ex (int)    expiration time in seconds
            - exat (int)  set the specified time stamp in seconds at wich the key will expire
            - nx (bool)   set if the key does not exists
            - xx (bool)   set only if the key exists
        
        Args:
            r (redis): redis cursor 
            key (str): key 
            value (str): value 

        Returns:
            bool: True if the operation soceeded
            bool: False if the operation failed
        """
        if not self.__validate_key_value(key,value):
            return False
        try:
            result=self.__r.set(
                name=key,
                value=value,
                ex=kargs.get("ex"),
                exat=kargs.get("exat"),
                nx=kargs.get("nx"),
                xx=kargs.get("xx")
            )
            if result=="OK":
                return  True 
            return False
        except  Exception as err:
            print(f"Redis set operation failed : {err}")
            return False


    def append(self,key:str,value:str)->int:
        """If key already exists and is a string, 
        this command appends the value at the 
        end of the string. If key does not exist it is created 
        and set as an empty string. If the operations suceesd it 
        returns the number of characters/elements appendt ->(int). 
        Key and value must always be strings , example:
         - name "Jhon"
         - address "12345"

        Args:
            key (str): key
            value (str): key value

        Returns:
            int: return the numer of characters or elements added (return can be 0)
            bool: return false if the operation failed
        """
        if not self.__validate_key_value(key,value):
            return False
        try:
            return self.__r.append(key,value)
        except Exception as err:
            print(f"Redis append operation failed : {err}")
            return False


    def mset(self,items:dict)->bool:
        """Takes a dictionary as argument.
        Sets the keys and their respective values.
        If any given key already exists, its value is 
        replaced by the new value.

        Args:
            items (dict): Map of keys and values. Keys and values must be strings

        Returns:
            bool: True if the operation suceeded.
            bool: False if the operation failed.
        """
        if not isinstance(items,dict):
            print("Redis mset operation : arg items must be type (dict)")
            return False
        try:
            return self.__r.mset(items)
        except Exception as err:
            print(f"Redis mset operation failed : {err}")
            return False
        
    
    def mget(self,items:list)->list:
        """Takes a list of keys.
        Returns a list of values corresponding to each key.
        If a key does no exists or does not hold a value
        that value will be None

        Args:
            items (list): list of keys

        Returns:
            list: list of values for each key
            None: returns None if the operation failed
        """
        if not isinstance(items,list):
            print("Redis mget operation : arg items must be type (list)")
        try:
            return self.__r.mget(items)
        except Exception as err:
            print(f"Redis mget operation failed : {err}")
            return None

    
    def getdel(self,key:str)->bool:
        """Finds a key, returns its value and deletes the key.

        Args:
            key (str): key

        Returns:
            str: Returns the value of the key before deleting it.
            bool: False if the key wasnt found
        """

        if not self.__validate_key_value(key,"value"):
            return  False
        try:
            result=self.__r.getdel(key)
            if result is not None:
                return result
            return False
        except Exception as err:
            print(f"Redis getdel operation failed : {err}")
            return False