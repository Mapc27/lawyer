$(document).ready(function(){
    $('.solved-tasks').slick({
        dots: true,
        focusOnSelect: true
    })
});

cleave_params = {
    phone: true,
    phoneRegionCode: 'RU',
}

new Cleave('#phone_number', cleave_params);
new Cleave('#contact-phone_number', cleave_params);

const checkForm = document.querySelector("#checkForm");
const contactForm = document.querySelector("#contactForm");

checkForm.addEventListener("submit", (e) => submit_form(e, checkForm));
contactForm.addEventListener("submit", (e) => submit_form(e, contactForm));

function validate_form(form){
    let regex = '^(\\+7|7|8)?[\\s\\-]?\\(?[489][0-9]{2}\\)?[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{2}[\\s\\-]?[0-9]{2}$'
    let re = new RegExp(regex);
    return re.test(form.phone_number.value);
}

function submit_form (e, form){
    e.preventDefault();
    if (!validate_form(form)){
        form.phone_number.classList.add('invalid-input');
        form.querySelector(".invalid-message").classList.add('display-block');
        return
    }

    const formData = new FormData(form);
    let href = ''
    if(form === checkForm) {
        href = 'api/applications/'
    }
    else if(form === contactForm){
        href = 'api/applications/'
    }

    axios.post(
        window.location.href + href,
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        })
        .then((res) => {
            console.log(res);
        })
        .catch((err) => {
            console.log(err);
        });

    form.form_button.classList.add("button-success")
    form.form_button.textContent = "Заявка отправлена"

    let el;
    for (el of form.elements){
        el.disabled = true;
    }
}


$('.title-button-link').on( 'click', function(){
    let el = $(this);
    let dest = el.attr('href');
    if(dest !== undefined && dest !== '') {
        $('html').animate({
    	    scrollTop: $(dest).offset().top
        }, 700
        );
    }
    return false;
});

let phone_number = checkForm.phone_number
let contact_phone_number = contactForm.phone_number

phone_number.addEventListener('input', () => oninput_phone(phone_number, document.querySelector('#invalid-message')))
contact_phone_number.addEventListener('input', () => oninput_phone(contact_phone_number, document.querySelector('#contact-invalid-message')))

function oninput_phone(el, message_el) {
    el.classList.remove('invalid-input')
    message_el.classList.remove('display-block')
}
