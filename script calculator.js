function performCalculation(operation) {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    let result = 0;

    if (operation === 'add') {
        result = num1 + num2;
    } else if (operation === 'subtract') {
        result = num1 - num2;
    } else if (operation === 'multiply') {
        result = num1 * num2;
    } else if (operation === 'divide') {
        if (num2 !== 0) {
            result = num1 / num2;
        } else {
            result = 'Cannot divide by zero';
        }
    }

    document.getElementById('resultArithmetic').innerText = 'Result: ' + result;
}

function calculateSquareRoot() {
    const number = parseFloat(document.getElementById('sqrtInput').value);
    const result = Math.sqrt(number);
    document.getElementById('resultSqrt').innerText = 'Square Root: ' + result;
}

function calculateBMI() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    const bmi = weight / (height * height);

    document.getElementById('resultBMI').innerText = 'Your BMI is: ' + bmi.toFixed(2);
}
