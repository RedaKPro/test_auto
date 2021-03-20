# Todos

Ajouter des taches depuis les lignes de commande

## Setup

# create a virutalenv in .ven
python3 -m venv .venv

# install pytest in the virtualenv
.venv/bin/pip install pytest     # Linux, macOS
.venv\Scripts\pip install pytest # Windows

# Run the tests:
.venv/bin/pytest      # Linux, macOS
.venv\Scripts\pytest  # Windows