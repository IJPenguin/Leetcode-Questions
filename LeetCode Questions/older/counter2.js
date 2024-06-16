const createCounter = function (init) {
    temp = init;
    return {
        increment() {
            init++
        },
        decrement() {
            init--
        },
        reset() {
            init = temp
        }
    }
}

