function Adder({ n1, n2 }) {
    const sum = n1 + n2;
    // return React.createElement('h1', {}, sum);
    return <h1>{sum}</h1> // JSX
}

ReactDOM.render(
    // React.createElement(Adder, {n1: 1, n2: 4}),
    <Adder n1={2} n2={4} />,
    document.getElementById('app')
);