# l5r-compendium

A small Python script that generates a **custom compendium module for the L5R 5e (`l5r5e`) system on Foundry VTT v13**.

It does the same job as Vlyan's excellent
[L5R5e Custom Compendium Maker](https://vly.yn.lu/l5r5e-custom-compendium-maker/), but reads the
data from a **PostgreSQL database** instead of Excel files. I wrote it for personal use because I
found a database easier to maintain than spreadsheets.

> ⚠️ **Status: personal project, unfinished and not usable as-is.**
> The database with the actual content is **not included** in this repository. Without your own
> database populated with data, the script has nothing to generate. Feel free to reuse the
> structure with your own data source.

## What it generates

Running the script creates a Foundry module in `output/l5r5e-custom-compendiums/`, relative to the directory you run it from (so `src/output/` with the commands below):

```
l5r5e-custom-compendiums/
├── module.json            # Foundry v13 module manifest (requires the l5r5e system and Babele)
├── register-babele.js     # Registers the translation files with Babele
└── compendiums/en/        # One Babele JSON file per compendium
```

The JSON files use the [Babele](https://foundryvtt.com/packages/babele) translation format to fill
in the `l5r5e` system compendiums, overriding fields like `system.description` and
`system.source_reference`. Files generated:

- `l5r5e.core-armors.json`, `l5r5e.core-weapons.json`, `l5r5e.core-items.json`,
  `l5r5e.core-item-patterns.json`, `l5r5e.core-properties.json`
- `l5r5e.core-bonds.json`, `l5r5e.core-titles.json`, `l5r5e.core-signature-scrolls.json`,
  `l5r5e.core-celestial-implement-boons.json`
- `l5r5e.core-techniques-<type>.json` (one per technique type: kata, kiho, shuji, etc.)
- `l5r5e.core-peculiarities-{distinctions,adversities,passions,anxieties}.json`
- `l5r5e.core-journal-{conditions,opportunities,terrain-qualities,school-curriculum}.json`

## How it works

```
PostgreSQL ──► SQLAlchemy models ──► services ──► generators ──► Babele JSON + module.json
              (src/db/models)       (src/services) (src/generators)  (output/)
```

- `src/db/models/` holds the **table structure**. Each model maps one table (`l5r_books`,
  `l5r_techniques`, `l5r_weapons`, …). Every content table references `l5r_books.code`, and that
  table holds the book's `babele_key` used in `source_reference`.
- `src/services/` has simple read services (`get_all()`) for each model.
- `src/generators/` turns rows into Babele entries, building the HTML descriptions.
- `src/utils/module_builder.py` writes the module skeleton (`module.json`, `register-babele.js`).

## Usage (if you have your own database)

Requires Python 3.11+.

1. Create the tables in PostgreSQL following the models in `src/db/models/`
   (`db.base.init_db()` can create them with `Base.metadata.create_all`) and populate them.
2. Create a `.env` file at the repository root:

   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=l5r
   DB_USER=postgres
   DB_PASS=secret
   ```

3. Install the dependencies and run the generator from `src/`:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cd src && python main.py
   ```

4. Copy `src/output/l5r5e-custom-compendiums/` into your Foundry `Data/modules/` folder and enable it
   in your world (together with Babele).

## Development

The `Makefile` has formatting and lint shortcuts: `make fix`, `make lint`, `make clean`.
Dependencies are managed with pip-tools (`requirements.in` → `requirements.txt`).

## Credits

Module format and inspiration: [Vlyan](https://ko-fi.com/vlyan), author of the `l5r5e` system and
the L5R5e Custom Compendium Maker.
