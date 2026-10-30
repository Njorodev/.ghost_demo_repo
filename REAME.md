# 👻 Ghost Demo Repository

A simple demonstration repository for testing, learning, and experimenting with Python development workflows.

## Features

- Sample Python scripts
- Basic project structure
- Git version control practice
- Easy setup for local development

## Project Structure

```text
.ghost_demo_repo/
│
├── README.md
├── sample.py
├── requirements.txt
└── tests/
    └── test_sample.py
```

## Prerequisites

- Python 3.10+
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/.ghost_demo_repo.git
cd .ghost_demo_repo
```

Create and activate a virtual environment:

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Sample

Execute the sample script:

```bash
python sample.py
```

Example output:

```text
Hello, Developer! Welcome to Ghost Demo Repository.
```

## Running Tests

```bash
pytest -q
```

## Development Workflow

1. Create a feature branch.

```bash
git checkout -b feature/my-feature
```

2. Make changes and commit.

```bash
git add .
git commit -m "Add new feature"
```

3. Push changes.

```bash
git push origin feature/my-feature
```

## Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

## License

This project is provided for educational and demonstration purposes.

---

Created for testing and experimentation with Python, Git, and modern development workflows.