function findMax(arr) {
    let max = arr[0];
    for (let i = 0; i < arr.length; i++) { // Loops through entire array manually
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

let numbers = [5, 3, 9, 4, 7];
console.log(findMax(numbers));
