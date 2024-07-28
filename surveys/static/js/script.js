
document.getElementById('button').addEventListener('click', function(event) {
    event.preventDefault();
    const form = document.getElementById('form');
     const total = form.querySelectorAll('input[type="radio"]:checked').length;
    if(total<9)alert('모든 필드를 채워주세요!');
    else form.submit();
});
    