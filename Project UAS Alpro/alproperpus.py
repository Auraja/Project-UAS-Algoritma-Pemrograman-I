import csv
import os

os.system("cls")

def load():
    books = []
    global list_books
    list_books = []
    books_sorted = []
    books_title = []
    with open("books.csv") as f:
        books_csv = csv.DictReader(f)
        for i in books_csv:
            books.append(dict(i)) 

    for i in range(len(books)):
        books_title.append(str(books[i]["Title"]))

    for i in range(len(books_title)):
        books_sorted.append(str(min(books_title)))
        books_title[books_title.index(min(books_title))] = books_title[-1]
        books_title.pop()

    for i in books_sorted:
        for j in range(len(books)):
            if books[j]["Title"] == i:
                list_books.append(books[j])

def listBuku():
    global list_books
    for i in range(len(list_books)):
        title = list_books[i]["Title"]
        author = list_books[i]["Author"]
        publisher = list_books[i]["Publisher"]
        year = list_books[i]["Year"]

        print(
            f"{i+1}).\tTitle     : {title}\n",
            f"\tAuthor    : {author}\n",
            f"\tPublisher : {publisher}\n",
            f"\tYear      : {year}\n"
        )

def cariBuku(x: str):
    
    global list_books
    possible = []

    for i in range(len(list_books)):
        if x.lower() in list_books[i]["Title"].lower():
            possible.append(list_books[i])
        
    if len(possible) == 0:
        print("\nMaaf, buku itu tidak tersedia\n")
        return
    
    for i in range(len(possible)):
        title = possible[i]["Title"]
        author =possible[i]["Author"]
        publisher = possible[i]["Publisher"]
        year = possible[i]["Year"]

        print(
            f"{i+1}).\tTitle     : {title}\n",
            f"\tAuthor    : {author}\n",
            f"\tPublisher : {publisher}\n",
            f"\tYear      : {year}\n"
        )

def pinjamBuku(x):

    global list_books, borrowed

    for i in range(len(list_books)):
        if x.lower() in list_books[i]["Title"].lower():
            for j in range(len(borrowed)):
                if x.lower() not in borrowed[j].lower():
                    continue
                else:
                    print("\nMaaf, buku itu sudah dipinjam.\n")
                    break
            else:
                title = list_books[i]["Title"]
                author = list_books[i]["Author"]
                publisher = list_books[i]["Publisher"]
                year = list_books[i]["Year"]

                print(
                    "\nTerima kasih sudah meminjam buku!\n"
                    "\nBook Information:\n"
                    f"\tTitle     : {title}\n",
                    f"\tAuthor    : {author}\n",
                    f"\tPublisher : {publisher}\n",
                    f"\tYear      : {year}\n"
                )

                borrowed.append(title)
            break
        else:
            print("Mencari...\n")
            

def kembalikanBuku(x):

    global list_books, borrowed

    for i in range(len(list_books)):
        if x.lower() in list_books[i]["Title"].lower():
            for j in range(len(borrowed)):
                if x.lower() not in borrowed[j].lower():
                    continue
                else:
                    title = list_books[i]["Title"]
                    author = list_books[i]["Author"]
                    publisher = list_books[i]["Publisher"]
                    year = list_books[i]["Year"]
                    
                    print(
                        "\nTerima kasih sudah mengembalikan buku!\n"
                        "\nBook Information:\n"
                        f"\tTitle     : {title}\n",
                        f"\tAuthor    : {author}\n",
                        f"\tPublisher : {publisher}\n",
                        f"\tYear      : {year}\n"
                    )

                    borrowed.remove(title)
                break
            else:
                print("\nBuku itu tidak anda pinjam!\n")
            break      
        else:
            print("Mencari...\n")
            

        

if __name__ == "__main__":

    list_books = []
    borrowed = []
    run = True
    load()

    while run:
        print(
            "=" * 40 + "\n",
            "= Selamat Datang Di Perpustakaan Kita! =\n",
            "=" * 40 + "\n",
            "[1] Melihat list buku yang tersedia\n"
            "[2] Mencari sebuah buku\n"
            "[3] Meminjam buku\n"
            "[4] Mengembalikan buku\n"
            "[5] Exit."
            , sep= ""
        )

        pilihan = input("Apa yang ingim anda lakukan? : ")

        if pilihan == "1":
            listBuku()
            inListBooks = True
            while inListBooks:
                pilihan = input(("Kembali ke menu utama? ( Y / N [keluar dari perpustakaan] ) : "))
                if pilihan not in list("YynN"):
                    continue
                else:
                    os.system("cls")
                    if pilihan in list("Yy"):
                        inListBooks = False
                        continue
                    else:
                        print("\nTerima kasih sudah berkunjung!\n")
                        exit()
                                
        elif pilihan == "2":
            cariBuku(input("\nMasukkan judul buku : "))
            inSearch = True
            while inSearch:
                pilihan = input(("Kembali ke menu utama? ( Y / N [keluar dari perpustakaan] ) : "))
                if pilihan not in list("YynN"):
                    continue
                else:
                    os.system("cls")
                    if pilihan in list("Yy"):
                        inSearch = False
                        continue
                    else:
                        print("\nTerima kasih sudah berkunjung!\n")
                        exit()

        elif pilihan == "3":
            pinjamBuku(input("\nBuku apa yang ingin dipinjam? : "))
            isBorrow = True
            while isBorrow:
                pilihan = input(("Kembali ke menu utama? ( Y / N [keluar dari perpustakaan] ) : "))
                if pilihan not in list("YynN"):
                    continue
                else:
                    os.system("cls")
                    if pilihan in list("Yy"):
                        isBorrow = False
                        continue
                    else:
                        print("\nTerima kasih sudah berkunjung!\n")
                        exit()

        elif pilihan == "4":
            kembalikanBuku(input("\nMasukkan judul buku yang ingin dikembalikan : "))
            isReturn = True
            while isReturn:
                pilihan = input(("Kembali ke menu utama? ( Y / N [keluar dari perpustakaan] ) : "))
                if pilihan not in list("YynN"):
                    continue
                else:
                    os.system("cls")
                    if pilihan in list("Yy"):
                        isReturn = False
                        continue
                    else:
                        print("\nTerima kasih sudah berkunjung!\n")
                        exit()

        elif pilihan == "5":
            os.system("cls")
            print("\nTerima kasih sudah berkunjung!\n")
            exit()
