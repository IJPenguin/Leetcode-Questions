functions = [(x) => x + 1, (x) => x * x, (x) => 2 * x];
for (const fn in functions) {
    const temp = fn
    console.log(temp(x))
}