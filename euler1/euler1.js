/** PROJECT EULER PROBLEM NUMBER 1:
 Find the sum of all the multiples of 3 or 5 below 1000.
 Generalized to find all the multiples of 3 or 5
 for 0 up to, but not including, x.**/

var findMultiples3and5 = function (x) {
    var total = 0;
    for (var i = 0; i < x; i++) {
        if ((i % 3 == 0) || (i % 5 == 0)) {
            total = total + i;
        }
    }
    console.log("The multiples of 3 and 5, less than " + x + ", is " + total + ".")
    return total;
};

findMultiples3and5(1000);