// Først litt leking med lister
// let drikke = ["kaffe", "te", "cola", "melk"];
// let mat = ["taco", "pizza", "hamburger", "pølse"];
// let matListe2 = ["Hei", "På", "Deg"];
// mat.splice(2, 0, matListe2[2]);

// console.log(drikke, mat);


// Oppgave 1
// Lag en array med tallene 0, 1, 2, 3, 4, 6, 7, 8, 9 og 10 og gi den et passende navn.

let liste = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10];


// Oppgave 2
// Skriv ut alle partallene fra arrayen i konsollen.

for (const num in liste) {
    if (num % 2 === 0) {
        console.log(num);
    }
}


// Oppgave 3
// Lag arrayen let tall = [2, 4, 6, 8] ;.

let tall = [2, 4, 6, 8];

// a)	Bruk metodene vi har sett på, og gjør om arrayen tall til [4, 6] .

tall.shift();
tall.pop();

// b)	Legg til tallet 5 mellom tallene 4 og 6, slik at arrayen nå inneholder [4, 5, 6] .

tall.splice(1, 0, 5);

// c)	Gjør om arrayen slik at den inneholder [3, 4, 5, 6, 7] .

tall.unshift(3);
tall.push(7);

// d)	Gjør om arrayen slik at den inneholder ["tre", 4, "fem", 6, "syv"] .

bokstavNavn = ["null", "en", "to", "tre", "fire", "fem", "seks", "syv", "åtte", "ni", "ti"];

tall.forEach(function (item, index) {
    // Hvis oddetall
    if (item%2 == 1) {
        tall.splice(index, 1, bokstavNavn[item]);
    }
});


// e)   Vis veriden av tall i consollen.

console.log(tall);


// Oppgave 4
// Ta igjen utgangspunkt i arrayen du laget i forrige oppgave.

// a)	Hva tror du skjer hvis du skriver tall.indexOf(10) eller tall.lastIndexOf(10) ?
// 10 er ikke i listen 'tall', så jeg tror en error blir hevet.
// Jeg tester:
console.log(tall.indexOf(10));
// Resultatet er -1
// Dette er sikkert verdien man får om verdien ikke var i listen.


// b)	Prøv ut begge variantene og se hva du får. Hvordan tolker du resultatet?
// Jeg tror igjen at svaret blir -1, siden 10 fortsatt ikke er i listen.
// Jeg tester:
console.log(tall.lastIndexOf(10));
// Resultatet er -1.
