#Zwischenlager der ersten 10 Fragen mit Antworten und alles drum und dran 
#die ersten 10 fragen - computergenerationen vom Schreiber dem gEnIE

"""fragen = [
    #erste frage
    ( 'Computergenerationen',
    'Leicht',
    'Welche Technologie dominierte die 1. Computergeneration?',
    'Transistoren',              # A - wrong
    'Röhren/Vakuumröhren',      # B - richtig
    'Integrierte Schaltungen',  # C - wrong
    'Mikroprozessoren',         # D - wrong
    'b',  #weil b ja richtig ist
    'Die 1. Generation (1940-1956) nutzte Vakuumröhren du Hund.',
    datetime.now().isoformat()
    ),

    #zweite frage
    (
        'Computergenerationen',
        'Leicht',
        'Was war ein typisches Problem der 1. Generation?',
        'Zu klein',
        'Hohe Hitzeentwicklung',
        'Zu schnell',
        'Zu leise',
        'b',
        'Vakuumröhren erzeugten viel Wärme und fielen oft aus.',
        datetime.now().isoformat()
    ),
    
    #dritte frage
    (
        'Computergenerationen',
        'Leicht',
        'Welche Technologie kennzeichnet die 2. Generation?',
        'Vakuumröhren',
        'Transistoren',
        'Mikroprozessoren',
        'Künstliche Intelligenz',
        'b',
        'Die 2. Generation (1956-1963) nutzte Transistoren.',
        datetime.now().isoformat()
    ),
    
    #vierte frage
    (
        'Computergenerationen',
        'Mittel',
        'Warum waren Computer der 2. Generation besser?',
        'Größer und schwerer',
        'Kleiner, schneller, zuverlässiger',
        'Teurer',
        'Komplizierter',
        'b',
        'Transistoren waren kleiner, schneller und zuverlässiger als Röhren.',
        datetime.now().isoformat()
    ),
    
    #fünfte frage
    (
        'Computergenerationen',
        'Mittel',
        'Was prägte die 3. Generation?',
        'Vakuumröhren',
        'Transistoren',
        'Integrierte Schaltungen (ICs)',
        'Quantencomputer',
        'c',
        'Die 3. Generation (1964-1971) nutzte integrierte Schaltungen.',
        datetime.now().isoformat()
    ),
    
    #sechste frage
    (
        'Computergenerationen',
        'Mittel',
        'Was ist eine integrierte Schaltung (IC)?',
        'Ein einzelner Transistor',
        'Viele Komponenten auf einem Chip',
        'Eine Vakuumröhre',
        'Ein Kabel',
        'b',
        'ICs kombinieren viele Transistoren und Komponenten auf einem Chip.',
        datetime.now().isoformat()
    ),
    
    #siebte frage
    (
        'Computergenerationen',
        'Mittel',
        'Welche Innovation definierte die 4. Generation?',
        'Vakuumröhren',
        'Transistoren',
        'Integrierte Schaltungen',
        'Mikroprozessoren',
        'd',
        'Die 4. Generation (1971-heute) nutzt Mikroprozessoren.',
        datetime.now().isoformat()
    ),
    
    #achte frage
    (
        'Computergenerationen',
        'Leicht',
        'Was wurde ab der 4. Generation massentauglich?',
        'Großrechner',
        'Personal Computer (PCs)',
        'Rechenschieber',
        'Dampfmaschinen',
        'b',
        'PCs wurden durch Mikroprozessoren erschwinglich und verbreitet.',
        datetime.now().isoformat()
    ),
    
    #neunte frage
    (
        'Computergenerationen',
        'Schwer',
        'Was ist typisch für die 5. Generation?',
        'Vakuumröhren',
        'Transistoren',
        'Künstliche Intelligenz und parallele Verarbeitung',
        'Dampfbetrieb',
        'c',
        'Die 5. Generation fokussiert auf KI, neuronale Netze und parallele Verarbeitung.',
        datetime.now().isoformat()
    ),
    
    #zehnte frage
    (
        'Computergenerationen',
        'Mittel',
        'Welche Reihenfolge ist korrekt?',
        'Transistoren → Röhren → ICs → Mikroprozessoren',
        'Röhren → Transistoren → ICs → Mikroprozessoren',
        'ICs → Transistoren → Röhren → Mikroprozessoren',
        'Mikroprozessoren → ICs → Transistoren → Röhren',
        'b',
        'Korrekte Reihenfolge: 1. Röhren, 2. Transistoren, 3. ICs, 4. Mikroprozessoren.',
        datetime.now().isoformat()
    ),
]

# Alle Fragen in die Datenbank einfügen
for f in fragen:
    cursor.execute('''
        INSERT INTO questions 
        (category, difficulty, question, option_a, option_b, option_c, 
         option_d, correct_answer, explanation, created_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', f)

# Speichern und schließen
conn.commit()
conn.close()

print(f"🐟🍟 {len(fragen)} Fragen vom gEnIE erfolgreich hinzugefügt!")
print("✅ Fish & Chips Datenbank ist bereit!")"""

#Zwischenlager vom Skript zeige_data

"""import sqlite3

#datenbank öffnen
conn = sqlite3.connect('fish_and_chips.db')
cursor = conn.cursor()

#er soll die fragen holen
cursor.execute('SELECT * FROM questions')
alle_fragen = cursor.fetchall()

print(f"\n🐟🍟 Fish & Chips Quiz - {len(alle_fragen)} Fragen in der Datenbank\n")
print("="*70)

#zeige mir jede frage
for frage in alle_fragen:
    print(f"\n📝 Frage ID: {frage[0]}")
    print(f"📁 Kategorie: {frage[1]} | ⭐ Schwierigkeit: {frage[2]}")
    print(f"\n❓ {frage[3]}")
    print(f"   A) {frage[4]}")
    print(f"   B) {frage[5]}")
    print(f"   C) {frage[6]}")
    print(f"   D) {frage[7]}")
    print(f"\n✅ Richtige Antwort: {frage[8].upper()}")
    print(f"💡 Erklärung: {frage[9]}")
    print("-"*70)

conn.close()

print("\n Das sind alle Fragen vom gEnIE!\n")"""