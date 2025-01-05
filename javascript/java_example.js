
console.log("hello world!") // prints: "hello world!"
//-------------------------------------------------------------------
my_name = 7
console.log(my_name) // prints: 7
//-------------------------------------------------------------------

const name = "bader"
// const name = "kamal" - const can not be changed. once defined as "bader".
console.log(name)
//-------------------------------------------------------------------
a = "majd"
console.log(a)
//-------------------------------------------------------------------
var number_1;
number_1 = 5
console.log(number_1)
//-------------------------------------------------------------------
var sum = 5 + 7
console.log(sum)
//-------------------------------------------------------------------
var number_2 = 18
number_2 += 1 //or: number ++
console.log(number_2)
//-------------------------------------------------------------------
var remainder
remainder = 12 % 7
console.log(remainder)
//-------------------------------------------------------------------
let number_3 = 33
//-------------------------------------------------------------------
number_3 = 46 // changes the value of number_3 from 33 to 46
console.log(number_3)
//-------------------------------------------------------------------
let first_name = "majd "
let second_name = "bader"
first_name += second_name
console.log(first_name)
//-------------------------------------------------------------------
let len_example = "example"
let len = len_example.length
console.log(len)
//-------------------------------------------------------------------
let word = "positive"
let ind_word_first_letter = word[0]
console.log(ind_word_first_letter)
//-------------------------------------------------------------------
let firstName = "majd"
let lastLetter0fFirstName = firstName[firstName.length - 1]
console.log(lastLetter0fFirstName)
//-------------------------------------------------------------------
function sentenceMaker(firstName, secondName) {
    let result = ""
    result += firstName + " " + secondName
    return result
}
console.log(sentenceMaker("majd", "bader"))
//-------------------------------------------------------------------
