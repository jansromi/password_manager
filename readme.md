## Stack

- **Database:** SQLite3
- **Text-based User Interface** textual

---

## Tables

### User
| Column name | Datatype |
|------|---------|
| id | `INTEGER` |
| username | `TEXT` |
| pword_hash | `TEXT` |
| salt | `TEXT` |
| creation_date | `DATE` |
| modified_date | `DATE` |

### Password
| Column name | Datatype |
|----------|---------|
| id | `INTEGER` |
| user_id | `INTEGER` |
| application_name | `TEXT` |
| application_handle | `TEXT` |
| pword_hash | `TEXT` |
| creation_date | `DATE` |
| modified_date | `DATE` |

---

## GUI


