
# 🌿 Rhizomata — Where Roots Become Destiny

![Rhizomata Banner](core/static/core/assets/game%20board.webp)

Rhizomata is the official digital experience and promotional platform engineered and developed by Ishtiaq-Codes for the premium, mystical, and philosophical physical board game conceptualized by Amna Noor. This repository contains the complete architecture for the web experience, featuring a custom-built Content Management System (CMS), high-performance scrolling animations, and an immersive user interface.

## 🌟 Features

- **Immersive User Experience:** Built with a dark, premium aesthetic utilizing glassmorphism, dynamic gradients, and custom typography (Cinzel & Playfair Display).
- **High-Performance Animations:** Powered by **GSAP ScrollTrigger** and **Lenis Smooth Scroll**, fully hardware-accelerated for buttery-smooth 60fps scrolling on both desktop and mobile.
- **Custom Django CMS:** A fully custom, secure Developer Console allowing the creator to dynamically upload game cards (Identity, Situation, Context), game pawns, gallery visuals, and preview images without touching code.
- **Optimized Asset Delivery:** All game assets are compressed into modern `.webp` formats and served efficiently using **WhiteNoise** with async image decoding.
- **Dynamic Site Settings:** Global settings (contact emails, social links, rulebooks) are easily managed directly from the database.

## 🛠️ Tech Stack

- **Backend:** Python 3.12, Django 6.0
- **Frontend:** HTML5, Vanilla JS, TailwindCSS
- **Animations:** GSAP (GreenSock), ScrollTrigger, Lenis
- **Database:** SQLite3 (optimized for read-heavy CMS delivery)
- **Production Server:** Gunicorn, AWS EC2 (Ubuntu Linux)
- **Static File Management:** WhiteNoise

## 🚀 Local Development Setup

Follow these steps to run the Rhizomata platform on your local Windows/Mac machine.

### 1. Clone the Repository
```bash
git clone https://github.com/Ishtiaq-Codes/RHIZOMATA.git
cd RHIZOMATA
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```
Activate the environment:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Development Server
```bash
python manage.py runserver
```
The site will now be available at `http://127.0.0.1:8000/`.

## 🌐 Production Deployment (AWS)

The live production environment is hosted on an AWS EC2 instance running Ubuntu. Static files are collected into a `staticfiles` directory and served via WhiteNoise, while dynamic requests are handled by Gunicorn.

### Deployment Steps
Whenever new code is pushed to the `main` branch, run the following commands on the AWS terminal to deploy the updates safely without overwriting the live production database:

```bash
# 1. Stash any live database changes to prevent merge conflicts
git stash

# 2. Pull the latest code from GitHub
git pull origin main

# 3. Restore the live database
git stash pop

# 4. Collect new static files/assets
python manage.py collectstatic --noinput

# 5. Restart the Gunicorn server to apply Python changes
sudo systemctl restart gunicorn
```

## 🗂️ Project Structure

```text
RHIZOMATA/
├── core/                       # Main Django App
│   ├── models.py               # Database schemas for Cards, Pawns, and Settings
│   ├── views.py                # Route controllers
│   ├── context_processors.py   # Global variables (Site Settings injection)
│   ├── static/core/assets/     # Global static assets (Favicons, Logos)
│   └── templates/
│       ├── core/               # Public-facing HTML templates
│       └── admin/              # Custom Developer Console overrides
├── rhizomata_project/          # Django Project Settings
│   ├── settings.py             # Configuration (WhiteNoise, Installed Apps)
│   └── urls.py                 # URL Routing (including custom admin path)
├── media/                      # Dynamically uploaded CMS images (Cards, Pawns)
├── staticfiles/                # Compiled static files for production
├── requirements.txt            # Python dependencies
└── db.sqlite3                  # Production Database
```

## 🔐 Developer Console (CMS)

The backend CMS is heavily customized for managing the game's assets. For security purposes, the default Django `/admin/` route has been hidden and replaced with a custom, unguessable path.

To manage site content, log into the Developer Console, where you can modify:
- **Site Settings:** Update contact emails, Instagram links, LinkedIn profiles, and Rulebook PDFs.
- **Game Cards:** Upload new Identity, Situation, or Context cards with front and back `.webp` images.
- **Game Pawns:** Manage 3D rendered pawn assets (e.g., Ambition, Stability).
- **Visuals:** Update the Gallery and Component Preview carousels.

## 🎨 Credits & Copyright

- **Game Design & Concept:** Amna Noor
- **Web Development & Architecture:** Ishtiaq-Codes
- **Copyright:** © 2026 Rhizomata. All Rights Reserved.
```
