// function to decide whether the submit button should work or not
// so that 'Choose an area...' cannot be selected and cause an error
function formValidate(formName) {
  let selectedValue = document.getElementById(formName).value;
  // check if the selected value is "choose" and prevent/allow submit
  if (selectedValue === "choose") {
    return false;
  }
  return true;
}

// Event listener to enable/disable the submit button on the wall search
document
  .getElementById("wall-search-inputs")
  .addEventListener("change", function () {
    let submitButton = document.getElementById("submitButton");
    let selectedValue = this.value;

    submitButton = selectedValue === "choose";
  });

// Event listener to enable/disable the submit button on the class search
document
  .getElementById("class-search-inputs")
  .addEventListener("change", function () {
    let submitButton = document.getElementById("submitButton");
    let selectedValue = this.value;

    submitButton = selectedValue === "choose";
  });

// Event listener to enable/disable the submit button on the club search
document
  .getElementById("club-search-inputs")
  .addEventListener("change", function () {
    let submitButton = document.getElementById("submitButton");
    let selectedValue = this.value;

    submitButton = selectedValue === "choose";
  });
