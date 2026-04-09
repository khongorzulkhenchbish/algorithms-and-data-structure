# implement a bookshelf with books. each book is indexed, but only one book has bookmark.
# you should be able to add | remove | move books in the bookshelf
# 1. addBook(toIndex, list): insert given amount of books into the bookshelf
# 2. remove(fromIndex, toIndex): remove books between given indexes, inclusive toIndex
# 3. moveBook(fromIndex, toIndex, size): move size amount of books between given indexes


# The "Bookmark" is the secret to this problem.
# It makes this a State Management problem rather than just a Data Structure problem.


class Bookshelf:
    def __init__(self):
        self.books = []
        self.bookmark_idx = -1  # Track the actual index of the book with the bookmark

    def addBook(self, toIndex, new_books):
        # Python slicing: self.books[toIndex:toIndex] = new_books is even faster!
        self.books[toIndex:toIndex] = new_books
        
        # Logic: If we insert books BEFORE the bookmark, the bookmark shifts right
        if self.bookmark_idx >= toIndex:
            self.bookmark_idx += len(new_books)

    def removeBooks(self, fromIndex, toIndex):
        num_removed = toIndex - fromIndex
        # Logic: Was the bookmark inside the removed range?
        if fromIndex <= self.bookmark_idx < toIndex:
            self.bookmark_idx = -1 # Bookmark is gone
        elif self.bookmark_idx >= toIndex:
            self.bookmark_idx -= num_removed
            
        self.books[fromIndex:toIndex] = []

    def moveBook(self, fromIndex, toIndex, size):
        # 1. Extract the segment
        segment = self.books[fromIndex : fromIndex + size]
        # 2. Delete the segment
        self.books[fromIndex : fromIndex + size] = []
        # 3. Insert at new location (adjusting for the deletion)
        self.books[toIndex:toIndex] = segment
        # 4. (You would also need logic here to update the bookmark_idx)