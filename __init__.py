from booklover.booklover import BookLover
book_lover = BookLover('Han Solo', 'hsolo@millenn.com', 'scifi')
book_lover.add_book('Star Wars: no hope', 5)
print(book_lover.num_books_read())
