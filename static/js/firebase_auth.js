// Configuração Firebase
const firebaseConfig = {
  apiKey: "AIzaSyDGj4fZsXO4Oo_6aahUKffJfJi0RPUWI74",
  authDomain: "projeto-pap-284ca.firebaseapp.com",
  projectId: "projeto-pap-284ca",
  storageBucket: "projeto-pap-284ca.appspot.com",
  messagingSenderId: "232143822949",
  appId: "1:232143822949:web:e5ed740f3caf499b05268c",
  measurementId: "G-H7QE5QXWW9"
};

// Inicializar Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const provider = new firebase.auth.GoogleAuthProvider();

// Login com Email/Password
function loginEmailPassword(e) {
    e.preventDefault();
    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    auth.signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
        localStorage.setItem("uid", userCredential.user.uid);
        window.location.href = "{{ url_for('questionario') }}";
    })
    .catch((error) => alert(error.message));
}

// Cadastro com Email/Password
function signupEmailPassword(e) {
    e.preventDefault();
    const email = document.getElementById("signupEmail").value;
    const password = document.getElementById("signupPassword").value;

    auth.createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
        localStorage.setItem("uid", userCredential.user.uid);
        window.location.href = "{{ url_for('questionario') }}";
    })
    .catch((error) => alert(error.message));
}

// Login com Google
function loginGoogle() {
    auth.signInWithPopup(provider)
    .then((result) => {
        localStorage.setItem("uid", result.user.uid);
        window.location.href = "{{ url_for('questionario') }}";
    })
    .catch((error) => alert(error.message));
}
