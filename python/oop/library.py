class Library:
    def __init__(self,books : list[str]):
        self.books = books
    
    def add_book(self,book_name:str):

        self.books.append(book_name)
        
        print(f"book '{book_name}' added")
    
    def remove_book(self,book_name : str) :
        if book_name not in self.books:
           print(f"No book found with name:{book_name}")
        else :
            self.books.remove(book_name)
            print(f"book '{book_name}' has been removed")        

    def display(self):
        for book in self.books:
            print(book)
    
    
    # lib = Library(["Python","Java"])


        
    
        