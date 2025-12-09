// Gestion des étudiants
let etudiants = [];

const liste = document.getElementById('listeEtudiants');
const nomInput = document.getElementById('nomEtudiant');
const ajouterBtn = document.getElementById('ajouterEtudiant');
const supprimerBtn = document.getElementById('supprimerEtudiant');

function afficherEtudiants() {
  liste.innerHTML = '';
  etudiants.forEach(nom => {
    const li = document.createElement('li');
    li.textContent = nom;
    liste.appendChild(li);
  });
}

ajouterBtn.addEventListener('click', () => {
  const nom = nomInput.value.trim();
  if(nom && !etudiants.includes(nom)) {
    etudiants.push(nom);
    afficherEtudiants();
    nomInput.value = '';
  }
});

supprimerBtn.addEventListener('click', () => {
  const nom = nomInput.value.trim();
  etudiants = etudiants.filter(e => e !== nom);
  afficherEtudiants();
  nomInput.value = '';
});

// Générateur de mots de passe
const btnMDP = document.getElementById('genererMDP');
const mdpAffiche = document.getElementById('mdpGenere');

btnMDP.addEventListener('click', () => {
  const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
  let mdp = '';
  for(let i=0; i<12; i++){
    mdp += chars.charAt(Math.floor(Math.random()*chars.length));
  }
  mdpAffiche.textContent = mdp;
});
