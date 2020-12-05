var toggleButton = document.querySelector(".toggle-button");

var toggleButtonCircle = document.querySelector(".toggle-button-circle");

var basicPriceValue = document.querySelector("#basic-price");

var professionalPriceValue = document.querySelector("#professional-price");

var masterPriceValue = document.querySelector("#master-price");

function switchValues() {
  if (toggleButtonCircle.classList.contains("toggle-button-monthly")) {
    basicPriceValue.innerHTML = "<span class='dollar-sign'>$ </span>19.99";
    professionalPriceValue.innerHTML = "<span class='dollar-sign'>$ </span>24.99";
    masterPriceValue.innerHTML = "<span class='dollar-sign'>$ </span>39.99";
  } else {
    basicPriceValue.innerHTML = "<span class='dollar-sign'>$ </span>199.99";
    professionalPriceValue.innerHTML = "<span class='dollar-sign'>$ </span>249.99";
    masterPriceValue.innerHTML = "<span class='dollar-sign'>$ </span>399.99";
  };
}

toggleButton.addEventListener("click", function() {

  toggleButtonCircle.classList.toggle("toggle-button-monthly");

  switchValues();
});

toggleButton.addEventListener("keydown", function(event) {
  console.log(event.key);
  if (event.key == "Enter") {
    
    toggleButtonCircle.classList.toggle("toggle-button-monthly");

    switchValues();
  };
});
