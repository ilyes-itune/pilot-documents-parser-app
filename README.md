# Pilot Documents Parser App

Application complète pour parser des fichiers (.msg, .pdf, .doc) et extraire les données structurées, tableaux et emails.

## 🏗️ Architecture

- **Frontend**: Angular 17+
- **Backend**: Python/FastAPI
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose

## 📋 Prérequis

### Option 1: Docker (Recommandé)
- Docker
- Docker Compose

### Option 2: Manual Setup
- Node.js (v18+)
- Python (3.9+)
- PostgreSQL (14+)

## 🚀 Installation rapide (Docker Compose)

```bash
# 1. Clone le repo
git clone https://github.com/ilyes-itune/pilot-documents-parser-app.git
cd pilot-documents-parser-app

# 2. Copie le fichier .env
cp .env.example .env

# 3. Lance les services
docker-compose up -d

# 4. Accès
# Frontend: http://localhost:4200
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
# Database: localhost:5432
```

## 📦 Installation manuelle

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
ng serve
```

## ✅ Fonctionnalités

- ✅ Upload de fichiers (.msg, .pdf, .doc, .docx)
- ✅ Extraction de métadonnées
- ✅ Extraction de tableaux structurés
- ✅ Extraction d'emails (fichiers .msg)
- ✅ Affichage interactif des données
- ✅ Export JSON
- ✅ Prêt pour PostgreSQL

## 📚 Structure du projet

```
pilot-documents-parser-app/
├── frontend/                    # Application Angular
│   ├── src/
│   │   ├── app/
│   │   │   ├── services/
│   │   │   │   └── api.service.ts
│   │   │   ├── features/
│   │   │   │   ├── upload/
│   │   │   │   └── documents/
│   │   │   └── app.component.ts
│   │   └── main.ts
│   ├── angular.json
│   ├── package.json
│   ├── Dockerfile
│   └── ...
├── backend/                     # API FastAPI
│   ├── main.py
│   ├── models/
│   │   ├── schemas.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── parser_service.py
│   │   ├── msg_parser.py
│   │   ├── pdf_parser.py
│   │   ├── doc_parser.py
│   │   └── __init__.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── ...
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## 🔌 API Endpoints

```
POST   /api/parse/msg         - Parser fichier .msg
POST   /api/parse/pdf         - Parser fichier .pdf
POST   /api/parse/doc         - Parser fichier .doc/.docx
GET    /api/documents         - Lister les documents (à intégrer BD)
GET    /health                - Vérifier la santé de l'API
```

## 🛠️ Technologies

### Frontend
- Angular 17+
- TypeScript
- Angular Material UI
- RxJS
- Reactive Forms

### Backend
- FastAPI
- Pydantic v2
- SQLAlchemy (ORM)
- python-docx (Word)
- PyPDF2 (PDF)
- extract-msg (Outlook)
- PostgreSQL Driver

### DevOps
- Docker
- Docker Compose
- Python venv

## 📝 Configuration

### Fichier `.env`

```env
# Database
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=pilot_documents
DB_HOST=localhost
DB_PORT=5432

# Backend
BACKEND_HOST=localhost
BACKEND_PORT=8000
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/pilot_documents

# Frontend
FRONTEND_HOST=localhost
FRONTEND_PORT=4200
API_URL=http://localhost:8000/api

# Upload
MAX_UPLOAD_SIZE=50000000
UPLOAD_DIR=uploads/
```

## 🐛 Troubleshooting

### Port déjà utilisé
```bash
# Trouver le processus
lsof -i :8000  # Backend
lsof -i :4200  # Frontend
lsof -i :5432  # Database

# Tuer le processus
kill -9 <PID>
```

### Erreur de connexion BDD
```bash
# Vérifier PostgreSQL
psql postgresql://postgres:postgres@localhost:5432/pilot_documents

# Réinitialiser les services
docker-compose down
docker-compose up --build
```

### Problèmes CORS
Vérifier la configuration CORS dans `backend/main.py`

### Dépendances MSG
```bash
pip install extract-msg --upgrade
```

## 🚀 Prochaines étapes

- [ ] Intégration PostgreSQL (models + migrations)
- [ ] Authentification utilisateur
- [ ] Tests unitaires
- [ ] CI/CD avec GitHub Actions
- [ ] Déploiement AWS/GCP
- [ ] Extraction avancée de tableaux (Camelot)
- [ ] Support fichiers supplémentaires (XLS, PPT)

## 📄 License

MIT

---

**Besoin d'aide ?** Consultez [INSTALLATION.md](./INSTALLATION.md) pour plus de détails.
