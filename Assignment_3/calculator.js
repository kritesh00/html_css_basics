
export let add = (a, b) => a+b
export let subtract = (a, b) => a-b
export let multiply = (a, b) => a*b 
export let divide = (a, b) => { 
    if(b === 0){
        return 'Error: Division by zero'
    }
    return a / b;
}

