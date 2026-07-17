# Database

This folder contains the original database backups or database exports provided by the client during the **Data Discovery** phase.

The files in this folder represent the primary source of operational data and should remain unchanged throughout the project.

## Typical Contents

- SQL dump files (`.sql`)
- Database backup files
- Database schema exports

## Example

- `swiftmart_db.sql`

> These files are considered **read-only source data**.

---

## DAPM Rule

Files in this folder represent the original data received from the client.

Do **not** modify these files directly. Any cleaned, transformed, or derived datasets should be stored separately under `data/processed/`.