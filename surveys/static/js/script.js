
document.addEventListener('DOMContentLoaded', function() {
    var inputs = document.querySelectorAll('.survey-item input');
    var submitBtn = document.getElementById('submit-btn');

    inputs.forEach(function(input) {
    input.addEventListener('input', function() {
    var value = this.value;
    if (isNaN(value) || value < 0) {
    this.classList.add('is-invalid');
    submitBtn.disabled = true;
} else {
    this.classList.remove('is-invalid');
    submitBtn.disabled = false;
}
});
});

    document.getElementById('survey-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var isValid = true;
    inputs.forEach(function(input) {
    if (input.classList.contains('is-invalid')) {
    isValid = false;
}
});
    if (isValid) {
    this.submit();
} else {
    alert('숫자 이외의 데이터가 입력되었습니다. 다시 확인해주세요.');
}
});
});
