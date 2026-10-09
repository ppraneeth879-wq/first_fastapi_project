from fastapi import FastAPI
app = FastAPI()

BOOKS = [
         {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
@app.get("/api-endpoint")
async def first_api():
    return  BOOKS
##note- order matter in path parameter: 
@app.get("/books/mybooks")
async def read_all_books():
    return {'book_title': 'My Favorite Book'}
@app.get("/books/{dynamic_param}")
async def second_api(dynamic_param):
    return {'dynamic_param':dynamic_param}
@app.get('/books2/{book_title}')
async def third_api(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book
    




