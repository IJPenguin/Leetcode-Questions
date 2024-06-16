function memoize(fn) {
    const cache = {};
    return function (...args) {
        const key = JSON.stringify();
        if (key in cache) {
            return cache[key];
        }
        const output = fn(...args);
        cache[key] = output;
        return output;
    };
}
