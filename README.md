# Roomly_match

A Python CLI tool that calculates compatibility between potential roommates based on customizable living preference criteria.

This project was developed to practice Object-Oriented Programming (OOP) principles, with a clear separation between the data model, business logic, and user interface.

## How It Works

Each person completes a questionnaire covering 8 roommate compatibility criteria:

* Organization
* Noise
* Pets
* Parties
* Smoking
* Schedule
* Cooking
* Cleaning

For each criterion, users choose one of the following responses:

* **F** – In Favor
* **S** – Against
* **I** – Indifferent

The system compares the responses of two people and calculates a **compatibility percentage**, highlighting:

* ✅ Shared preferences
* ❌ Conflicting preferences
* ➖ Neutral criteria (where at least one person is indifferent)

## Example Output

```text
==================================================
   MATCH: FRANCESCA vs LORENZO
==================================================
  Compatibility: 83.3%
  [+] Shared Preferences (5): Organization, Noise, Schedule, Cooking, Cleaning
  [-] Conflicts          (1): Smoking
  [/] Neutral            (2): Pets, Parties
--------------------------------------------------
```

## Running the Project

```bash
python roommate_match.py
```

From the main menu, you can:

1. Start a 1v1 compatibility match by creating two new profiles or selecting existing ones.
2. Exit the program.

## Code Structure

* `Preferenze` / `Persona` — Data model
* `CalcoloMatch` / `RisultatoMatch` — Compatibility calculation logic
* CLI functions (`crea_persona`, `menu_principale`, etc.) — User input and output handling

The application does not rely on mutable global variables. The application state (the list of people) is passed explicitly between functions.

## Project Status

Functional MVP.

Planned improvements:

* [ ] Multiple matching (one person vs. all registered profiles with a ranked compatibility list)
* [ ] Data persistence (save and load profiles from files)
* [ ] Weighted criteria (allow some criteria to have greater importance than others)

## Tech Stack

* Python 3
* Standard Library only (no external dependencies)

---

This project was built for learning purposes, focusing on Object-Oriented Programming (OOP), application logic, and CLI application design.
