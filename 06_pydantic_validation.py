from pydantic import BaseModel, field_validator, model_validator

class CreateUser(BaseModel):
    email : str
    password : str
    confirm_password : str

    @field_validator('email')    
    def validate_email(cls, value):
        if "admin" in value:
            raise ValueError('This email with <ADMIN> is not allowed')
        return value

    @model_validator(mode="before")
    def validate_password(cls, values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise  ValueError("the password dont match")
        return values


CreateUser(email="admi@tyson.com",password="12345", confirm_password="123456")