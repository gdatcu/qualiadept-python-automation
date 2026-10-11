"""
=============================================================================
QualiAdept LMS - Python for QA Automation Portfolio
=============================================================================
Challenge : Provocarea 1: Curățarea și Validarea Prețului din Coș
Session   : Sesiunea 1: Primii Pași în Python & Tipuri de Date Fundamentale
Challenge ID: py-s1-c1
Completed : 2026-10-11
Status    : PASSED (Verified via in-browser Pyodide test suite)
Platform  : https://qualiadept.eu
=============================================================================
"""

def parse_cart_price(raw_text: str) -> float:
    # 1. Curățăm spațiile albe de la început și sfârșit (inclusiv \n)
    cleaned = raw_text.strip()
    
    # 2. Eliminăm etichetele text, indiferent de spațiile din jurul lor
    cleaned = cleaned.replace("Preț Total:", "").replace("RON", "")
    
    # 3. Eliminăm toate spațiile rămase în interior pentru a izola doar numărul
    cleaned = cleaned.replace(" ", "")
    
    # 4. Transformăm formatul RO (2.450,50) în format standard Python (2450.50)
    normalized = cleaned.replace(".", "").replace(",", ".")
    
    return float(normalized)

# Testare:
print(parse_cart_price(" Preț Total: 2.450,50 RON \n"))  # Output: 2450.5
