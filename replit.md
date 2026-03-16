# Grilles ECOS - Medical Evaluation Forms

## Overview

A static French medical website serving 253 clinical case evaluation grids (Grilles ECOS) across 5 categories. Each HTML file is a self-contained interactive scoring sheet for evaluating medical student performance during simulated patient encounters (ECOS = Examens Cliniques Objectifs Structurés / OSCEs).

## Categories

- **AMBOSS**: 40 cases
- **German**: 88 cases
- **RESCOS**: 41 cases (includes case 9b)
- **USMLE**: 44 cases
- **USMLE Triage**: 40 cases

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

- **Technology**: Pure HTML5 with embedded CSS and JavaScript — no frameworks, no build tools, no dependencies
- **Landing page** (`index.html`): Modern dashboard with Inter font, indigo-to-purple gradient header, sticky toolbar with real-time search (diacritics-normalized) and category filter tabs, 3-column responsive card grid, color-coded category badges (AMB/GER/RES/USM/TRI)
- **Case files**: Each case is a single `.html` file that works standalone in any browser
- **Self-contained files**: Styles are duplicated inline in each HTML file for portability

### Dashboard Features (index.html)

- Real-time search with French diacritics normalization (NFD decomposition)
- Category filter tabs with ARIA accessibility (tablist, aria-selected)
- Dynamic card count that updates on filter/search
- 3-column responsive grid (1 col on mobile, 2 on tablet, 3 on desktop)
- Sections hide entirely when no cards match; "Aucun résultat" shown when nothing matches
- Sticky toolbar that stays at top when scrolling

### Scoring Structure (Individual Cases)

Each evaluation grid is divided into sections (anamnesis, clinical reasoning, communication) with:
- Criteria rows with radio buttons for point assignment
- Sub-criteria with checkboxes for detail tracking
- Patient responses shown in blue, example phrases in green
- Section percentage scores and global grade in summary panel

## Deployment

- **Server**: `python3 -m http.server 5000 --bind 0.0.0.0`
- **Deployment type**: Static (publicDir: ".")
- **No backend, no database, no authentication**

## External Dependencies

None — all files are fully self-contained with no external CSS frameworks, JavaScript libraries, or API integrations. The only external resource is Google Fonts (Inter) loaded in `index.html`.
