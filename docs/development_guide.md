# Developer Onboarding & Contribution Guide

## 1. Prerequisites

- **Python**: Version 3.10+ (Current runtime: Python 3.13)
- **Pip**: Latest version
- **Git**: Version control

---

## 2. Quick Setup

### Step 1: Clone and Enter Repository
```bash
git clone <repository-url>
cd "Truth Lens(AG)"
```

### Step 2: Configure Environment Variables
Copy the template `.env.example` to `.env`:
```bash
python scripts/setup_env.py
```
Or manually:
```bash
cp .env.example .env
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 3. Running the Foundation Application

Start the local development server:
```bash
python scripts/run_dev.py
```
Or directly via Python module:
```bash
python -m src.app
```

The application will be accessible at:
- **Web UI**: `http://127.0.0.1:5000/`
- **Module Status**: `http://127.0.0.1:5000/status`
- **Health Check API**: `http://127.0.0.1:5000/api/health`

---

## 4. Running Automated Tests

Run the test suite using the provided runner:
```bash
python scripts/run_tests.py
```
Or using Python's built-in `unittest`:
```bash
python -m unittest discover -s tests
```

---

## 5. Coding Standards & Conventions

- **Python**: Adhere to PEP 8 standards. Use type annotations where appropriate.
- **Imports**: Group imports into standard library, third-party, and local modules.
- **Static Assets**: Keep CSS modern, modular, and responsive within `public/assets/`.
- **Security**: Never commit `.env` or sensitive credentials to source control.
