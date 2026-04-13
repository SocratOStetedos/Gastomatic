#!/bin/bash
# ─────────────────────────────────────────────────────────────────
# run_tests.sh
# Script pour lancer tous les tests et générer un rapport HTML
#
# Usage :
#   chmod +x run_tests.sh   (rendre le script exécutable, une seule fois)
#   ./run_tests.sh
# ─────────────────────────────────────────────────────────────────

echo "🚀 Lancement de la suite de tests API..."
echo "─────────────────────────────────────────"

# Lance pytest avec :
# --html=report.html  → génère un rapport HTML dans report.html
# --self-contained-html → tout dans un seul fichier (pas de dépendances CSS)
# -v                  → mode verbeux
pytest tests/ \
    --html=report.html \
    --self-contained-html \
    -v

# Récupère le code de sortie de pytest (0 = succès, 1 = échecs)
EXIT_CODE=$?

echo "─────────────────────────────────────────"

if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Tous les tests ont réussi !"
else
    echo "❌ Certains tests ont échoué. Consultez report.html pour les détails."
fi

echo "📄 Rapport HTML généré : report.html"
echo "─────────────────────────────────────────"

exit $EXIT_CODE
