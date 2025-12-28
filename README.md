# Role-Based User Management System

## Overview
This project demonstrates a real-world Git workflow used in team-based software development.
It shows how code moves safely from **idea → development → testing → production**, using
branching, role-based permissions, and CI/CD automation.

The application itself is a simple **role-based user management system** built in Python,
where only admins can manage users and roles.

---

## Objectives
- Demonstrate Git branching strategy (`main`, `development`, `feature/*`)
- Show safe collaboration using pull requests
- Enforce role-based permissions at code level
- Automate testing using CI/CD
- Protect production code using branch rules

---

## Branching Strategy

| Branch | Purpose |
|------|--------|
| `main` | Production-ready code |
| `development` | Integration and testing |
| `feature/*` | Individual feature development |

> Direct pushes to `main` and `development` are restricted.

---

## Role-Based Permissions (Application Level)

| Role | Permissions |
|----|------------|
| Admin | Add users, change roles |
| User | Read-only access |

These permissions are enforced in the application logic.

---

## GitHub Permissions (Repository Level)

| Role | Access Level |
|----|-------------|
| Admin | Full control |
| Maintainer | Merge pull requests |
| Developer | Push feature branches |
| Tester | Read and validate |
| Viewer | Read-only |

---

## Project Structure

git-workflow-demo/
│
├── app/
│ ├── auth.py
│ ├── user_service.py
│ └── file_store.py
│
├── tests/
│ └── run_tests.py
│
├── data/
│ └── users.json

├── .github/
│ └── workflows/
│ └── ci.yml
│
├── README.md
└── requirements.txt


---

## Development Workflow

1. Create a feature branch from `development`
2. Implement changes
3. Commit with meaningful messages
4. Open a Pull Request to `development`
5. CI pipeline runs automated tests
6. After approval, merge into `development`
7. Merge `development` into `main` for release

---

## CI/CD Pipeline

- Triggered on:
  - Push to `development`
  - Pull request to `main`
- Steps:
  - Checkout code
  - Setup Python environment
  - Run automated permission and logic tests

Only code that passes CI is allowed to be merged into `main`.

---

## How to Run Locally

```bash
python tests/run_tests.py
