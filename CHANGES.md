# What's Changed

## Added Docker Support
- Dockerfile + docker-compose.yml for containerization
- deploy.sh for one-command deployment
- .env.example for configuration template

## How to run in docker
### 1. Create the .env file
cp .env.example .env    

### Open .env and fill in the values

### 2. Start the app
docker compose up --build -d

## Note: Linux Blockers (Need to Address)

| Issue | Current | Fix |
|-------|---------|-----|
| **Email** | Win32 COM (Outlook) | Replace with smtplib + SMTP config |
| **CyberArk** | PowerShell script | Use CyberArk REST API directly |
| **Database Path** | `\\vn-vwl5050\...` (Windows share) | Switch to PostgreSQL or embedded SQLite |

**Status:** Docker-ready, but these 3 Windows-specific components need refactoring for Linux production.