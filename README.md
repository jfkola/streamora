<br/>
<div align="center">
  <h1 style="color: #00E5FF; font-weight: 900; letter-spacing: -1px;">STREAMORA</h1>
  <p><b>An advanced, AI-driven cinematic streaming platform built with Python & Flask.</b></p>
</div>

---

## 🚀 Overview

Streamora is a premium video-on-demand platform engineered for scale. Built with a robust Flask backend and an interactive glassmorphic UX, Streamora bypasses standard NGINX limitations through internal Cloudinary chunked streaming algorithms, allowing massive HD video handling natively.

### Key Features
- **Intelligent Playback Tracking**: An asynchronous Javascript daemon inherently syncs user playback sessions, mapping `.currentTime` timestamps securely to a PostgreSQL database every 5 seconds.
- **Dynamic "My List" Saving**: Ghost-loading AJAX operations allow users to organically curate extensive watch-later catalogs without ever navigating away from or reloading their active dashboard.
- **Predictive Recommendations**: The platform inherently tracks viewing histories to calculate mathematical category preferences, dynamically serving highly-rated cinematic choices labeled dynamically.
- **Chunked File Pipelining**: Hardened upload logic that shivers 1GB+ movies into manageable 20MB blocks inside a localized OS buffer array before firing them efficiently to Cloudinary's ingress edge nodes.

---

## 🛠 Tech Stack

**Frontend Framework:**
- HTML5, Jinja2, Vanilla Javascript
- Bootstrap 5 CSS Framework
- High-Performance Glassmorphism Effects & Variable Theming

**Backend Architecture:**
- **Core Server:** Python / Flask
- **Relational Mapping:** Flask-SQLAlchemy
- **Media Ingestion:** Cloudinary CLI / Werkzeug
- **Deployment Strategy:** Render Web Service via Gunicorn
- **Database Architecture:** PostgreSQL

---

## ☁️ Deployment Guide (Render & GitHub)

Streamora is purpose-built to run effortlessly on modern Infrastructure-as-Service (IaaS) clouds. This repository contains a pre-built `render.yaml` manifest.

1. **Fork or Push** this entire repository privately to your GitHub account.
2. Link your GitHub account to [Render.com](https://render.com).
3. Open your Render Dashboard and select **Blueprints** -> **New Blueprint Instance**.
4. Select the Streamora repository.
5. Render's orchestration framework will detect the `render.yaml` directives and automatically:
   - Instantiate a dedicated PostgreSQL database container.
   - Boot up a Python standard web environment.
   - Install production `gunicorn` servers via `requirements.txt`.
   - Wire the `DATABASE_URL` routing internally.
6. The only manual step required is to plug your `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, and `CLOUDINARY_API_SECRET` flags into Render's secure *Environment Variables* tab inside your new Web Service.

---

<div align="center">
  <sub>Built exclusively by <b>Antigravity</b>. &copy; 2026.</sub>
</div>
