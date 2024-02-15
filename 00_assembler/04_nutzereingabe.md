```
section .data
    msg db 0xA, 'Enter a message: ', 0

section .bss
    buffer resb 255

section .text
    global _start

_start:
    ; Display message to enter a message
    mov eax, 4          ; sys_write syscall number
    mov ebx, 1          ; file descriptor (stdout)
    mov ecx, msg        ; pointer to the message
    mov edx, 18         ; message length
    int 0x80            ; call kernel

    ; Read user input
    mov eax, 3          ; sys_read syscall number
    mov ebx, 0          ; file descriptor (stdin)
    mov ecx, buffer     ; pointer to buffer
    mov edx, 255        ; buffer size
    int 0x80            ; call kernel

    ; Display the input message
    mov eax, 4          ; sys_write syscall number
    mov ebx, 1          ; file descriptor (stdout)
    mov ecx, buffer     ; pointer to the input buffer
    int 0x80            ; call kernel

    ; Exit the program
    mov eax, 1          ; sys_exit syscall number
    xor ebx, ebx        ; exit status
    int 0x80            ; call kernel

```