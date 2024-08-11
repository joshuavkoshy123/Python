import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('inventory.db')
    
    # Get a cursor.
    cur = conn.cursor()
    
    # Get the lowest price.
    cur.execute('SELECT MIN(Price) FROM Inventory')
    lowest = cur.fetchone()[0]
    cur.execute('SELECT ItemName FROM Inventory WHERE Price == ?', (lowest,))
    lowest_name = cur.fetchone()

    # Get the highest price.
    cur.execute('SELECT MAX(Price) FROM Inventory')
    highest = cur.fetchone()[0]
    cur.execute('SELECT ItemName FROM Inventory WHERE Price == ?', (highest,))
    highest_name = cur.fetchone()

    # Get the average price.
    cur.execute('SELECT AVG(Price) FROM Inventory')
    average = cur.fetchone()[0]
    cur.execute('SELECT ItemName FROM Inventory WHERE Price == ?', (average,))
    average_name = cur.fetchone()

    # Display the results.
    print('Lowest Price: ')
    print(lowest_name[0], f"           ${lowest:.2f}")
    print('Highest Price: ')
    print(highest_name[0], f"           ${highest:.2f}")
    print(f'Average Price:            ${average:.2f}')
    
    # Close the database connection.
    conn.close()

# Execute the main function.
if __name__ == '__main__':
    main()