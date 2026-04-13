# 🧪 API Test Automation — Python & PyTest

Projet d'automatisation de tests sur une API REST réelle, réalisé avec **Python** et **PyTest**.  
Conçu pour démontrer des compétences en test logiciel, bonnes pratiques de code, et CI/CD.

> **API testée** : [JSONPlaceholder](https://jsonplaceholder.typicode.com) — une fausse API REST gratuite et publique.

---

## 📁 Structure du projet

```
api-test-automation/
│
├── tests/                    # Tous les fichiers de tests
│   ├── conftest.py           # Fixtures partagées (données réutilisables)
│   ├── test_posts.py         # Tests CRUD sur /posts
│   ├── test_users.py         # Tests sur /users
│   └── test_errors.py        # Tests des erreurs et cas limites
│
├── utils/                    # Utilitaires réutilisables
│   └── api_client.py         # Client HTTP centralisé
│
├── .github/
│   └── workflows/
│       └── ci.yml            # Pipeline CI/CD GitHub Actions
│
├── pytest.ini                # Configuration PyTest
├── requirements.txt          # Dépendances Python
├── run_tests.sh              # Script de lancement des tests
└── README.md                 # Ce fichier
```

---

## ⚙️ Installation

### Prérequis
- Python 3.9 ou supérieur
- pip

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/TON_USERNAME/api-test-automation.git
cd api-test-automation

# 2. (Recommandé) Créer un environnement virtuel
python -m venv venv
source venv/bin/activate       # Sur Linux/Mac
# venv\Scripts\activate        # Sur Windows

# 3. Installer les dépendances
pip install -r requirements.txt
```

---

## 🚀 Lancer les tests

### Option 1 — Script automatique (recommandé)
```bash
chmod +x run_tests.sh
./run_tests.sh
```
→ Lance tous les tests et génère un **rapport HTML** (`report.html`)

### Option 2 — PyTest directement
```bash
# Tous les tests
pytest

# Un fichier spécifique
pytest tests/test_posts.py

# Mode verbeux
pytest -v

# Avec rapport HTML
pytest --html=report.html --self-contained-html
```

---

## 🧪 Ce que les tests vérifient

| Fichier | Ce qui est testé |
|---|---|
| `test_posts.py` | GET/POST/PUT/DELETE sur `/posts` — codes de statut, structure JSON, cohérence des données |
| `test_users.py` | Liste et détail des utilisateurs — validation des champs, relation avec les posts |
| `test_errors.py` | Codes 404, format JSON, temps de réponse, types de données |

---

## 🔄 Pipeline CI/CD

Le fichier `.github/workflows/ci.yml` configure un **pipeline automatique** sur GitHub Actions :

```
Push sur main
     ↓
Checkout du code
     ↓
Installation de Python + dépendances
     ↓
Exécution de tous les tests
     ↓
Génération et sauvegarde du rapport HTML
```

**Résultat** : à chaque modification du code, les tests s'exécutent automatiquement. Si un test échoue, GitHub te le signale immédiatement.

---

## 📈 Idées d'améliorations

- [ ] Ajouter des tests avec `pytest-mock` pour simuler des erreurs réseau
- [ ] Intégrer `pytest-cov` pour mesurer la couverture de code
- [ ] Tester une vraie API avec authentification (token JWT)
- [ ] Ajouter des tests de performance avec `locust`
- [ ] Utiliser `Faker` pour générer des données de test aléatoires

---

## 🛠️ Technologies utilisées

- **Python 3.11**
- **PyTest** — framework de tests
- **Requests** — appels HTTP
- **pytest-html** — génération de rapports
- **GitHub Actions** — CI/CD

---

## 👤 Auteur

Étudiant ingénieur en informatique — Projet portfolio QA/Automation.
