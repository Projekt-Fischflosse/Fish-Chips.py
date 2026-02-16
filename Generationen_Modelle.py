import sqlite3
from datetime import datetime

#Datenbank erstellen
conn = sqlite3.connect('fish_and_chips.db')
cursor = conn.cursor()

#egemen erstellt jetzt eine Tabelle für die ersten 10 Fragen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        difficulty TEXT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        explanation TEXT,
        created_date TEXT
    )
''')

print("✅ Tabelle erstellt!")

fragen = [
    ('Computergenerationen', 'Welche Technologie dominierte die 1. Computergeneration?', datetime.now().isoformat()),
    ('Computergenerationen', 'Was war ein typisches Problem der 1. Generation?', datetime.now().isoformat()),
    ('Computergenerationen', 'Welche Technologie kennzeichnet die 2. Generation?', datetime.now().isoformat()),
    ('Computergenerationen', 'Warum waren Computer der 2. Generation besser?', datetime.now().isoformat()),
    ('Computergenerationen', 'Was prägte die 3. Generation?', datetime.now().isoformat()),
    ('Computergenerationen', 'Was ist eine integrierte Schaltung (IC)?', datetime.now().isoformat()),
    ('Computergenerationen', 'Welche Innovation definierte die 4. Generation?', datetime.now().isoformat()),
    ('Computergenerationen', 'Was wurde ab der 4. Generation massentauglich?', datetime.now().isoformat()),
    ('Computergenerationen', 'Was ist typisch für die 5. Generation?', datetime.now().isoformat()),
    ('Computergenerationen', 'Welche Reihenfolge ist korrekt?', datetime.now().isoformat()),
]

#fragen einfügen oder so wie mans sagen soll
for f in fragen:
    cursor.execute('''
        INSERT INTO fragen 
        (category, question, created_date)
        VALUES (?, ?, ?)
    ''', f)

conn.commit()
conn.close()

print(f"🐟🍟 {len(fragen)} Fragen hinzugefügt!")
