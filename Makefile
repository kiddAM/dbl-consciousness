PIP_VER=9.0.1

default: server

# ---- INSTALL & SETUP
venv: venv/bin/activate
venv/bin/activate: requirements.txt
	@test -d venv || virtualenv venv
	@. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

# ---- CLEAN
clean: clean-pyc
	@rm -rf venv
clean-pyc:
	@ find . -name "*.pyc" -exec rm -rf {} \;

# ---- TOOLS
server: venv
	@. venv/bin/activate; python run.py
console: venv
	@. venv/bin/activate; python

.PHONY: clean clean-pyc
