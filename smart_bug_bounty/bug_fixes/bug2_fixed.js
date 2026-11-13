function calculateAverage(numbers) {
    // Return the arithmetic average of the numbers.
    if (numbers.length === 0) {
        return 0;
    }

    let total = 0;

    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }

    return total / numbers.length;
}

const scores = [70, 80, 90];
console.log(calculateAverage(scores)); // Expected: 80
