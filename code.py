import sys
if sys.version_info < (3, 0):
    from thread import *
else:
    from threading import Thread
import time

data_dict = dict()

def raise_exception(message):
    """
    Used to raise exception
    :param message:                 (str)       --  Message and raises its exception
    :return: None
    """
    raise Exception(message)

def is_not_expired(time_to_compare, key):
    """
    Used to check if time has expired for that
    :param time_to_compare:         (time)      --  end time value for that key
    :param key:                     (str)       --  name of key to raise exception
    :return: bool:
                True: If time not expired
    """
    if time_to_compare != 0:
        if time.time() < time_to_compare:
            return True
        else:
            raise_exception("Error: Time-to-live of %s expired" % key)
    return True

def create(key,value,timeout=0):
    """
    Used to create a key value file system for that key name
    :param key:                     (str)       --  name of key
    :param value:                   (any)       --  value of that file
    :param timeout:                 (int)       --  time to live of this file
    :return: None
    """
    if key in data_dict.keys():
        raise_exception("Error: Key exists")
    else:
        if key.isalpha():
            if len(data_dict) < (1024*1024*1024) and value <= (16*1024*1024):
                if timeout == 0:
                    value_list = [value, timeout]
                else:
                    value_list = [value, time.time() + timeout]
                if len(key) <= 32: # key name constraints
                    data_dict[key] = value_list
            else:
                raise_exception("Error: Memory limit exceeded!")
        else:
            raise_exception("Error: Invalid key_name!")

def read(key):
    """
    Used to return value associated with the key
    :param key:                     (str)       --  name of key
    :return: value of that key in json format
    """
    if key not in data_dict.keys():
        raise_exception("Error: Key Not present!")
    else:
        value_list = data_dict[key]
        if is_not_expired(value_list[1], key):
            ret_value = str(key) + ":" + str(value_list[0])
            return ret_value

def deleting_key(key):
    """
    Used to delete the key
    :param key:                     (str)       --  name of key
    :return: None
    """
    try:
        del data_dict[key]
        print("Key deleted successfully..")
    except Exception as e:
        raise_exception(str(e))

def delete(key):
    """
    Used to delete the key
    :param key:                     (str)       --  name of key
    :return: None
    """
    if key not in data_dict.keys():
        raise_exception("Error: Key Not present!")
    else:
        value_list = data_dict[key]
        if is_not_expired(value_list[1], key):
            deleting_key(key)
