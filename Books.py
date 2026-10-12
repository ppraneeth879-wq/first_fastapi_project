from fastapi import FastAPI,Body
app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},
    {'title':'Title Seven','author':'Author Three','category':'biology'}
]

@app.get("/api-endpoint")
async def first_api_read_all_book():
    return  BOOKS
##note- order matter in path parameter: 
@app.get("/books/mybooks")
async def read_favourite_book():
    return {'book_title': 'My Favorite Book'}

#path parameters
@app.get("/books/{dynamic_param}")
async def second_api(dynamic_param):
    return {'dynamic_param':dynamic_param}
@app.get('/books2/{book_title}')
async def third_api_readbook(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book
#query parameter
@app.get('/books3/')
async def fourth_api_read_by_category(category: str): 
    
    for book in BOOKS: 
        if book.get('category').casefold()==category.casefold():
            return book
    return 

#path + query parameter combined 
@app.get("/books5/{books_author}/")
async def read_author_category_by_query(books_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == books_author.casefold() and \
             book.get('category').casefold() == category.casefold():
                
            books_to_return.append(book)
    return books_to_return
# post request
#note get request cannot have a body!!!
@app.post('/books6/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
#put is update request
@app.put('/books7/update')
async def update_book(new_book = Body()): 
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == new_book.get('title').casefold():
            BOOKS[i] = new_book
    return 

#delte request 
@app.delete("/books8/{delete_title}")
async def delete_book(delete_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==delete_title.casefold():
            BOOKS.pop(i)
            break
    return 

##Assignment question to create endpoint fetching all books from an author
@app.get('/books9/{author_get}')
async def author_get(author_get: str):
    author_list = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold()==author_get.casefold():
            author_list.append(BOOKS[i])
            
    return author_list

## THe end of project 
