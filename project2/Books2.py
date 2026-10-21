from fastapi import FastAPI,Body
from pydantic import BaseModel,Field

app = FastAPI()

class BookRequest(BaseModel):
    id: int 
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description : str = Field(min_length=3,max_length=10)
    rating: int = Field(gt=0,lt=10)
    
'''Book is a regular Python class, not a Pydantic model. Field validation only works on classes that inherit from BaseModel.'''
class Book: 
    id: int 
    title: str 
    author: str 
    description : str
    rating: int 
    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
#BOOKS here is a list of objects!! not primitive     
BOOKS = [
   
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1)
    
    
]

@app.get("/books")
async def read_all_books():
    return BOOKS 

@app.post("/books")
async def create_book(book_request: BookRequest):
    #
    new_book = Book(**book_request.dict())
    BOOKS.append(book_request)
    
@app.post("/books232")
# Expects raw payload: {"title": "HP1", "author": "..."}
# With embed=True, it expects: {"book_request": {"title": "HP1", "author": "..."}}
async def create_book(book_request: BookRequest = Body(..., embed=True)):
    return book_request


