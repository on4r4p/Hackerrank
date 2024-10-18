'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    const A = ["a","e","i","o","u"];
    const B = ["b","c","d","f","g"];
    const C = ["h","j","k","l","m"];
    const D = ["n","p","q","r","s","t","v","w","x","y","z"];
    let firstL = s.charAt(0);

    switch (true) {
    case A.includes(firstL): 
        letter = "A";
        break;
    case B.includes(firstL): 
        letter = "B";
        break;
    case C.includes(firstL): 
        letter = "C";
        break;
    case D.includes(firstL): 
        letter = "D";
        break;
    }
    
    return letter;
}


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}
