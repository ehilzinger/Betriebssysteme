# Einführung in die Assemblerprogrammierung

Willkommen zu unserer Einführung in die Assemblerprogrammierung! In diesem Tutorial werden wir die Grundlagen der Assemblerprogrammierung auf einfache Weise erklären.

## Online-Compiler

Verfügbar [hier](https://onecompiler.com/assembly/424h8rhu5) 

## Was ist Assembler?

Assembler ist eine Programmiersprache, die eng mit der Maschinensprache des Computers verbunden ist. Im Gegensatz zu Hochsprachen wie C oder Python, die von Menschen leicht verstanden werden können, ist Assembler viel näher an der Hardware des Computers. Jede Anweisung in einem Assemblerprogramm entspricht im Wesentlichen einer Anweisung, die direkt von der CPU des Computers ausgeführt wird.

## Warum Assembler?

Obwohl Assembler weniger intuitiv ist als Hochsprachen, bietet es einige Vorteile:
- Präzise Kontrolle über Hardware-Ressourcen.
- Hohe Leistung und Geschwindigkeit.
- Nützlich für die Entwicklung von Betriebssystemen, Treibern und eingebetteten Systemen.

## Beispielprogramm: Addition von Zahlen

Um den Einstieg in die Assemblerprogrammierung zu erleichtern, betrachten wir ein einfaches Beispielprogramm, das zwei Zahlen addiert.

```assembly
section .data
    zahl1 dd 10    ; Erste Zahl
    zahl2 dd 20    ; Zweite Zahl
    summe dd 0     ; Variable für das Ergebnis

section .text
    global _start

_start:
    ; Addition
    mov eax, [zahl1]    ; Lade die erste Zahl in das Register eax
    add eax, [zahl2]    ; Addiere die zweite Zahl zu eax
    mov [summe], eax    ; Speichere das Ergebnis in der Variable summe

    ; Programmende
    mov eax, 1          ; Systemaufrufnummer für sys_exit
    xor ebx, ebx        ; Exit-Code 0
    int 0x80            ; Aufruf des Kernels
```

## Schritt-für-Schritt-Erklärung

### Datenbereich (`.data`):
- Hier werden die Daten definiert, die im Programm verwendet werden.
- `zahl1` und `zahl2` sind die beiden Zahlen, die wir addieren möchten.
- `summe` ist die Variable, in der das Ergebnis gespeichert wird.

### Codebereich (`.text`):
- Hier befindet sich der eigentliche Programmcode.
- `mov`, `add` und `int` sind Befehle der x86-Assemblerbefehlssatzes.
- `eax`, `ebx` sind Register, die zum Speichern von Daten verwendet werden.

## Zusammenfassung

In diesem Tutorial haben wir die Grundlagen der Assemblerprogrammierung kennengelernt und ein einfaches Beispielprogramm zur Addition von Zahlen betrachtet. Wir haben auch Markdown-Syntax für die Formatierung dieses Tutorials verwendet. Jetzt sind Sie bereit, Ihre Reise in die Welt der Assemblerprogrammierung zu beginnen!