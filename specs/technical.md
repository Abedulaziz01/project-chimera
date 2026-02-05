# Technical Specification

## Agent API Contracts

### Fetch Trends

Input:
{
"platform": "string",
"limit": number
}

Output:
{
"trends": [
{
"topic": "string",
"score": number
}
]
}

---

### Generate Content

Input:
{
"topic": "string",
"style": "string"
}

Output:
{
"content_text": "string"
}

---

### Publish Content

Input:
{
"platform": "string",
"content_text": "string"
}

Output:
{
"post_id": "string",
"url": "string"
}

---

## Database Schema

Table: posts

- id (uuid)
- platform (text)
- topic (text)
- content (text)
- url (text)
- created_at (timestamp)
