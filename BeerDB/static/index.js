// Retreive all beers in the database.
function getAllBeers() {
  $('singleBeer').hide();
  var beerList = $('<ul></ul>');
  $.get("http://localhost:5000/beers/all")
  .done(function(data) {
    data = jQuery.parseJSON(data);
    for (var i=0, n=data.length; i<n; i++) {
      beerList.append($('<li></li>').text(data[i].name))
    }
  });
  $(".beerList").show().append(beerList);
};

// Displays a specific beer object to the user.
function displayBeer(beer) {
  console.log(beer);
  $(".beerList").hide();
  // Assign beer display stuff
  $('.singleBeer').show();
};

// Look for a specific beer in database.
function findBeer(beername) {
  beername = beername || $('#searchBox').val();
  $(".beerList").hide();
  $.get("http://localhost:5000/beers", { beername: JSON.stringify(beername) })
  .done(function(data) {
    console.log(data);
    displayBeer(jQuery.parseJSON(data));
  });
};

// Add a new beer to the database.
function addBeer() {

};
