from pydantic import BaseModel, ConfigDict , field_validator

class User(BaseModel):
    id: int = 123
    name: str = 'Jane Doe'

    model_config = ConfigDict(str_max_length=20 , int_max_length=1)   # it is used because it we give another name that we want but if its string lengthh is greater then we asked then the code will through validation error.

# FOR THIS CODE IF WE WANT THAT WE HAVE TO CONFIG THE ID LENGTH ALSO JUST LIKE STR_MAX_LENGTH WE CAN CREATE THE CUSTUM VALIDATOR CLASS
   
    @field_validator("id")                        #here this "id" string refers to the field name in your model that this validator is meant to validate.
    def field_id_length(cls , v: int ) -> int:     #here this arrow and after arrow int signifies that when we make set the type of integer 
        if len(str(v)) > 5:
            raise ValueError('id cannot be more than 5 digits long')
        return v


# field validator is the decorator in which we have passed the id do it works with id 


user = User(id = "123")
print(user)



assert user.name == 'Jane Doe'  
assert user.id == 123  
assert isinstance(user.id, int)

assert user.model_dump() == {'id': 123, 'name': 'Jane Doe'}

# we can short this code by using 
# from pydantic import BaseModel, Field

# class User(BaseModel):
#     id: int = Field(default=123, le=99999)  # max 5-digit value
#     name: str = Field(default='Jane Doe', max_length=20)
# this helps us defining the defauld and default lent using field we dont need to use configdict
