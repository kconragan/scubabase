$(document).ready(function() {
    $('#search-input')
        .freebaseSuggest( {ac_param:{type:'/user/kconragan/scuba_diving/marine_creature'}} )
        .bind('fb-select', function(e, data) { console.log('suggest: ', data.guid); });
});