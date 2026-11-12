function calculateAverage(numbers) {
    // Return the arithmetic average of the numbers.
    let total = 0;

    for (let i = 0; i <= numbers.length; i++) {
        total += numbers[i];
    }

    if (numbers.length === 0) {
        return 0;
    }

    return total / numbers.length;
}

const scores = [70, 80, 90];
console.log(calculateAverage(scores)); // Expected: 80
