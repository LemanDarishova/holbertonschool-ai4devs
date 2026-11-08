function calculateQuantity(orders) {
    let totalQuantity = 0;

    for (let i = 0; i < orders.length; i++) {
        totalQuantity += orders[i].quantity;
    }

    return totalQuantity;
}

const orders = [
    { product: "Laptop", quantity: "2" },
    { product: "Mouse", quantity: "3" },
    { product: "Keyboard", quantity: "1" }
];

console.log("Total quantity:", calculateQuantity(orders));
