#  Agent Referral Backend

![](https://github.com/khan-asfi-reza/real-estate-referral-app/workflows/Development/badge.svg)
![](https://github.com/khan-asfi-reza/real-estate-referral-app/workflows/Production/badge.svg)
### This project is being used in production by a different company

## Client Side 👩‍💻

### Frameworks
1. Svelte
2. Bootstrap
3. AOS

### How to run

1. Change directory to the client
```shell
cd client
```

2. Install packages
```shell
npm i 
```

3. Run Server
```shell
npm run dev
```


## Server Side 🖥️

Reza Corporation Agent Referral Backend, Basic referral system backend.

Recruiters will create account and use their unique referral link to recruit other users, 
those Recruits will complete a transaction and based on that transaction, the recruiter will get commission

## Used Stacks

### Framework

1. Django
2. Django Rest Framework

### Database
1. Postgresql

## Models

1. User
2. Recruiter
3. Recruit
4. Referral
5. Transaction
6. Commission

### User
`User` model contains Account information, 
1. `email`: Email [Username]
2. `first_name`: String
3. `last_name`: String
4. `role`: Int [Recruiter | Recruit | Admin]
5. `created_at`: Time Stamp
6. `password`: Hash
7. `city`: String
8. `state`: String
9. `zip`: String
10. `address`: String
11. `phone_number`: String

### Recruiter
`Recruiter` model contains recruiter information and referral code
1. `user`: User Model Instance
2. `ref_code`: Int
3. `time_stamp` Date Time

### Recruit
`Recruit` model contains Recruit Information
1. `nmls_id`: String
2. `dre_license`: String
3. `cba_license`: Boolean
4. `association`: String

### Referral
`Referral` Contains Relationship between Recruit and Recruiter
1. `Recruiter`: User Model Instance
2. `Recruit`: User Model Instance

### Transaction
`Transaction` can be done by a recruit
1. `Recruit`: User Model Instance
2. `Amount`: Float
3. `time_stamp` Date Time

### Commission

1. `Recruit`: User Model Instance
2. `Recruiter`: User Model Instance
3. `commission`: Float
4. `time_stamp`: Date Time
5. `Transaction`: Transaction ID

### Commission Payment

1. `Recruit`: User Model Instance
2. `commission`: Commission Model Instance []
3. `amount`: Float
4. `time_stamp`: Date Time


Transaction Creation Adds A New Commission 

## Installation

1. Clone the repo
```shell
git clone https://github.com/khan-asfi-reza/real-estate-referral-app
```

2. Install packages
```shell
pip install -r requirements.txt
```

3. Test 
```shell
python manage.py test
```

4. Run
```shell
python manage.py runserver
```


## API Docs

#### 1. Login

`api/auth/login`

Method: `POST`

Request Body:
```json5
{
    email: "example@email.com",
    password: "Password"
}
```

Response: 
```json5
{ token: "String", 
  user: {
    email: "example@test.com", 
    role: 1
  }
}
```

#### 2. Change Password

`api/auth/change-password/`

Method: `POST`

Request Body:
```json5
{
    old_password: "Old Password",
    new_password: "New Password"
}
```


Response: `{token: String}`

#### 3. User Update | Update User Information


`api/auth/user/update/`

Method: `PATCH`

Partial Update

Request Body:
```json5
{
    first_name: "String",
    last_name: "String",
    phone_number: "String",
    address: "String",
    city: "String",
    state: "String",
    zip: "String",
}
```


Response: `Same as body`

#### 4. Check Email Available


`user/email/check`

Method: `POST`

Request Body:

```json5
{
     email: "Email"
}
```


Response: `{msg: 0 / 1}`


###### 0 > Email Is not Available
###### 1 > Email is available


#### 5. Get Ref Code

`/api/core/ref-code`

Method: `POST`

Request Body

```json
{
  "ref_code": "123455"
}    
```

Response
```json5
{
  email: "example@email.com",
  full_name: "Full Name"
}
```

#### 6. Recruiter Create
`/api/core/recruiter/create`

Method: `POST`

Request Body
```json5
{
   user: {
    first_name: "String",
    last_name: "String",
    phone_number: "String",
    address: "String",
    city: "String",
    state: "String",
    zip: "String",
    password: "String" 
   }
}
```
Response 
```json5
{
  token: "String",
  data: {
    "key": "value"
  }
}
```
`Data Same as Request Body`

#### 7. Recruit Create and List

`/api/core/recruit/`

METHOD: `POST`

Request Body
```json5
{
     user:{
        first_name: "String",
        last_name: "String",
        phone_number: "String",
        address: "String",
        city: "String",
        state: "String",
        zip: "String",
        password: "String" 
     },
    phone_number: "String",
    nmls_number: "String",
    dre_license: "String",
    ref_code: "String"
}

```
Response 
```json5
{
  token: "String",
  data: {
    "key": "value"
  }
}
```
`Data Same as Request Body`

#### 7. Referral Data

`api/core/referral`

METHOD: `GET`

Headers : `{Authorization: "Token <YOUR TOKEN>"}`

Query Params: `?page=<page_number>`

Response Body
```json5
{
  page: 1,
  next: "Link",
  prev: "Link",
  results: [
    {
       id: 1,
       recruiter: 1,
       recruit: {
         email: "Email",
         first_name: "First Name",
         last_name: "Last Name"
       },
       time_stamp: "2020-02-02 12:19:34.45666"
    }
  ]
}
```


#### 8. Recruiter Info

`api/core/recruiter/info`

METHOD: `GET`

Headers : `{Authorization: "Token <YOUR TOKEN>"}`

Response Body
```json5
{
  bonus: 100,
  total_recruited: 5,
}
```


#### 9. Recruiter Ref Code


`api/core/recruiter`

METHOD: `GET`

Headers : `{Authorization: "Token <YOUR TOKEN>"}`

Response Body

```json5
{
  ref_code: "<UNIQUE REF CODE>"
}
```


#### 10. Commission Data

`api/core/recruite/commission`

METHOD: `GET`

Headers : `{Authorization: "Token <YOUR TOKEN>"}`

Query Params: `?page=<page_number>`

Response Body
```json5
{
  page: 1,
  next: "Link",
  prev: "Link",
  results: [
    {
       id: 1,
       recruiter: 1,
       recruit: {
         email: "Email",
         first_name: "First Name",
         last_name: "Last Name"
       },
       time_stamp: "2020-02-02 12:19:34.45666",
       commission: 100,
       transaction: 1,
       completed: true
    }
  ]
}
```

#### 11. Email Forget Reset Request

`api/auth/password/forget`

METHOD: `POST`

POST BODY 
```json5
{
  email: "email@example.com"
}
```
Response
```json5
{
  msg: 1,
  text: "Response Text"
}

```
msg - 0 - Fail

msg - 1 - Success

#### 12. Email Unique Link Validation

`api/auth/password/forget/validate`

METHOD: `POST`

POST BODY 
```json5
{
  unqiue_link: "PQRSTUVWX123"
}
```
Response
```json5
{
  msg: 1,
  text: "Response Text"
}

```
msg - 0 - Fail

msg - 1 - Success


#### 13. Email Unique Link Validation

`api/auth/password/forget/reset`

METHOD: `POST`

POST BODY 
```json5
{
  unqiue_link: "PQRSTUVWX123",
  email: "EMAIL",
  password: "PASSWORD"
}
```
Response
```json5
{
  msg: 1,
  text: "Response Text"
}

```
msg - 0 - Fail

msg - 1 - Success


## UTILS

`SendEmail`

Import Path: `Core.send_email.SendEmail`

```python
from server.apps.Core import SendEmail

SendEmail.send_email(
    subject="MAIL SUBJECT",
    body="Mail Body",
    to="MAIL SEND TO",
)

SendEmail.send_custom_context_html_email(
    template="TEMPLATE NAME",
    subject="MAIL SUBJECT",
    context="CONTEXT TEXT",
    to="EMAIL SEND TO"
)
```