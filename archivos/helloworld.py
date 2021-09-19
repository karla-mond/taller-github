from datetime import date

def main():
    today = date.today()

    print("Bienvenidos al taller de Github, hoy es el ", today.strftime("%d/%m/%Y"))

if __name__ == "__main__":
    main()