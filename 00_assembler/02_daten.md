## 1. Direkte Daten:

- `db`: Deklariert Byte-Daten (1 Byte).
- `dw`: Deklariert Wort-Daten (2 Bytes).
- `dd`: Deklariert Doppelwort-Daten (4 Bytes).
- `dq`: Deklariert Quadword-Daten (8 Bytes).

Beispiel:
```assembly
my_byte db 10      ; Byte-Deklaration
my_word dw 1234    ; Wort-Deklaration
my_dword dd 123456 ; Doppelwort-Deklaration
my_qword dq 1234567890123456 ; Quadword-Deklaration
```

## 2. Daten mit Initialisierung:

- `db`, `dw`, `dd`, `dq` gefolgt von einer Liste von Werten in geschweiften Klammern `{}`.

Beispiel:
```assembly
my_array db {1, 2, 3, 4, 5} ; Initialisierte Byte-Liste
my_values dd {100, 200, 300} ; Initialisierte Doppelwort-Liste
```

## 3. Reservieren von Speicher:

- `resb`: Reserviert eine bestimmte Anzahl von Bytes.
- `resw`: Reserviert eine bestimmte Anzahl von Worten.
- `resd`: Reserviert eine bestimmte Anzahl von Doppelwörtern.
- `resq`: Reserviert eine bestimmte Anzahl von Quadwörtern.

Beispiel:
```assembly
buffer resb 1024    ; Reserviert 1024 Bytes für einen Puffer
data_array resd 100 ; Reserviert Platz für ein Array von 100 Doppelwörtern
```

Diese Befehle ermöglichen es dem Programmierer, Speicherbereiche für verschiedene Zwecke zu definieren und zu reservieren. Die genaue Syntax und Verwendung kann je nach Assemblersprache variieren.