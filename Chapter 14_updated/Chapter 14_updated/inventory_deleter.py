import sqlite3

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

repeat = 'y'

def delete_row(item_name):
    cur.execute('''SELECT ItemName From Inventory WHERE ItemName = ?''', (item_name,))
    result = cur.fetchone()
    if (result != None):
        cur.execute('''DELETE FROM Inventory WHERE ItemName = ?''', (item_name,))
        conn.commit()
        print('The product was deleted.')
    else:
        print(f'Item " {item_name} " not found.')

while (repeat == 'y'):
    item_name = (input('Item Name: '))
    delete_row(item_name)
    repeat = input('Do you want to delete another row? ')
    
conn.close()