functions = [
    () => new Promise((res) => setTimeout(res, 300)),
    () => new Promise((res) => setTimeout(res, 400)),
    () => new Promise((res) => setTimeout(res, 200)),
];

n = 2

const promisePool = async function (functions, n) {
    return new Promise((resolve, reject) => {
        for (let i = 0; i < functions.length; i++){
            functions[i].call();
        }
        resolve('resolved');
    })
}