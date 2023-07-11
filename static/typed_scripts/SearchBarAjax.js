var url = window.location.href;
var searchForm = document.getElementById('search-form');
var resultsBox = document.getElementById('results-box');
var searchInput = document.getElementById('search-input');
var csrf = document.getElementsByName('csrfmiddlewaretoken');
var sendSearchData = function (annotation) {
    $.ajax({
        type: 'POST',
        url: 'search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'annotation': annotation,
        },
        success: function (res) {
            console.log(res.data);
            var data = res.data;
            if (Array.isArray(data)) {
                console.log('we have an array');
                data.foreach(function (i) {
                    resultsBox += "\n                        <a href=\"\">\n                            <div class=\"row mt-2 mb-2\">\n                                <div class=\"col-10\">\n                                    <h5>".concat(annotation.name, "</h5>\n                                    <p class=\"text-muted\">").concat(annotation.account, "</p>\n                                </div>\n                            </div>\n                        </a>");
                });
            }
            else {
                if (searchInput.value.length > 0) {
                    resultsBox.innerHTML = "<b>$(data)</b>";
                }
                else {
                    resultsBox.classList.add('not-visible');
                }
            }
        },
        error: function (err) {
            console.log(err);
        },
    });
};
searchInput.addEventListener('keyup', function (e) {
    console.log(e.target.value);
    if (resultsBox.classList.contains('not-visible')) {
        resultsBox.classList.remove('not-visible');
    }
    if (e.target.value === '') {
        // If the input value is empty, hide the result div
        resultsBox.style.display = 'none';
    }
    else {
        // If the input value is not empty, show the result div
        resultsBox.style.display = 'block';
        sendSearchData(e.target.value);
    }
});
