# RegRadar - veille réglementaire pour NovaCare Logistics

Prototype de tableau de bord (Streamlit) réalisé dans le cadre du TP 3
« Gouvernance RGPD et souveraineté numérique » (EPITA - MSCDS1), Mission 3.

Il présente 3 alertes réglementaires issues de sources officielles
(UE, États-Unis, Asie-Pacifique), classées par zone, date, thème et niveau
d'impact sur NovaCare, avec des filtres.

## Alertes présentées

| Zone | Source officielle | Alerte | Date |
|---|---|---|---|
| UE | EUR-Lex | Règlement (UE) 2026/1744 (omnibus numérique IA) | 8 juillet 2026 |
| États-Unis | Federal Register | Décret 14412 sur les attaques cryptographiques avancées | 25 juin 2026 |
| Asie-Pacifique | APEC | Déclaration ministérielle de Chengdu sur le numérique et l'IA | 23 juillet 2026 |

## Lancer le prototype

1. Installer Python 3.10 ou plus récent (python.org).
2. Dans un terminal, ouvrir le dossier du projet, puis installer les dépendances :

   ```
   pip install -r requirements.txt
   ```

3. Lancer l'application :

   ```
   streamlit run app.py
   ```

   Une page s'ouvre dans le navigateur (adresse locale `http://localhost:8501`).

## Fichiers

- `app.py` : le tableau de bord (données, filtres, affichage).
- `requirements.txt` : les bibliothèques nécessaires.

## Ajouter une alerte

Dans `app.py`, copier un bloc de la liste `ALERTES`, le coller à la suite et
modifier ses valeurs.




