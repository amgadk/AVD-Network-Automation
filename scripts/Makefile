### Generic Variables
SHELL := /bin/bash

.PHONY: all
all: install-pyavd install-collection update-apt install-gh

.PHONY: install-pyavd
install-pyavd: ## Install ansible collections
	pip install "pyavd[ansible]==5.7.0"

.PHONY: install-collection
install-collection: ## Build wan WAN artifacts
	ansible-galaxy collection install arista.avd:==5.7.0

.PHONY: update-apt
update-apt: ## Deploy config to CV
	sudo apt update

.PHONY: install-gh
install-gh: ## Deploy config to CV
	sudo apt install gh