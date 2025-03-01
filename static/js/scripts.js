<<<<<<< HEAD
const sidePane = document.getElementById('sidePane');

    // Show the pane when the mouse is on the left edge
    document.addEventListener('mousemove', (event) => {
        if (event.clientX < 50) { // Mouse near the left edge
            sidePane.style.left = '0';
        } else if (event.clientX > 300) { // Mouse away from the pane
            sidePane.style.left = '-300px';
        }
    });
=======
$(document).ready(function () {
    const $sidePane = $('#sidePane');
    const $movieSelect = $('#movieSelect');

    // Show the loader initially
    $('#loader').show();

    // Show/hide the side pane when hovering on the left edge
    $(document).mousemove(function (event) {
        if (event.clientX < 50) { // Mouse near the left edge
            $sidePane.css('left', '0');
        } else if (event.clientX > 300) { // Mouse away from the pane
            $sidePane.css('left', '-300px');
        }
    });

    // Initialize Select2 with a proper placeholder
    $movieSelect.select2({
        placeholder: "Search for a movie...",
        allowClear: true,
        dropdownAutoWidth: true
    });

    // Ensure no movie is preselected
    setTimeout(() => {
        $movieSelect.val(null).trigger('change');
    }, 100);

    // Fetch movie list and populate dropdown
    function loadMovies() {
        $.ajax({
            url: '/get_movies', // Fetch from Flask API
            type: 'GET',
            dataType: 'json',
            success: function (movies) {
                $movieSelect.empty(); // Clear existing options
                
                // Add an empty option for placeholder
                $movieSelect.append('<option></option>');

                // Populate dropdown with movies
                $.each(movies, function (index, movie) {
                    $movieSelect.append($('<option>', {
                        value: movie,
                        text: movie
                    }));
                });

                // Ensure placeholder is properly set
                $movieSelect.val(null).trigger('change');
            },
            error: function () {
                console.error("Error fetching movies.");
            }
        });
    }

    // Load movies when the page is ready
    loadMovies();

    // Hide loader when everything is fully loaded (including images)
    $(window).on('load', function () {
        $('#loader').fadeOut();
    });

    // Handle recommendation button click
    $('#recommendButton').click(function () {
        let selectedMovie = $movieSelect.val();
        if (selectedMovie) {
            alert("You selected: " + selectedMovie);
        } else {
            alert("Please select a movie.");
        }
    });

    // Close dropdown when clicking outside
    $(document).on('click', function (e) {
        if (!$(e.target).closest('.select2-container').length) {
            $movieSelect.select2('close');
        }
    });
});
>>>>>>> master
