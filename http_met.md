# 1. Управление справочником клиентов.
> Для управления справочником мы будем использовать "POST", "PUT", "PATCH" и "DELETE" запросы.
### 1.1 POST запрос
POST запрос нужен для создания новой строки в таблице.

>POST /client

Тело запроса:
```json
{
  "id": 314,
  "name": "Fedor Golovlev"
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "The line was created successfully"
}
```
### 1.2 PUT запрос.
PUT запрос нужен для полной замены строки в таблице.
>PUT /client/314

Тело запроса:
```json
{
  "id": 314,
  "name": "David Beliackii"
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "The string was successfully replaced"
}
```
### 1.3 PATCH запрос.
PATCH запрос нужен для частичной замены строки в таблице.
>PUT /client/314

Тело запроса:
```json
{
  "id": 314,
  "name": "Fedor Golovlev"
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Part of the string has been successfully replaced"
}
```
### 1.4 DELETE запрос.
DELETE запрос нужен для удаления строки в таблице.
>DELETE /client/314

Тело запроса:
```json
{
  "id": 314
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Successfully deleted"
}
```
***
# 2. Управление справочником туров
> Для управления справочником мы будем использовать "POST", "PUT", "PATCH" и "DELETE" запросы.

### 2.1 POST запрос
POST запрос нужен для создания новой строки в таблице.

>POST /tur

Тело запроса:
```json
{
  "id": 10,
  "price": 145000,
  "transportation_id": 2,
  "hotel_id": 5,
  "days": 10,
  "Departure_date": "2022-08-28",
  "Arrival_date": "2022-09-06"
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Tour created"
}
```
### 2.2 PUT запрос.
PUT запрос нужен для полной замены строки в таблице.
>PUT /tur/10

Тело запроса:
```json
{
  "id": 10,
  "price": 155000,
  "transportation_id": 1,
  "hotel_id": 4,
  "days": 10,
  "Departure_date": "2022-08-28",
  "Arrival_date": "2022-09-06"
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Tour edited"
}
```
### 2.3 PATCH запрос.
PATCH запрос нужен для частичной замены строки в таблице.
>PUT /tur/10

Тело запроса:
```json
{
  "id": 10,
  "price": 145000,
  "transportation_id": 2,
  "hotel_id": 5
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Tour edited"
}
```
### 2.4 DELETE запрос.
DELETE запрос нужен для удаления строки в таблице.
>DELETE /tur/10

Тело запроса:
```json
{
  "id": 10
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Tour deleted"
}
```
***
# 3. Управление справочником отелей
> Для управления справочником мы будем использовать "POST", "PUT", "PATCH" и "DELETE" запросы.

### 3.1 POST запрос
POST запрос нужен для создания новой строки в таблице.

>POST /hotel

Тело запроса:
```json
{
  "id": 10,
  "city_id": 2,
  "stars": 4,
  "price": 4000,
  "name": ""
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Hotel created"
}
```
### 3.2 PUT запрос.
PUT запрос нужен для полной замены строки в таблице.
>PUT /hotel

Тело запроса:
```json
{
  "id": 10,
  "price": 155000,
  "transportation_id": 1,
  "hotel_id": 4,
  "days": 10,
  "Departure_date": "2022-08-28",
  "Arrival_date": "2022-09-06"
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Hotel edited"
}
```
### 3.3 PATCH запрос.
PATCH запрос нужен для частичной замены строки в таблице.
>PUT /hotel

Тело запроса:
```json
{
  "id": 10,
  "price": 145000,
  "transportation_id": 2,
  "hotel_id": 5
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Tour edited"
}
```
### 3.4 DELETE запрос.
DELETE запрос нужен для удаления строки в таблице.
>DELETE /tur/10

Тело запроса:
```json
{
  "id": 10
}
```
Ответ:
```json
{
  "status": "True",
  "Answer": "Tour deleted"
}
```
***
### 5. Продажа тура происходит через метод добавления его в таблицу проданных.