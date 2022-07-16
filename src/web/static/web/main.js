$(document).ready(function(){
    $('.solved-tasks').slick({
        dots: true,
        focusOnSelect: true
    })
});

cleave_params = {
    phone: true,
    phoneRegionCode: 'RU',
    prefix: '+7 ',
    noImmediatePrefix: true,
}

new Cleave('#phone_number', cleave_params);
new Cleave('#contact-phone_number', cleave_params);

function validate_form(form){
    return form.phone_number.value.replace(/[^0-9]/g, "").length === 11
}

const checkForm = document.querySelector("#checkForm");
const contactForm = document.querySelector("#contactForm");

checkForm.addEventListener("submit", (e) => submit_form(e, checkForm));
contactForm.addEventListener("submit", (e) => submit_form(e, contactForm));

function submit_form (e, form){
    if (!validate_form(form)){
        e.preventDefault();

        console.log("ValidateError")
        return
    }

    const formData = new FormData(form);
    axios.post(
        window.location.href + 'api/applications/',
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
}
