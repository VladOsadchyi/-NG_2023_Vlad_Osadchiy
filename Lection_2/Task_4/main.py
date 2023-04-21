yourbooks=[]
while True:
    yourchoice=int(input("Enter your choice: "))
    match yourchoice:
        case 1:
            title=input("Enter your title: ")
            author=input("Enter your author: ")
            pages=input("Enter your pages: ")
            genre=input("Enter your genre: ")
            binding=input("Enter your binding: ")
            book={
                "title":title,
                "author":author,
                "pages":pages,
                "genre":genre,
                "binding":binding
            }
            yourbooks.append(book)
            print(yourbooks)
        case 2:
            title=input("Enter the name of book which you want to delete: ")
            for book in yourbooks:
                if book["title"]==title:
                    yourbooks.remove(book)
            print(yourbooks)
            break
            