document.getElementById("search_categories").addEventListener("change", function () {
  const table = document.getElementById("crops");
  if (this.value !== "none") {
    table.style.display = "table"; // Show the table
  } else {
    table.style.display = "none"; // Hide the table if no location is selected
  }
});