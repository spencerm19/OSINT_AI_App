# OSINT Buddy

A modern OSINT research and visualization platform with AI integration and workflow automation capabilities.

## System Requirements

- Ubuntu Server (recommended: 20.04 LTS or later)
- Docker Engine
- Docker Compose
- At least 8GB RAM
- At least 50GB free disk space

## Quick Start

1. Clone this repository:
```bash
git clone <repository-url>
cd osint-buddy
```

2. Create necessary directories and set permissions:
```bash
mkdir -p backend frontend
chmod -R 755 .
```

3. Start the application:
```bash
docker compose up -d
```

4. Access the services:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Neo4j Browser: http://localhost:7474
- n8n Workflow Editor: http://localhost:5678

## Default Credentials

- PostgreSQL:
  - User: osint
  - Password: osint
  - Database: osint

- Neo4j:
  - User: neo4j
  - Password: osintbuddy

## Data Persistence

All data is persisted in Docker volumes:
- postgres_data: PostgreSQL database
- redis_data: Redis cache
- neo4j_data: Neo4j graph database
- n8n_data: n8n workflows and credentials

## Services

- Frontend (Next.js): Modern web interface
- Backend (FastAPI): API server with AI integration
- PostgreSQL: Main database with vector storage
- Redis: Caching and session management
- Neo4j: Graph database for relationship visualization
- n8n: Workflow automation

## Development

To rebuild and update services:
```bash
docker compose build --no-cache
docker compose up -d
```

To view logs:
```bash
docker compose logs -f [service_name]
```

## Backup

To backup data, you can use Docker volume backup commands:
```bash
docker run --rm -v osintbuddy_postgres_data:/source -v /path/to/backup:/backup alpine tar czf /backup/postgres_backup.tar.gz -C /source .
docker run --rm -v osintbuddy_neo4j_data:/source -v /path/to/backup:/backup alpine tar czf /backup/neo4j_backup.tar.gz -C /source .
docker run --rm -v osintbuddy_n8n_data:/source -v /path/to/backup:/backup alpine tar czf /backup/n8n_backup.tar.gz -C /source .
```

## Security Notes

This setup is configured for home server deployment without reverse proxy or SSL. For additional security:
- Change default passwords in docker-compose.yml
- Use UFW or similar firewall to restrict port access
- Consider adding authentication to n8n
- Regularly update Docker images and dependencies 