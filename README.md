# 🛡️ Shield Scan — URL Phishing Detector

> A lightweight cybersecurity auditing tool for detecting suspicious URLs using heuristic phishing analysis.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-UI-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 🔎 Overview

**Shield Scan** is a Flask-based web application that analyzes URLs for common phishing indicators.

Instead of relying only on a blacklist, the application examines the structure and characteristics of a submitted URL and produces a **threat-oriented assessment** using heuristic rules.

The workflow is simple:

**Enter URL → Analyze → Review Result**

---

## 🖥️ Preview

<p align="center">
  <img src="Demo Image.png" alt="Shield Scan URL Phishing Detector" width="900">
</p>

<p align="center">
  <i>Shield Scan — URL analysis interface</i>
</p>

---

## ✨ Key Features

### 🛡️ Heuristic URL Analysis

The application checks submitted URLs for suspicious characteristics such as:

- IP-based URLs
- Unusual or excessively long subdomains
- Suspicious URL structures
- Phishing-related keywords
- Login and verification terminology
- Banking-related terminology
- Other configurable URL patterns

### ⚡ Lightweight Architecture

A small Flask application with a straightforward frontend, making it easy to run locally and modify.

### 🎨 Cybersecurity-Focused UI

The interface provides:

- Dark cybersecurity-inspired design
- Glassmorphism-inspired components
- Responsive layout
- High-contrast threat feedback
- Minimal input workflow
- Diagnostic-friendly presentation

### 📱 Responsive Design

The interface is designed to remain usable across desktop and smaller screens.

---

## 🔬 How It Works

```text
┌─────────────────┐
│    Enter URL    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Normalize Input │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Heuristic Checks│
│                 │
│ • IP Address    │
│ • Subdomains    │
│ • Keywords      │
│ • URL Structure │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Threat Analysis │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Display Result  │
└─────────────────┘