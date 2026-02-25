import json
old_book= [
  {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": True},
  {"title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": True}
]
with open("inventory.json","w")as file:
   json.dump(old_book,file,indent=2)


with open("inventory.json","r")as file:
  books=json.load(file)
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
books.append(new_book)

with open("inventory.json","w") as file:
  json.dump(books,file,indent=4)


with open("inventory.json","r")as file:
  bookstor=json.load(file)
for book  in bookstor:
  print(f"Title:{book.get('title')}|"
        f"author:{book.get('author')}|"
        f"price:{book.get('price','n/a')}|"
        f"in stock:{book.get('in_stock','n/a')}"
        )
