from connect_db import Database
def table():
    menu_table = f"""
        CREATE TABLE menu(
            menu_id SERIAL PRIMARY KEY,
            mane VARCHAR(30),
            create_data TIMESTAMP DEFAULT now())
    """

    category = f"""
        CREATE TABLE category(
            category_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_data TIMESTAMP DEFAULT now())
        """

    data = {
        "menu_table": menu_table,
        "category": category
    }

    for i in data:
        print(f"{i} - {Databese.connect(data[i], "create")}")

if __name__ =="__main__":
    table()
