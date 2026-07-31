from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str


class Customer(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True