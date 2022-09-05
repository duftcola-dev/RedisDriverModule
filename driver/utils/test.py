from redis import Redis 

class Test:

    def __init__(self,r:Redis) -> None:
        self.__r=r


    def close(self):
        """Close connection and kills the client object
        """
        self.__r.quit()
        self.__r=None

    
    def check_memory(self):
        """The MEMORY DOCTOR command reports about different memory-related 
        issues that the Redis server experiences, and advises about possible 
        remedies.

        Returns:
            _type_: _description_
        """
        return self.__r.memory_doctor()

    
    def check_memory_stats(self)->list:
        """The MEMORY STATS command returns an Array reply 
        about the memory usage of the server.
        The information about memory usage is provided as metrics and their respective values. The following metrics are reported:

        - peak.allocated: Peak memory consumed by Redis in bytes (see INFO's used_memory_peak)
        - total.allocated: Total number of bytes allocated by Redis using its allocator (see INFO's used_memory)
        - startup.allocated: Initial amount of memory consumed by Redis at startup in bytes (see INFO's used_memory_startup)
        - replication.backlog: Size in bytes of the replication backlog (see INFO's repl_backlog_active)
        - clients.slaves: The total size in bytes of all replicas overheads (output and query buffers, connection contexts)
        - clients.normal: The total size in bytes of all clients overheads (output and query buffers, connection contexts)
        - cluster.links: Memory usage by cluster links (Added in Redis 7.0, see INFO's mem_cluster_links).
        - aof.buffer: The summed size in bytes of AOF related buffers.
        - lua.caches: the summed size in bytes of the overheads of the Lua scripts' caches
        - dbXXX: For each of the server's databases, the overheads of the main and expiry dictionaries (overhead.hashtable.main and overhead.hashtable.expires, respectively) are reported in bytes
        - overhead.total: The sum of all overheads, i.e. startup.allocated, replication.backlog, clients.slaves, clients.normal, aof.buffer and those of the internal data structures that are used in managing the Redis keyspace (see INFO's used_memory_overhead)
        - keys.count: The total number of keys stored across all databases in the server
        - keys.bytes-per-key: The ratio between net memory usage (total.allocated minus startup.allocated) and keys.count
        - dataset.bytes: The size in bytes of the dataset, i.e. overhead.total subtracted from total.allocated (see INFO's used_memory_dataset)
        - dataset.percentage: The percentage of dataset.bytes out of the net memory usage
        - peak.percentage: The percentage of peak.allocated out of total.allocated
        - fragmentation: See INFO's mem_fragmentation_ratio

        """
        return self.__r.memory_stats()


    def memory_usage(self,key:str)->int:
        """Returns the number of bytes that a 
        key and its value require to be stored in RAM.

        Args:
            key (str): key name

        Returns:
            int: number of bytes the content of a key occupies in RAM
        """
        if not isinstance(key,str):
            print("Redis memory_usage : Argument passed must be a string")
            return 0
        return self.__r.memory_usage(key)

    
    def database_size(self)->int:
        """Return the number of keys in the currently-selected database.

        Returns:
            int: number of keys
        """
        return self.__r.dbsize()


    def get_actions_registry(self)->list:
        """streams back every command processed by the Redis server. 
        It can help in understanding what is happening to the database. 
        This command can both be used via redis-cli and via telnet.

        Returns:
            list: List of actons perfomed in the server.
        """
        return self.__r.monitor()