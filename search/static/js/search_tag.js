var hashTags = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('q'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    prefetch: '/hashtag.json?q=%QUERY',
    remote: {
    url: '/hashtag.json?q=%QUERY',
    wildcard: '%QUERY'
    }
});

$('.search-tag-query').typeahead({
    hint:true,
    highlight: true,
    // autoselect: true,
    minLength:1,
    limit: 10,
},
    {
    name: 'hashTags',
    display: 'q',
    // displayKey: 'count',
    source: hashTags.ttAdapter(),
    templates: {
        empty: 'Результаты не найдены...',
        suggestion: function (data) {
            return '<p><span>' + data.q + '</span></p>';
        }
    }
});
