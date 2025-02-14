from itertools import cycle
from base64 import b64encode


class xor:
    def __init__(self, message:str, key:str):
        self.message = message
        self.key = key
        

    def __xor(self) -> bytes:
        encrypted_message = ""

        cycle_key = cycle(self.key)
        i = 0
        len_message = len(self.message)

        for char in self.message:
            if i == len_message:
                break
            else:
                encrypted_message += chr(ord(char) ^ ord(next(cycle_key)))
                i += 1
        return bytes(encrypted_message, "utf-8")

    def as_string(self):        
        return(self.__xor().decode("utf-8"))
    
    def as_b64_encoded(self):
        return(b64encode(self.__xor()).decode("utf-8"))
        

#Example usage
# my_thing = xor(message="This is my message", key="1234")

# print(my_thing.as_string())
# print(my_thing.as_b64_encoded())