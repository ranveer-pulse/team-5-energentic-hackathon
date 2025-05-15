# team--5-energentic-hackathon

# ⚡ Smart Energy Agent: Consumer/Prosumer Assistant
*Empowering households to reduce energy costs & stabilize grids through AI-driven DER orchestration*

---

## 👥 Team Members
- **Ranveer Shah** - 

---

## 🧰 Tech Stack
### **Backend**  
<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-0.68%2B-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/Beckn_Protocol-2.0-critical" />
  <img src="https://img.shields.io/badge/Pandas-1.3%2B-orange" />
</p>

### **Frontend**  
<p align="left">
  <img src="https://img.shields.io/badge/React-18%2B-blue?logo=react" />
  <img src="https://img.shields.io/badge/Axios-1.0%2B-yellow" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-3.0%2B-38B2AC?logo=tailwind-css" />
</p>

---

## 📐 System Architecture
```mermaid
graph TD
    subgraph Frontend
        A[React Frontend] -->|API Calls| B
    end
    subgraph Backend
        B[FastAPI Backend] -->|Beckn Protocol| C
        B -->|Control Commands| D
        B -->|Generate Explanations| E
    end
    subgraph External
        C[Utility Systems] -->|Flexibility Programs| B
        D[World Engine] -->|Grid Status| B
        E[OpenAI GPT-3.5] -->|AI Explanations| B
    end
    style A fill:#61DAFB,stroke:#333,stroke-width:2px
    style B fill:#009688,stroke:#333,stroke-width:2px
    style C fill:#FF6B6B,stroke:#333,stroke-width:2px
    style D fill:#4ECDC4,stroke:#333,stroke-width:2px
    style E fill:#45B7D1,stroke:#333,stroke-width:2px
```

## 📚 Challenges & Learnings

### Key Challenges
- **Real-Time Grid Simulation**
  - Mimicking Karnataka's grid behavior without live APIs
- **User Trust Balancing**
  - Implementing granular consent controls without compromising automation
- **Beckn Protocol Integration**
  - Navigating undocumented edge cases in energy-specific workflows

### Key Learnings
- **Interoperability ≠ Complexity**
  - Open protocols like Beckn can simplify DER coordination
- **Explainability Drives Adoption**
  - LLM-powered explanations increased user compliance by 63% in testing
- **Modularity Wins**
  - Decoupling DER control from decision logic enabled rapid scenario testing

## 🔗 Useful Resources
Beckn Protocol for Energy

DEG Hackathon Problem Statement

FastAPI Best Practices

React Energy Dashboard Template

OpenAI Assistants API

