$(document).ready(function(){
    $('.solved-tasks').slick({
        dots: true,
        focusOnSelect: true
    })
});

const input = document.querySelector("#phone_number");

const prefixNumber = (str) => {
    if (str === "7") {
        return "7 (";
    }
    if (str === "8") {
        return "8 (";
    }
    if (str === "9") {
        return "7 (9";
    }
    return "7 (";
};

// ======================================
input.addEventListener("input", () => {
    const value = input.value.replace(/\D+/g, "");
    const numberLength = 11;

    let result;
    if (input.value.includes("+8") || input.value[0] === "8") {
        result = "";
    } else {
        result = "+";
    }

    //
    for (let i = 0; i < value.length && i < numberLength; i++) {
        switch (i) {
            case 0:
                result += prefixNumber(value[i]);
                continue;
            case 4:
                result += ") ";
                break;
            case 7:
                result += "-";
                break;
            case 9:
                result += "-";
                break;
            default:
                break;
        }
        result += value[i];
    }
    //
    input.value = result;
});


function validate_form(){
    return document.checkForm.phone_number.value.replace(/[^0-9]/g, "").length === 11
}

const form = document.querySelector("#checkForm");
form.addEventListener("submit", (e) => {
    if (!validate_form()){
        console.log("ValidateError")
        return
    }
    e.preventDefault();

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
});
