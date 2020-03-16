class book:

        def accept(self):
            self.name =str(input("Enter name of the book: "))
            self.author =str(input("Entar author of the book: "))
            self.price =float(input("Enter the price of the book: "))
            self.n_copies =int(input("Enter the no of copies of the book to be purchased: "))

        def total_price(self):
            t = self.price*self.n_copies
            print("Total pricr : ",t)

        def details(self):
            print("Purchase details",center(70,"-"))
            print("Name of book: ",self.name)
            print("Author of book : ",self.author)
            print("Pricr of the book :",self.price)
            print("Number of copies : ",self.n_copies)

c = book()
c.accept()
c.details()
c.total_price()
