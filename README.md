# Database Schema Diagram

Below is a simplified database schema diagram represented using Mermaid:

```mermaid
erDiagram
  Contact ||--o{ ContactPhone : Belongs_to
  Contact {
    + id (PK)
    name
    email
    address
  }
  ContactPhone {
    + id (PK)
    phone
  }
