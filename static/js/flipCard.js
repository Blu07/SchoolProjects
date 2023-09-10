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
        count = 0
    }
}