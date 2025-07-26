![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%2011-lightgrey?logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Cockpit-Stable-brightgreen)
![Plugins](https://img.shields.io/badge/Plugins-Modular%20Bucket-yellow?logo=plug&logoColor=white)
![Validation](https://img.shields.io/badge/Semantic%20Validator-Enabled-blueviolet)
# 🧠 NetMorph 3.5 — Modular Telecom Intelligence Cockpit

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%2011-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Cockpit-Stable-brightgreen)
![Plugins](https://img.shields.io/badge/Plugins-Modular%20Bucket-yellow?logo=plug)
![Validation](https://img.shields.io/badge/Semantic%20Validator-Enabled-blueviolet)

---

## ✨ Overview

NetMorph 3.5 is a plugin-driven cockpit for LTE KPI optimization, semantic metadata validation, and spatial coverage intelligence. Built by RF engineers for RF engineers, it bridges field automation with software elegance.

---

## 🧩 Architecture

- **Cockpit GUI**: Tkinter-powered modular dashboard
- **Plugin Buckets**:
  - `coverage/`: Kriging overlays for spatial health
  - `geometry/`: Site loader and sector geometry mapping
  - `predictive/`: Traffic forecasting using RF models
  - `preprocessors/`: KPI validation and data cleanup
  - `visual/`: Intelligent overlays and sector rendering
- **Registry**: Plugin registration and health diagnostics
- **Semantic Validator**: Ensures cross-flow metadata integrity

---

## 🚀 Getting Started

```bash
git clone https://github.com/abisval/netmorph-3.5.git
cd netmorph-3.5
pip install -r requirements.txt
python cockpit_boot.py

graph TD
    A[Input Data] --> B[KPI Validator]
    B --> C[Semantic Validator]
    C --> D[Coverage Intelligence]
    C --> E[Traffic Predictor]
    C --> F[Site Geometry Loader]
    D --> G[Visual Overlays]
    E --> G
    F --> G

    NetMorph-3.5/
├── cockpit_boot.py
├── gui/
├── plugins/
│   ├── coverage/
│   ├── geometry/
│   ├── predictive/
│   ├── preprocessors/
│   └── visual/
├── plugin_registry/
├── docs/
├── requirements.txt
└── README.md