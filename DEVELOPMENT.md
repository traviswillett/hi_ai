# AI-enabled Satellite Tracker - Local Development

## 🚀 Quick Start (Docker)

### Prerequisites
- Docker Desktop installed on your machine
- Git (to clone the repository)

### Run Locally
```bash
# Clone the repository (if you haven't already)
git clone https://github.com/traviswillett/hi_ai.git
cd hi_ai

# Start the development server
docker-compose up

# Or build and run in one command
docker-compose up --build
```

### 🌐 Access Your Site
- **Local site:** http://localhost:4000 (development mode - CSS properly loaded)
- **LiveReload:** Automatically refreshes when you make changes
- **Stop server:** Press `Ctrl+C` or run `docker-compose down`

**Note:** The development server uses a special configuration that removes the `/hi_ai/` base path to ensure CSS and assets load correctly locally.

### 🔄 Development Workflow
1. Edit your markdown files, CSS, or layouts
2. Save the changes
3. Browser automatically refreshes with updates
4. Preview looks exactly like GitHub Pages will render it

### 🛠️ Useful Commands
```bash
# Start in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the server
docker-compose down

# Rebuild after changing Gemfile
docker-compose up --build

# Clean rebuild (if you have issues)
docker-compose down
docker-compose build --no-cache
docker-compose up
```

### 📂 File Structure
```
hi_ai/
├── Dockerfile              # Jekyll container setup
├── docker-compose.yml      # Development environment
├── Gemfile                 # Ruby dependencies
├── _config.yml             # Jekyll configuration
├── README.md               # This file
├── step1_get_satellites/   # Tutorial steps
├── step2_data_processing/  # Tutorial steps
├── _layouts/               # Custom layouts
└── assets/                 # CSS, images, etc.
```

### 🚨 Troubleshooting

**Docker Desktop not running:**
```bash
# Windows: Use the PowerShell script to start Docker Desktop
.\start-dev.ps1

# Or manually start Docker Desktop from Start Menu, then run:
docker-compose up
```

**Docker Desktop not installed:**
1. Download from https://www.docker.com/products/docker-desktop
2. Install and restart your computer
3. Run `docker-compose up`

**Quick alternative (Node.js only):**
```bash
# Windows PowerShell
.\start-simple.ps1

# Mac/Linux
chmod +x start-simple.sh
./start-simple.sh
```
*Note: Simple server shows raw files, not full Jekyll processing*

**Other issues:**
- **Port 4000 in use:** Change the port in `docker-compose.yml` (e.g., `"4001:4000"`)
- **Changes not reflecting:** Try `docker-compose restart`
- **Bundle errors:** Run `docker-compose down && docker-compose up --build`
- **Permission errors:** Try running PowerShell as Administrator

---

## Manual Installation (Alternative)

If you prefer not to use Docker:

```bash
# Install Ruby and Bundler
gem install bundler

# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve --livereload

# Access at http://localhost:4000
```