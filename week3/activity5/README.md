# Database structure

## Currencies table

Includes names and codes of all currencies.

id: auto increment
name: full name
code: 3 letters code

## Rates table

Includes exchange rates from one currency to another.

id: auto increment
base: base currency id
quote: quote currency id'
rate: exchange rate

## Customers

Includes data of all the customers.

id: auto increment
first: first name
last: last name
email: email

## Balances

Includes data about balance left of every customer in every currency.

id: auto increment
customer: id of customer
currency: id of currency
balance: balance of corresponding currency for corresponding customer


## Transactions

Includes data of all currency exchange transactions including exchanged currencies and amount of eeach currency.

id: auto increment
created: timestamp when transaction occured
base_curr: id of base currency
quote_curr: id of quote currency
base_sum: amount of base currency
quote_sum: amount of quote currency
