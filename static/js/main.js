const loginBtn = document.getElementById("btnLogin");
const cadastroBtn = document.getElementById("btnCadastro");

const loginForm = document.getElementById("loginForm");
const cadastroForm = document.getElementById("cadastroForm");

loginBtn.addEventListener("click", () => {
    loginForm.classList.add("active");
    cadastroForm.classList.remove("active");

    loginBtn.classList.add("active");
    cadastroBtn.classList.remove("active");
});

cadastroBtn.addEventListener("click", () => {
    cadastroForm.classList.add("active");
    loginForm.classList.remove("active");

    cadastroBtn.classList.add("active");
    loginBtn.classList.remove("active");
});
