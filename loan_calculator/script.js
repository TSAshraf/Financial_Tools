// Get elements
const loanAmountInput = document.getElementById("loanAmount");
const loanYearsInput = document.getElementById("loanYears");
const interestRateInput = document.getElementById("interestRate");
const rateDisplay = document.getElementById("rateDisplay");
const totalRepaymentDisplay = document.getElementById("totalRepayment");

// Function to calculate total repayment
function calculateRepayment() {
    let amount = parseFloat(loanAmountInput.value) || 0;
    let years = parseInt(loanYearsInput.value) || 0;
    let rate = parseFloat(interestRateInput.value) || 0;

    // Formula: Total Repayment = Loan Amount * (1 + (Interest Rate * Years) / 100)
    let totalRepayment = amount * (1 + (rate * years) / 100);

    // Display result
    totalRepaymentDisplay.textContent = `$${totalRepayment.toFixed(2)}`;
}

// Update interest rate display dynamically
interestRateInput.addEventListener("input", function () {
    rateDisplay.textContent = this.value + "%";
    calculateRepayment();
});

// Recalculate on input changes
loanAmountInput.addEventListener("input", calculateRepayment);
loanYearsInput.addEventListener("input", calculateRepayment);
