# Architecture & Modular Foundation Guide

## 1. Overview

**Truth Lens** is structured using a clean, layered architectural pattern designed for high maintainability, separation of concerns, and effortless scalability.

The foundational design decouples presentation, routing, core business services, utilities, data schemas, and static assets into dedicated, modular packages.

```
Truth Lens Architecture
┌────────────────────────────────────────────────────────┐
│                      Presentation                      │
│        (public/ assets, index.html, components/)       │
└───────────────────────────┬────────────────────────────┘
                            │ HTTP / API Requests
┌───────────────────────────▼────────────────────────────┐
│                      Routing Layer                     │
│                       (src/pages/)                     │
└───────────────────────────┬────────────────────────────┘
                            │ Dispatch
┌───────────────────────────▼────────────────────────────┐
│                     Service Layer                      │
│                     (src/services/)                    │
└─────────────────┬───────────────────┬──────────────────┘
                  │                   │
┌─────────────────▼────────┐  ┌───────▼──────────────────┐
│       Domain Models      │  │        Utilities         │
│       (src/models/)      │  │       (src/utils/)       │
└──────────────────────────┘  └──────────────────────────┘
                  │                   │
┌─────────────────▼───────────────────▼──────────────────┐
│                     Configuration                      │
│                     (src/config/)                      │
└────────────────────────────────────────────────────────┘
```

---

## 2. Directory Responsibilities

| Directory | Architectural Layer | Responsibility |
| :--- | :--- | :--- |
| `src/components/` | Reusable UI Elements | Reusable template components, partials, and UI modules isolated from state logic. |
| `src/pages/` | Routing / Page Controllers | Blueprint routes and views that handle page requests and user navigation. |
| `src/services/` | Business & Integrations | External API clients, service connectors, and business processing logic. |
| `src/utils/` | Cross-Cutting Utilities | Logging, sanitization, response shaping, and general helper functions. |
| `src/models/` | Domain / Schemas | Data contracts, dataclasses, serialization, and entity definitions. |
| `src/config/` | Application Configuration | Environment parsing, path resolution, security parameters, and defaults. |
| `public/` | Public Static Assets | Client-facing static assets (`assets/style.css`, `assets/main.js`, `images/logo.svg`). |
| `tests/` | Automated Testing | Unit tests and integration tests verifying application integrity. |
| `docs/` | Documentation | Architecture specifications, development guides, and onboarding references. |
| `scripts/` | Dev & Automation Scripts | Local development server runners, environment setup, and test automation. |

---

## 3. Core Design Principles

1. **Strict Separation of Concerns**: Components do not execute business services directly; pages coordinate requests; services manage domain operations; models encapsulate data schemas.
2. **Zero Hardcoded Secrets**: Secrets and environment-specific settings are strictly managed via `.env` and typed in `src/config/settings.py`.
3. **Extensibility Without Refactoring**: Adding a new feature involves creating a service in `src/services/`, defining a model in `src/models/`, adding a route in `src/pages/`, and attaching components without altering existing code.
4. **Standardized Responses**: All API endpoints return a predictable JSON envelope produced by `src/utils/helpers.py:json_response()`.
