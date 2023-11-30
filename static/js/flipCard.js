var greetings= ['Hi',
                'Hello',
                'Welcome',
                'Good to see you'];
var count = 0;

function newGreet() {
    let len = greetings.length;
    document.getElementById('greeting').innerHTML = greetings[count % len];
    
    if (count < len - 1) {
        count++;
    }
    else {
        count = 0;
    }
    return true;
}



function getRandomIndex(highest) {
    let delta = 0.00001
    return Math.floor(Math.min(Math.random() * highest, highest - delta));
}

function randomGreet(greets) {
    let greeting = greets[getRandomIndex(highest=greets.length)];
    
    console.log(greeting);
}

randomGreet(greetings)