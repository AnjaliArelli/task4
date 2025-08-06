# Flask REST API Example

This project is a simple REST API built with Flask for managing users.  
It supports basic CRUD operations: Create, Read, Update, and Delete.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone or download this repository.
2. Install Flask using pip:
   ```
   pip install flask
   ```

## Usage

1. Start the Flask server:
   ```
   python rest.py
   ```
2. The API will run at `http://127.0.0.1:5000`.

OUTPUT :
  ```
 Invoke-WebRequest http://127.0.0.1:5000/users


StatusCode        : 200
StatusDescription : OK
Content           : [
                      {
                        "id": 1,
                        "name": "Rohee"
                      },
                      {
                        "id": 2,
                        "name": "Anjali"
                      }
                    ]

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 89
                    Content-Type: application/json
                    Date: Wed, 06 Aug 2025 14:38:21 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    [
                      {
                        "id": 1,
                        "name": "Roh...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 89], [Content-Type,
                    application/json], [Date, Wed, 06 Aug 2025 14:38:21 GMT]...}
Images            : {}                                                                        InputFields       : {}                                                                        Links             : {}                                                                        ParsedHtml        : mshtml.HTMLDocumentClass                                                  
RawContentLength  : 89


 Invoke-WebRequest -Uri http://127.0.0.1:5000/users -Method POST -Body
 '{"name":"NewUser"}' -ContentType "application/json"


StatusCode        : 201
StatusDescription : CREATED
Content           : {
                      "id": 3,
                      "name": "NewUser"
                    }

RawContent        : HTTP/1.1 201 CREATED
                    Connection: close
                    Content-Length: 35
                    Content-Type: application/json
                    Date: Wed, 06 Aug 2025 14:40:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {
                      "id": 3,
                      "name": "NewUse...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 35], [Content-Type,
                    application/json], [Date, Wed, 06 Aug 2025 14:40:59 GMT]...}
Images            : {}
InputFields       : {}                                                                        Links             : {}                                                                        ParsedHtml        : mshtml.HTMLDocumentClass                                                  RawContentLength  : 35                                                                        

 Invoke-WebRequest -Uri http://127.0.0.1:5000/users/1 -Method PUT -Body '{"name":"UpdatedName"}' -ContentType "application/json
StatusCode        : 200
StatusDescription : OK
Content           : {
                      "id": 1,
                      "name": "UpdatedName"
                    }

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 39
                    Content-Type: application/json
                    Date: Wed, 06 Aug 2025 14:41:20 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {
                      "id": 1,
                      "name": "UpdatedName...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 39], [Content-Type,
                    application/json], [Date, Wed, 06 Aug 2025 14:41:20 GMT]...}
Images            : {}                                                                        InputFields       : {}                                                                        Links             : {}                                                                        ParsedHtml        : mshtml.HTMLDocumentClass                                                  
RawContentLength  : 39

 Invoke-WebRequest -Uri http://127.0.0.1:5000/users/1 -Method DELETE
StatusCode        : 200
StatusDescription : OK
Content           : {
                      "result": "User deleted"
                    }

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 31
                    Content-Type: application/json
                    Date: Wed, 06 Aug 2025 14:42:25 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {
                      "result": "User deleted"
                    }

Forms             : {}
Headers           : {[Connection, close], [Content-Length, 31], [Content-Type,
                    application/json], [Date, Wed, 06 Aug 2025 14:42:25 GMT]...}
Images            : {}                                                                        InputFields       : {}                                                                        Links             : {}                                                                        ParsedHtml        : mshtml.HTMLDocumentClass                                                  
RawContentLength  : 31



PS C:\Users\rohit\Task4> (Invoke-WebRequest http://127.0.0.1:5000/users).Content
[
  {
    "id": 2,
    "name": "Anjali"
  },
  {
    "id": 3,
    "name": "NewUser"
  }
]


