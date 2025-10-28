const form_reg = document.getElementById('formReg');
if (form_reg) {
    form_reg.addEventListener('submit', function (event) {
        event.preventDefault();
        let password_one = form_reg.querySelector('#us_password_one');
        let password_two = form_reg.querySelector('#us_password_two');
        if (password_one.value !== password_two.value) {
            alert('Пароли не совпадают');
            password_two.value = '';
            password_two.focus();
            return;
        }
        form_reg.submit();
    })
}
alert(1000);