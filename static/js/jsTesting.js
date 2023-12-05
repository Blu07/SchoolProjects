antallTimer = 2;
antallMinutter = 30;
antallSekunder = 17;

let tiderListe = [antallTimer, antallMinutter, antallSekunder];
timeInString = tiderListe.join(":");

console.log("Oppgave 4\n" +
    timeInString + " er " +
    (
        antallTimer * 3600 +
        antallMinutter * 60 +
        antallSekunder
    ) + " sekunder."
);




sekunder = 9017;
tidIgjen = sekunder;

antallTimer = Math.floor(sekunder / 3600);
tidIgjen -= antallTimer * 3600; 
antallMinutter = Math.floor((tidIgjen % (antallTimer*3600)) / 60);
tidIgjen -= antallMinutter * 60;
antallSekunder = tidIgjen;

tiderListe = [antallTimer, antallMinutter, antallSekunder];
timeInString = tiderListe.join(":");

console.log("Oppgave 5\n" +
    sekunder + " sekunder er " + timeInString
);




let hoydeCM = 90;
let grenseCM = 100;

if (hoydeCM >= grenseCM) {
    console.log("Du kan ta berg-og-dal-banen.");
}
else {
    console.log("Du er dessverre for lav til å ta berg-og-dal-banen.");
};


mainPart = document.getElementById("main").innerHTML

mainPart = antallSekunder;



let terning_kast = Math.floor((Math.random() * 20) + 1);

console.log(terning_kast);


for (let i = 2; i <= 100; i += 2) {
    console.log(i);
}


let out = ''
for (let i = 1; i <= 100; i++) {
    out = ''
    if (i % 3 == 0) {
        out += 'Fizz'
    };
    if (i % 5 == 0) {
        out += 'Buzz'
    }
    if (!out) {
        console.log(i)
        continue
    }
    console.log(out)
}


