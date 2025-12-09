// Charger les étudiants depuis le localStorage
let students = JSON.parse(localStorage.getItem("students")) || [];

// Afficher les étudiants dans la liste
function displayStudents() {
    const list = document.getElementById("studentList");
    list.innerHTML = "";

    students.forEach((name, index) => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${name}
            <button class="delete-btn" onclick="deleteStudent(${index})">Supprimer</button>
        `;
        list.appendChild(li);
    });
}

// Ajouter un étudiant
function addStudent() {
    const name = document.getElementById("studentName").value;

    if (name.trim() === "") {
        alert("Veuillez entrer un nom.");
        return;
    }

    students.push(name);
    localStorage.setItem("students", JSON.stringify(students));
    document.getElementById("studentName").value = "";
    displayStudents();
}

// Supprimer un étudiant
function deleteStudent(index) {
    students.splice(index, 1);
    localStorage.setItem("students", JSON.stringify(students));
    displayStudents();
}

// Affichage au chargement
displayStudents();
