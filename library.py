import pandas as pd
books = [
        {
        'Title': "Atomic habits",
        'Author': "James Clear", 
        'Genre': "Self-help book",
        'Year': 2018,
        'Quantity': 50},
        
        
        {
        'Title': "The Hobbit",
        'Author': "J.R.R. Tolkien",
        'Genre': "Fantasy",
        'Year': 1937,
        'Quantity': 50
        
    },

        {
        'Title': "The Great Gatsby",
        'Author': "Scott Fitzgerald",
        'Genre': "Classic",
        'Year': 1925,
        'Quantity': 9

# "The Great Gatsby", "Scott Fitzgerald", 'Genre': "Classic", 1925, 9

    },

       { 'Title': "The Alchemist",
        'Author': "Paulo Coelho",
        'Genre': "Philosophy",
        'Year': 1988,
        'Quantity': 15

    }

]





class library:
    def __init__(self):
        self.books = books.copy()


    def add_book(self, title, author, genre, year, quantity):
        for book in self.books:
            if book['Title'].lower() == title.lower():
                book['Quantity'] += quantity
                return
            
        self.books.append({"Title": title, "Author": author, "Genre": genre, "Year": year, "Quantity": quantity})

    def remove_book(self, title, author, genre, year, quantity):
      
        for book in self.books:
            if book['Title'].lower() == title.lower():
                if book['Quantity'] > quantity:
                    book['Quantity'] -= quantity
                elif book['Quantity'] == quantity:
                    self.books.remove(book)

                else:
                    print("There are not enough copies to delele!")
                return
       
        print("You can not remove not existed book from the library!")

        


    def info_book(self):
        if not self.books:
            print("No books in the library.")
            return
        data = pd.DataFrame(books)
        print(data)



        

lib1 = library()

# lib1.add_book("Mans Search for Meaning", "Viktor E. Frankl", "Psychology", 1946, 15)
# lib1.remove_book("The Great Gatsby", "Scott Fitzgerald", "Genre" "Classic", 1925, 1)
# lib1.add_book("The Great Gatsby", "Scott Fitzgerald", 'Genre' "Classic", 1925, 99)
# lib1.remove_book("To Kill a Mockingbird", "Harper Lee", "Classic", 1960, 5)
# lib1.remove_book("The Great Gatsby", "Scott Fitzgerald", "Genre" "Classic", 1925, 10)
# lib1.remove_book("The Great Gatsby", "Scott Fitzgerald", "Genre" "Classic", 1925, 9)


bookss = pd.DataFrame(books)

lib1.info_book()
