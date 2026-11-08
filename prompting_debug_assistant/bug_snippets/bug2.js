function calculateTotal(prices) {
    let total = 0;

    for (let i = 0; i < prices.length; i++) {
        total += prices[i];
    }

    let discount = 10;
    let finalPrice = total + (total * discount / 100);

    return finalPrice;
}

const products = [100, 200, 300];

console.log("Final price:", calculateTotal(products));
