```mermaid
classDiagram
  class Contact {
    + id (PK)
    + name
    + email
    + address
  }

  class ContactPhone {
    + id (PK)
    + phone
  }

  Contact "1" -- "0..*" ContactPhone : Has
```
