import sys
yourbooks=[]
while True:
    print(" 1-add book;\n 2-delete the book;\n 3-find book and change parameters(if you want)\n 4-finish this program")
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
            print(yourbooks, "\n")
        case 2:
            title=input("Enter the name of book which you want to delete: ")
            for book in yourbooks:
                if book["title"]==title:
                    yourbooks.remove(book)
            print(yourbooks)
            break
        case 3:
            findbook=input("Enter the name of book which you want to find: ")
            for book in yourbooks:
                if book["title"]==findbook:
                    print(book)
                    print("Do you want to change something in it?Y/N")
                    yourYN=input("")
                    if yourYN=="Y":
                        print(" 1-title;\n 2-author;\n 3-pages;\n 4-genre;\n 5-binding;")
                        changedelofbook=int(input("Enter the parameter:"))
                        match changedelofbook:
                            case 1:
                                newtitle=input("Enter your new title: ")
                                book["title"]=newtitle
                                print(book)
                            case 2:
                                newauthor=input("Enter your new author: ")
                                book["author"]=newauthor
                                print(book)
                            case 3:
                                newpages=input("Enter your new pages: ")
                                book["pages"]=newpages
                                print(book)
                            case 4:
                                newgenre=input("Enter your new genre: ")
                                book["genre"]=newgenre
                                print(book)
                            case 5:
                                newbinding=input("Enter your new binding: ")
                                book["binding"]=newbinding
                                print(book)
                    else:
                        print("Ok")
                else:
                    print("There is no such book")            
        case 4:
            sys.exit()
            
                