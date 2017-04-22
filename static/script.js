document.getElementById('logout-link').onclick = function() {
    document.getElementById('logout-form').submit();
    var myForm = document.createElement('form');
    myForm.action = this.href;
    myForm.target = 'myFrame';
    myForm.method = 'POST';
    myForm.submit();
    location.reload();
    return false;
};
