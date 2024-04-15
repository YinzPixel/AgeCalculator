function submitButton() {
  // set error flags, this way we can see if any other fields are also incorrect.
  let error = false;
  const today = moment();

  // check year
  let year = document.getElementById("year").value.replace(/^0+/, "");

  if (parseInt(year) > today.year()) {
    alert("Year Must be in the past.");
    document.querySelector("#year-label").classList.add("error-labels");
    document.querySelector("#year").className = "input-field-error";
    document.querySelector("#error-year").style.visibility = "visible";
    error = true;
  }

  // check month
  let month = document.getElementById("month").value.replace(/^0+/, "");

  if (parseInt(month) < 1 || parseInt(month) > 12) {
    alert("Please enter a valid month.");
    document.querySelector("#month-label").classList.add("error-labels");
    document.querySelector("#month").className = "input-field-error";
    document.querySelector("#error-month").style.visibility = "visible";
    error = true;
  }

  // check day
  const daysInMonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
  };

  let day = document.getElementById("day").value.replace(/^0+/, "");

  if (parseInt(day) < 1 || parseInt(day) > daysInMonth[parseInt(month)]) {
    alert("Please enter a valid day.");
    document.querySelector("#day-label").classList.add("error-labels");
    document.querySelector("#day").className = "input-field-error";
    document.querySelector("#error-day").style.visibility = "visible";
    error = true;
  }

  const inputDate = moment(year + "-" + month + "-" + day, "YYYY-MM-DD");

  // last check to make sure date is valid
  if (!inputDate.isValid()) {
    alert("Please enter a valid date.");
    document.querySelector("#year-label").classList.add("error-labels");
    document.querySelector("#year").className = "input-field-error";
    document.querySelector("#error-year").style.visibility = "visible";
    document.querySelector("#month-label").classList.add("error-labels");
    document.querySelector("#month").className = "input-field-error";
    document.querySelector("#error-month").style.visibility = "visible";
    document.querySelector("#day-label").classList.add("error-labels");
    document.querySelector("#day").className = "input-field-error";
    document.querySelector("#error-day").style.visibility = "visible";
    return;
  }

  // if error, do not calculate
  if (error) {
    return;
  }

  // calculate the time difference
  const timeDifference = today.diff(inputDate);

  var years = moment.duration(timeDifference).years();

  var months = moment.duration(timeDifference).months();

  var days = moment.duration(timeDifference).days();

  console.log(years, months, days);

  // update the output
  document.getElementById("output-year").innerHTML = years;
  document.getElementById("output-month").innerHTML = months;
  document.getElementById("output-day").innerHTML = days;
}

// Reset the error boxes on click

function clickDay() {
  document.querySelector("#day-label").classList.remove("error-labels");
  document.querySelector("#day").className = "input-field";
  document.querySelector("#error-day").style.visibility = "hidden";
}

function clickMonth() {
  document.querySelector("#month-label").classList.remove("error-labels");
  document.querySelector("#month").className = "input-field";
  document.querySelector("#error-month").style.visibility = "hidden";
}

function clickYear() {
  document.querySelector("#year-label").classList.remove("error-labels");
  document.querySelector("#year").className = "input-field";
  document.querySelector("#error-year").style.visibility = "hidden";
}
