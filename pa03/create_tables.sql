CREATE TABLE transactions {
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_num INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    category VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
    description VARCHAR(100) NOT NULL
}