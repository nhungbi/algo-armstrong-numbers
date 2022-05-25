// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(arrays) {
    armstrongArray = []
    for (let num of arrays) {
        const num_digit = String(num).length
        const lDigString= String(num).split('')
        const digitsArray = lDigString.filter(function (digit) {
            return Number(digit)})
        const totalArray = digitsArray.map( x => x**num_digit)
        sum = totalArray.reduce((prev,next) => prev + next, 0 )
        if (sum === num) {
            armstrongArray.push(num)
        }
    }
    return armstrongArray

};
console.log(exports.findArmstrongNumbers([1]))