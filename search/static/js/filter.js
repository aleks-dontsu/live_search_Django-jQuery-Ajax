function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    // Получаем данные из формы
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.filter>.row');
    div.innerHTML = output;
}

let html = '\
{{#posts}}\
<!-- Listing Item -->\
<div class="col-lg-12 col-md-12 transform-rez">\
    <div class="listing-item-container list-layout">\
        <a href="../../post/{{ url }}" class="listing-item">\
            <!-- Image -->\
            <div class="listing-item-image">\
                    <img src="../media/{{ photo }}" alt="">\
            </div>\
            <!-- Content -->\
            <div class="listing-item-content">\
                <div class="listing-item-inner">\
                    <h3>{{ name }}\
                        <i class="verified-icon"></i>\
                    </h3>\
                    <p>\
                        {{ text }}\
                    </p>\
                </div>\
            </div>\
        </a>\
    </div>\
</div>\
<!-- Listing Item / End -->\
{{/posts}}'
