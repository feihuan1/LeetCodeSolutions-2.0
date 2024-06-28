
// brute force will be loop in loop O(n^2)

// two pointer approach 

// set two pointer i, j on each side of array , res initial to 0 
// loop arr while i < j 
// w * h is current container size w = j - i, h will be height[i] or height[j] witchever smaller 
// update res if w * h is bigger 
// move one pointer to center if that array value at index of pointer is smaller than other

 // time: O(n) 
 // space: O(1)
 var maxArea = function (height) {
    let i = 0
    let j = height.length - 1
    let res = 0
    while (i < j) {
        const h = Math.min(height[i], height[j])
        const w = j - i 

        res = Math.max(res, h * w)
        console.log(res, i, j, h, w)
        if (height[i] < height[j]) {
            i++
        } else {
            j--
        }
    }
    return res
};