// Set current year in the footer.
(function () {
  var y = document.getElementById('year');
  if (y) { y.textContent = String(new Date().getFullYear()); }

  // Close the mobile nav after a link is tapped.
  var toggle = document.getElementById('nav-toggle');
  if (toggle) {
    var links = document.querySelectorAll('.nav-links a');
    links.forEach(function (a) {
      a.addEventListener('click', function () { toggle.checked = false; });
    });
  }
})();
