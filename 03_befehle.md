## 1. Datenübertragungsbefehle:

- `mov`: Bewegt Daten von einer Quelle in ein Ziel.
- `push`: Legt einen Wert auf den Stapel.
- `pop`: Nimmt einen Wert vom Stapel und speichert ihn in einem Register.
- `lea`: Lädt die effektive Adresse einer Speicheradresse in ein Register.
- `xchg`: Tauscht den Inhalt von zwei Operanden.

## 2. Arithmetische und logische Befehle:

- `add`, `sub`, `mul`, `div`: Führen arithmetische Operationen durch (Addition, Subtraktion, Multiplikation, Division).
- `inc`, `dec`: Inkrementiert bzw. dekrementiert den Wert eines Registers oder Speicherbereichs um 1.
- `and`, `or`, `xor`, `not`: Führen logische Operationen durch (AND, OR, XOR, NOT).
- `cmp`: Vergleicht zwei Operanden.

## 3. Sprungbefehle:

- `jmp`: Unbedingter Sprung zu einer Speicheradresse.
- `je`, `jne`, `jz`, `jnz`, `jl`, `jle`, `jg`, `jge`: Bedingte Sprünge basierend auf einem Vergleich.
- `call`: Ruft eine Unterfunktion auf.
- `ret`: Rückkehr von einer Unterfunktion.

## 4. Speicherzugriffsbefehle:

- `mov`: Bewegt Daten zwischen Registern und Speicher.
- `load`: Lädt Daten aus dem Speicher in ein Register.
- `store`: Speichert Daten aus einem Register im Speicher.

## 5. Systemaufrufe und Interrupts:

- `int`: Ruft einen Interrupt auf.
- `syscall`: Ruft einen Systemaufruf auf (in 64-Bit-Modus).

## 6. Sonstige Befehle:

- `nop`: Keine Operation (führt keine Aktion aus).
- `hlt`: Haltebefehl (hält die CPU an).
- `nop`: Führt keine Operation aus.

Dies ist nur ein Überblick über einige der grundlegenden Assemblerbefehle. Es gibt viele weitere Befehle und Variationen, die in verschiedenen Architekturen und Assemblersprachen existieren können. Es ist wichtig, die spezifische Dokumentation für die verwendete Architektur zu konsultieren, um eine vollständige Liste der verfügbaren Befehle zu erhalten.