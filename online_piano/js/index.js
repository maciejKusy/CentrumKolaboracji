
(function(){
  //creating tonation display starting values and vars

  var selectedTonationNumber = 4;

  var selectedTonation = null;

  function defineTonation() {
    selectedTonation = "C" + selectedTonationNumber + "-" + "C" + (selectedTonationNumber + 2);
  }

  defineTonation();

  var tonationDisplay = document.querySelector("#tonation-display");

  tonationDisplay.textContent = selectedTonation;

  //creating function to refresh and update the tonation and the tonation display

  function tonationDisplayRefresh() {
    defineTonation();

    tonationDisplay.textContent = selectedTonation;
  }

  //creating tonation display logic - event listener on tonation control container

  var tonationToggleContainer = document.querySelector("#tonation-control");

  tonationToggleContainer.addEventListener("click", function(event) {

    var buttonPressed = event.target;

    if (event.target.id == "tonation-down") {
      if (selectedTonationNumber > 3) {
        selectedTonationNumber -= 1;

        tonationDisplayRefresh();
      }
    }
    else if (event.target.id == "tonation-up") {
      if (selectedTonationNumber < 4) {
        selectedTonationNumber += 1;

        tonationDisplayRefresh()
      }
    }
  });

  //creating the function that selects the appropriate sound file and plays it
  //when event triggered

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

      this.setAttribute("data-clicked", true);

      playSound(this.dataset.key);
    });
  }


  document.addEventListener("mouseup", function() {
    if (document.querySelectorAll('[data-clicked=true]').length > 0) {
      var keyCurrentlyClicked = document.querySelector('[data-clicked=true]');

      keyCurrentlyClicked.setAttribute("data-clicked", false);

      if (keyCurrentlyClicked.classList.contains("white-key")) {
        keyCurrentlyClicked.classList.remove("pressed-white");
      } else {
        keyCurrentlyClicked.classList.remove("pressed-black");
      }
    }
  });

  //creating the loop adding event listener adjusting black keys styling
  //when clicked

  var listOfBlackKeys = document.getElementsByClassName("black-key");

  var numberOfBlackKeys = listOfBlackKeys.length;

  for (var i = 0; i < numberOfBlackKeys; i++) {

    var currentBlackKey = listOfBlackKeys[i];

    currentBlackKey.addEventListener("mousedown", function(event) {
      event.stopPropagation();

      this.classList.add("pressed-black");

      this.setAttribute("data-clicked", true);

      playSound(this.dataset.key);
    });
  }

  //creating event listeners adjusting the styling of keys when
  //when keyboard key corresponding to a given piano key is pressed and released

  document.addEventListener("keydown", function(event) {

    var currentKey = event.key;

    var correspondingPianoKeyElement = document.querySelector(`[data-key="${currentKey}"]`);

    if (event.repeat) {return;}

    if (correspondingPianoKeyElement) {
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

    var correspondingPianoKeyElement = document.querySelector(`[data-key="${currentKey}"]`);

    if (correspondingPianoKeyElement) {
      if (correspondingPianoKeyElement.classList.contains("white-key")) {
        correspondingPianoKeyElement.classList.remove("pressed-white");
      }
      else {
        correspondingPianoKeyElement.classList.remove("pressed-black");
      }
    }
  });
})();
