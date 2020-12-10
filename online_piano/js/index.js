
var selectedTonation = "c4-c6";

function playSound(key) {

  var sound = new Audio("sounds/" + selectedTonation + "/" + key + ".wav");

  sound.play();
}

//creating the loop adding event listener adjusting white keys styling
//when clicked

var listOfWhiteKeys = document.getElementsByClassName("white-key");

var numberOfWhiteKeys = listOfWhiteKeys.length;

for (var i = 0; i < numberOfWhiteKeys; i++) {

  var currentWhiteKey = listOfWhiteKeys[i];

  currentWhiteKey.addEventListener("mousedown", function() {
    this.classList.add("pressed-white");

    playSound(this.id);
  });

  currentWhiteKey.addEventListener("mouseup", function() {
    this.classList.remove("pressed-white");
  });
}

//creating the loop adding event listener adjusting black keys styling
//when clicked

var listOfBlackKeys = document.getElementsByClassName("black-key");

var numberOfBlackKeys = listOfBlackKeys.length;

for (var i = 0; i < numberOfBlackKeys; i++) {

  var currentBlackKey = listOfBlackKeys[i];

  currentBlackKey.addEventListener("mousedown", function() {
    this.classList.add("pressed-black");

    playSound(this.id);
  });

  currentBlackKey.addEventListener("mouseup", function() {
    this.classList.remove("pressed-black");
  });
}

//creating event listeners adjusting the styling of keys when
//when keyboard key corresponding to a given piano key is pressed and released

var listOfRelevantKeys = ["q", "Q", "w", "W", "e", "r", "R", "t", "T", "y", "Y",
 "u", "i", "I", "o", "O", "p", "a", "A", "s", "S", "d", "D", "f", "g", "G", "h",
 "H", "j", "k", "K", "l", "L", ";", ":", "'"];

document.addEventListener("keydown", function(event) {

  var currentKey = event.key;

  var correspondingPianoKeyElement = document.getElementById(currentKey);

  if (event.repeat) {return;}

  if (listOfRelevantKeys.includes(currentKey)) {
    if (correspondingPianoKeyElement.classList.contains("white-key")) {
      correspondingPianoKeyElement.classList.add("pressed-white");

      playSound(currentKey);

    }
    else {
      correspondingPianoKeyElement.classList.add("pressed-black");

      playSound(currentKey);
    }
  }
});

document.addEventListener("keyup", function(event) {

  var currentKey = event.key;

  var correspondingPianoKeyElement = document.getElementById(currentKey);

  if (listOfRelevantKeys.includes(currentKey)) {
    if (correspondingPianoKeyElement.classList.contains("white-key")) {
      correspondingPianoKeyElement.classList.remove("pressed-white");
    }
    else {
      correspondingPianoKeyElement.classList.remove("pressed-black");
    }
  }
});
