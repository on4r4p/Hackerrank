

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    //s.split('').forEach(letter => console.log(letter));
    //console.log(s)
    //for (let i = 0; i < materials.length; i++) {
 //    console.log(materials[i]);
 //}
     const vowels = ["a","e","i","o","u"]

     let vowels_output = "";
     let conson_output = "";
     
     for (let i = 0; i < s.length; i++){
         if (vowels.includes(s[i])){
             vowels_output += s[i];}
         else{
             conson_output += s[i];}
         }
     //console.log(vowels_ouput);
     //console.log(consonants_output);
     vowels_output.split('').forEach(char => console.log(char));
     conson_output.split('').forEach(char => console.log(char));      
     }



