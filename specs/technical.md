# Technical Specifications

## System Architecture

High-level components:

- Orchestrator Agent
- Skill Layer
- MCP Servers
- Database
- External APIs (social platforms)

Architecture Flow:

Agent → Skill → MCP / External API → Database

(Architecture diagram to be added later)

---

## API Contracts

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

### Table: trends

```sql
CREATE TABLE trends (
    id UUID PRIMARY KEY,
    topic VARCHAR(255) NOT NULL,
    platform VARCHAR(50) NOT NULL,
    volume INTEGER,
    discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
