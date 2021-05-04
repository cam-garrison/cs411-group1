let autoComplete;
    function activatePlacesSearch() {
        autoComplete = new google.maps.places.Autocomplete(document.getElementById('searchTerm'));
        autoComplete.addListener('placeChanged', onPlaceChanged);
    }
    function onPlaceChanged() {
        var place = autoComplete.getPlace();

        if (!place.geometry) {
            // no prediction selected; reset input field
            document.getElementById('searchTerm').placeholder = 'Enter a place';
        } else {
            // display details about valid place
            document.getElementById('details').innerHTML = place.name;
        }
    }