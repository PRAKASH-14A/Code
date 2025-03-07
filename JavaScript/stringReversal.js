function reverseString(str) {
    let reversed = "";
    for (let i = str.length - 1; i >= 0; i--) { // Loops manually
        reversed += str[i]; // String concatenation in loop (slow in JS)
    }
    return reversed;
}

console.log(reverseString("JavaScript"));
