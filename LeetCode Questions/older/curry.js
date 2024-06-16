const curry = (fn) => {
    return function curried(...args) {
        if (args.length >= fn.length) { // This if statement checks num of args provided to curried to the num of args in the fn function
            return fn(...args)
        };
        return curried.bind(this, ...args);
    }
}