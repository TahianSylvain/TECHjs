const url = window.location.href
const searchForm = document.getElementById('search-form') as HTMLElement
var resultsBox = document.getElementById('results-box') as HTMLElement
const searchInput = document.getElementById('search-input') as HTMLElement
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendSearchData = (annotation) => {
    $.ajax({
        type: 'POST',
        url: 'search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'annotation': annotation,
        },
        success: (res) => {
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)) {
                console.log('we have an array')
                data.foreach(i => { // for await (const iterator of object) {}
                    resultsBox += `
                        <a href="">
                            <div class="row mt-2 mb-2">
                                <div class="col-10">
                                    <h5>${annotation.name}</h5>
                                    <p class="text-muted">${annotation.account}</p>
                                </div>
                            </div>
                        </a>`
                })
            } else  {
                if (searchInput.value.length > 0) {
                    resultsBox.innerHTML = `<b>$(data)</b>`
                } else {
                    resultsBox.classList.add('not-visible')
                }
            }
        },
        error: (err) => {
            console.log(err)
        },
    })
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    if (resultsBox.classList.contains('not-visible')) {
        resultsBox.classList.remove('not-visible')
    }
    if (e.target.value === '') {
        // If the input value is empty, hide the result div
        resultsBox.style.display = 'none';
    } else {
        // If the input value is not empty, show the result div
        resultsBox.style.display = 'block';
        sendSearchData(e.target.value);
    }
})