from redis import Redis 


class Client:
    """Contains client related functions like:
        - get_client_id : Returns the current client id.
        - get_client_info : Returns partial or all the information about the current client.
        - get_client_list : Returns a list of the current clients connected to Redis.
        - kill : Closes the connection of the specified client.
        - set_client_name : Sets a name or alias for the connection of the current client.
        - echo : Sends a echo command string to the Redis server.
    """
    def __init__(self,r:Redis) -> None:
        self.__r=r

    
    def close(self):
        """Destroys the current local(class) client instance
        """
        self.__r.quit()
        self.__r=None
    

    def get_client_id(self)->str:
        """Returns the id of the current client connected to the database

        Returns:
            str: id
        """
        return self.__r.client_id()


    def get_client_info(self,all:bool=False)->dict:
        """Returns total or partial info about the current client.

        Args:
            all (bool, optional): If false only relevant information is returned about 
            the current client. If true a dictionary is returned with all the information
            about the current client. Defaults to False.

        Returns:
            dict: Client information
        """
        if not all:
            client_info={
                "id":self.__r.client_info()["id"],
                "addr":self.__r.client_info()["addr"],
                "laddr":self.__r.client_info()["laddr"],
                "fd":self.__r.client_info()["fd"],
                "name":self.__r.client_info()["name"],
                "db":self.__r.client_info()["db"],
            }
            return client_info
        else:
            return self.__r.client_info()

    
    def get_client_list(self)->list:
        """Returns a list with all the clients currently connected to the 
        Redis server.

        Returns:
            list: list of clients
        """
        return self.__r.client_list()


    def kill(self,address:str)->bool:
        """Closes de connection of the specified client

        Args:
            address (str): Addres of the client to be shut down.
            Use the following format : ip_address:port as a string.
            EXAMPLE : 
                "127.0.0.1:6523"
            You can get the address of all the client with get_client_list()
        Returns:
            bool: _description_
        """
        if not isinstance(address,str):
            print("Redis kill operation : wrong data type. Args must be both strings")
            return False
        try:
            return self.__r.client_kill(address=address)
        except Exception as err:
            print(err)
            return False
        
    
    def set_client_name(self,name:str)->bool:
        """Set a name or alias for the current client connection

        Args:
            name (str, optional): Alias or label/name. Defaults to ""(None).

        Returns:
            bool: True if operation was successful or no name. Flase if not-
        """
        if not isinstance(name,str):
            print("Redis set_client_name operation : name must be a string")
        return self.__r.client_setname(name=name)

    
    def echo(self,message:str):
        """Send an echo message/command to the redis server

        Args:
            message (str): message/command 
        """
        if not isinstance(message,str):
            print("Redis echo operation : message must be a string (str)")
        self.__r.echo(message)
      
    
  