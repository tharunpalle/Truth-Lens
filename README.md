# Truth Lens

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask%203.1-000000.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Foundation-Ready-10b981.svg)](#)

A clean, modular, and scalable foundation architecture for software and web applications. Truth Lens establishes an enterprise-grade directory structure and common architectural baseline without application-specific bloat, ready for subsequent feature engineering.

---

## 📁 Project Directory Structure

```text
Truth Lens(AG)/
│
├── src/
│   ├── components/       # Reusable UI component templates and partials
│   │   ├── __init__.py
│   │   ├── base_component.py
│   │   ├── navbar.html
│   │   └── footer.html
│   │
│   ├── pages/            # Application pages, screen views, and blueprints
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── services/         # API and external-service communication clients
│   │   ├── __init__.py
│   │   └── base_service.py
│   │
│   ├── utils/            # Reusable helper functions, logging, and formatters
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── logger.py
│   │
│   ├── models/           # Domain data models, dataclasses, and schemas
│   │   ├── __init__.py
│   │   └── base_model.py
│   │
│   ├── config/           # Application configuration and environment parsing
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── __init__.py       # Package metadata and root initialization
│   └── app.py            # Application factory and HTTP server entry point
│
├── public/               # Publicly served static assets and entry document
│   ├── assets/           # Design system styles and client scripts
│   │   ├── style.css
│   │   └── main.js
│   ├── images/           # Static images, vectors, and logos
│   │   └── logo.svg
│   └── index.html        # Foundational web landing page
│
├── tests/                # Automated unit and integration tests
│   ├── __init__.py
│   ├── test_app.py
│   ├── test_config.py
│   └── test_utils.py
│
├── docs/                 # Project documentation and specifications
│   ├── architecture.md
│   └── development_guide.md
│
├── scripts/              # Development and automation scripts
│   ├── run_dev.py
│   ├── run_tests.py
│   └── setup_env.py
│
├── .env.example          # Environment variable template
├── .gitignore            # Git exclusion rules
├── LICENSE               # MIT open-source license
├── pyproject.toml        # Standard Python package specifications
├── requirements.txt      # Runtime dependencies
└── README.md             # Project documentation
```

---

## 🏗️ Architectural Layer Breakdown

| Directory | Purpose | Key Responsibilities |
| :--- | :--- | :--- |
| `src/components/` | Reusable Components | Encapsulates reusable UI elements, view blocks, and partial templates. |
| `src/pages/` | Pages & Screen Routes | Maps HTTP requests to application views and controllers. |
| `src/services/` | External Services | Handles network requests, 3rd-party APIs, and data access layers. |
| `src/utils/` | Shared Utilities | Centralized logging, data sanitization, response envelopes. |
| `src/models/` | Data Models | Standardized entities, schemas, and serialization formats. |
| `src/config/` | Configuration | Manages environment-aware settings and security keys safely. |
| `public/` | Static Public Files | CSS styles, client scripts, vector graphics, and root HTML. |
| `tests/` | Automated Tests | Unit and integration test suites validating system integrity. |
| `docs/` | Documentation | Architectural design records and developer guides. |
| `scripts/` | Tooling & Scripts | Dev server runner, test automation, and environment bootstrapping. |

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.10 or higher (Installed: Python 3.13)
- Git (optional for version control)

### 2. Environment Setup
Bootstrap the `.env` configuration file from the template:
```bash
python scripts/setup_env.py
```

### 3. Install Dependencies (if not already installed)
```bash
pip install -r requirements.txt
```

### 4. Run Development Server
Start the local server:
```bash
python scripts/run_dev.py
```
Or directly:
```bash
python -m src.app
```

The application will start on:
- **Web Interface**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- **Status Endpoint**: [http://127.0.0.1:5000/status](http://127.0.0.1:5000/status)
- **Health Check API**: [http://127.0.0.1:5000/api/health](http://127.0.0.1:5000/api/health)

---

## 🧪 Running Automated Tests

Run the comprehensive unit test suite:
```bash
python scripts/run_tests.py
```
Or via standard unittest discovery:
```bash
python -m unittest discover -s tests
```

---

## 🗺️ Next Development Phases

Now that the common foundation is established, subsequent phases can build on this scaffold without refactoring:

1. **Phase 2 &bull; Domain Data Layer**:
   - Define concrete domain models in `src/models/`
   - Implement database connectors or repositories in `src/services/`
2. **Phase 3 &bull; Core Service & Business Logic**:
   - Implement verification and processing pipelines in `src/services/`
   - Add background workers or pipeline orchestrators
3. **Phase 4 &bull; REST API & Feature Endpoints**:
   - Extend `src/pages/` with feature-specific blueprint routes and JSON APIs
   - Add request payload validation
4. **Phase 5 &bull; Interactive UI & State Management**:
   - Build out interactive screens in `public/` and `src/components/`
   - Connect client-side state to backend API endpoints
5. **Phase 6 &bull; Authentication & Production Hardening**:
   - Add security middleware, rate limiting, and session/token management

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for full details.
