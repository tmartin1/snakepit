// Retreive all beers in the database.
function getAllBeers() {
  $('singleBeer').hide();
  var beerList = $('<ul></ul>');
  var allBeers = $.get("http://localhost:5000/beers/all", function(data) {
    data = jQuery.parseJSON(data);
    console.log(data);
    for (var i=0, n=data.length; i<n; i++) {
      beerList.append($('<li></li>').text(data[i].name))
    }
  });
  $(".beerList").show().append(beerList);
};

// Displays a specific beer object to the user.
function displayBeer(beer) {
  $(".beerList").hide();
  // Assign beer display stuff
  $('.singleBeer').show();
};

// Look for a specific beer in database.
function findBeer() {
  $(".beerList").hide();
  beer = jQuery.parseJSON()
};

// Add a new beer to the database.
function addBeer() {

};
