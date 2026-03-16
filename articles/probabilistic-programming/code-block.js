let symbols = {
    // Greek Letters (Sample)
    [String.raw `\alpha`]: "α",
    [String.raw `\beta`]: "β",
    [String.raw `\gamma`]: "γ",
    [String.raw `\lambda`]: "λ",
    [String.raw `\pi`]: "π",

    // Arrows
    "->": "→",
    "<-": "←",
    "<->": "↔",
    "=>": "⇒",
    [String.raw `\iff`]: "↔",
    [String.raw `\implies`]: "→",
    [String.raw `\impliedby`]: "←",
    [String.raw `\mapsto`]: "↦",
    [String.raw `\r`]: "→", // Common shorthand
    [String.raw `\l`]: "←", // Common shorthand

    // Quantifiers
    [String.raw `\forall`]: "∀",
    [String.raw `\exists`]: "∃",

    // Logical Connectives
    "/\\": "∧",
    "\\/": "∨",
    [String.raw `\and`]: "∧",
    [String.raw `\or`]: "∨",
    [String.raw `\not`]: "¬",
    [String.raw `\ne`]: "≠",
    [String.raw `\le`]: "≤",
    [String.raw `\ge`]: "≥",

    // Set Theory & Type Operations
    [String.raw `\in`]: "∈",
    [String.raw `\notin`]: "∉",
    [String.raw `\subset`]: "⊆",
    [String.raw `\subseteq`]: "⊆",
    [String.raw `\union`]: "∪",
    [String.raw `\inter`]: "∩",
    [String.raw `\empty`]: "∅",
    [String.raw `\times`]: "×",
    [String.raw `\comp`]: "∘",

    // Products and Sums
    [String.raw `\sum`]: "∑",
    [String.raw `\prod`]: "∏",

    // Common Types (Blackboard Bold)
    [String.raw `\N`]: "ℕ",
    [String.raw `\nat`]: "ℕ",
    [String.raw `\Z`]: "ℤ",
    [String.raw `\int`]: "ℤ",
    [String.raw `\Q`]: "ℚ",
    [String.raw `\rat`]: "ℚ",
    [String.raw `\R`]: "ℝ",
    [String.raw `\real`]: "ℝ",
    [String.raw `\C`]: "ℂ",
    [String.raw `\complex`]: "ℂ",

    // Syntactic Sugar / Proof Symbols
    [String.raw `\turnstile`]: "⊢",
    [String.raw `\qed`]: "∎",
    [String.raw `\cdot`]: "·"
};

const codeBlock = (id, language, code) => {
    let container = document.getElementById(id);
    let processedCode = code;

    for (const [key, sym] of Object.entries(symbols)) {
        processedCode = processedCode.replaceAll(key, sym);
    }

    let lang = document.createElement("p");
    lang.classList.add("code-language");
    lang.innerText = language;

    let codeBody = document.createElement("pre");
    codeBody.classList.add("code-body");
    codeBody.innerText = processedCode;

    container.classList.add("code-container");
    container.appendChild(lang);
    container.appendChild(document.createElement("hr"));
    container.appendChild(codeBody);
};

// <div class="code-container">
// <p class="code-language">language</p>
// <hr />
// 
// <pre class="code-body"></pre>
// </div>
