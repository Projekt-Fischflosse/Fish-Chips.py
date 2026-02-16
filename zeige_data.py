import sqlite3

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

print("\n Das sind alle Fragen vom gEnIE!\n")