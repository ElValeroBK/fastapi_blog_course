class Pydantic:
    def is_valid(self,text):
        if "admin" in text:
            return False
        return True

class Startlette:
    def is_valid(self,text):
        return True
    
class Fastapi(Pydantic,Startlette):
    pass

f= Fastapi()

print(Fastapi.__mro__)
print(f.is_valid("admin is a good job"))
