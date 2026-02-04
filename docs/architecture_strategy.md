# Project Chimera: Core Architecture Strategy

## 1. Agent Pattern Selection

**Selected Pattern: Hierarchical Swarm (FastRender Pattern)**

- **Rationale**: The SRS's Planner-Worker-Judge model is a proven hierarchical swarm. It's superior to a simple Sequential Chain for an Autonomous Influencer Network because it:
  - **Enables Parallelism**: Many Workers can execute simultaneously.
  - **Builds in Quality Control**: The Judge is a dedicated safety/quality layer.
  - **Facilitates Scaling**: The Planner can manage a dynamic pool of Workers. This aligns with the industry move toward coordinated multi-agent systems[citation:10].

## 2. Human-in-the-Loop (HITL) Integration Point

**Primary HITL Point: The Judge's Escalation Queue**

- The **Judge agent** is the sole decision point for committing any action (post, transaction, reply).
- **Automated Flow**: Worker → Judge → (Auto-Approve if confidence > threshold) → Action.
- **HITL Escalation Flow**: Worker → Judge → (if confidence low or topic sensitive) → **HITL Review Queue in Dashboard** → Human Reviewer → Approve/Reject/Edit → Judge → Action.
- **Why This Works**: It centralizes governance, aligns with the "Management by Exception" principle, and makes the safety layer observable and auditable.

## 3. Database Strategy for High-Velocity Video Metadata

**Use a Polyglot Persistence Approach:**

- **PostgreSQL (SQL)**: Stores **core transactional data**. Ideal for user accounts, agent definitions, campaign goals, and immutable audit logs of _what_ was posted and _when_. Ensures ACID compliance for financial and critical operational data.
- **Weaviate (NoSQL/Vector Database)**: Stores **semantic memories and media embeddings**. Essential for the RAG pipeline. Allows efficient similarity search for "video clips about summer fashion" based on content, not just tags.
- **Redis (Cache/Queue)**: Handles **ephemeral state**. Manages the `task_queue`, `review_queue`, short-term session caches, and real-time dashboard data. Chosen for millisecond-speed.

| Data Type                             | Database   | Justification                                             |
| :------------------------------------ | :--------- | :-------------------------------------------------------- |
| User Profile, Billing                 | PostgreSQL | Integrity, relationships, complex queries.                |
| Video Metadata (title, desc, post ID) | PostgreSQL | Reliable, queryable record of published assets.           |
| Video Frame Embeddings, Semantic Tags | Weaviate   | Enables content-based retrieval for "remixing" or recall. |
| Job States, Live Sessions             | Redis      | Speed and transient nature.                               |

## 4. System Context & Future-Proofing Diagram

The diagram below illustrates the enhanced "Fractal Orchestration" model, incorporating the A2A protocol for future agent-to-agent collaboration.

```mermaid
graph TB
    subgraph “External Agent Ecosystem (Future State)”
        AEA[Analytics Agent]
        CEA[Creative Agent]
    end

    subgraph “Chimera Orchestrator & Dashboard”
        HO[Human Operator]
        CA[Chimera Agent #1]
        CB[Chimera Agent #2]
    end

    subgraph “Agent Swarm (FastRender Pattern)”
        CA --> P1[Planner]
        P1 --> TQ[Task Queue]
        TQ --> W1[Worker]
        TQ --> W2[Worker]
        W1 --> RQ[Review Queue]
        W2 --> RQ
        RQ --> J1[Judge]
        J1 --> P1
        J1 --> HITL[HITL Queue]
    end

    subgraph “MCP Servers (Tool Layer)”
        MCP_TW[Twitter]
        MCP_IG[Instagram]
        MCP_AI[Image/Video AI]
        MCP_CB[Coinbase Kit]
        MCP_WV[Weaviate]
    end

    subgraph “Persistence Layer”
        DB_PG[(PostgreSQL)]
        DB_WV[(Weaviate)]
        DB_RD[(Redis)]
    end

    HO -- Monitors/Intervenes --> HITL
    J1 -- Escalates --> HITL

    W1 & W2 -- Use Tools via --> MCP_TW & MCP_IG & MCP_AI & MCP_CB
    P1 & J1 -- Query Memory via --> MCP_WV

    MCP_WV -- Reads/Writes --> DB_WV
    MCP_CB -- Reads/Writes --> Ledger[(Blockchain)]

    CA & CB -- Log Activity --> DB_PG
    TQ & RQ -- Backed by --> DB_RD

    %% Future A2A Connections
    P1 -.->|A2A Task Delegation| AEA
    P1 -.->|A2A Task Delegation| CEA
```
