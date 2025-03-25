// Funkcje pomocnicze do komunikacji z API
const api = {
  async getProjects() {
    const response = await fetch("/api/projects");
    return await response.json();
  },

  async addProject(project) {
    const response = await fetch("/api/projects", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(project),
    });
    return await response.json();
  },

  async deleteProject(projectId) {
    const response = await fetch(`/api/projects/${projectId}`, {
      method: "DELETE",
    });
    return await response.json();
  },

  async searchProjects(query) {
    const response = await fetch(
      `/api/projects/search?q=${encodeURIComponent(query)}`
    );
    return await response.json();
  },

  async sendContactMessage(data) {
    const response = await fetch("/api/contact", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    return await response.json();
  },

  async getStats() {
    const response = await fetch("/api/stats");
    return await response.json();
  },
};

// Płynne przewijanie do sekcji
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

// Burger menu
const burger = document.querySelector(".burger");
const nav = document.querySelector(".nav-links");
const navLinks = document.querySelectorAll(".nav-links li");

burger.addEventListener("click", () => {
  nav.classList.toggle("nav-active");
  navLinks.forEach((link, index) => {
    if (link.style.animation) {
      link.style.animation = "";
    } else {
      link.style.animation = `navLinkFade 0.5s ease forwards ${
        index / 7 + 0.3
      }s`;
    }
  });
  burger.classList.toggle("toggle");
});

// Formularz kontaktowy
const contactForm = document.getElementById("contact-form");
contactForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(contactForm);
  const data = {
    name: formData.get("name"),
    email: formData.get("email"),
    message: formData.get("message"),
  };

  try {
    const result = await api.sendContactMessage(data);
    alert(result.message);
    contactForm.reset();
  } catch (error) {
    console.error("Błąd:", error);
    alert("Wystąpił błąd podczas wysyłania wiadomości.");
  }
});

// Formularz dodawania projektu
const newProjectForm = document.getElementById("new-project-form");
newProjectForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(newProjectForm);
  const data = {
    title: formData.get("title"),
    description: formData.get("description"),
    technologies: formData
      .get("technologies")
      .split(",")
      .map((tech) => tech.trim()),
    image: formData.get("image"),
    link: formData.get("link"),
  };

  try {
    const result = await api.addProject(data);
    alert(result.message);
    newProjectForm.reset();
    window.location.reload();
  } catch (error) {
    console.error("Błąd:", error);
    alert("Wystąpił błąd podczas dodawania projektu.");
  }
});

// Wyszukiwarka projektów
const searchInput = document.createElement("input");
searchInput.type = "text";
searchInput.placeholder = "Szukaj projektów...";
searchInput.className = "search-input";
document
  .querySelector(".projects")
  .insertBefore(searchInput, document.querySelector(".projects-grid"));

let searchTimeout;
searchInput.addEventListener("input", async (e) => {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(async () => {
    const query = e.target.value;
    if (query.length >= 2) {
      try {
        const projects = await api.searchProjects(query);
        updateProjectsGrid(projects);
      } catch (error) {
        console.error("Błąd wyszukiwania:", error);
      }
    } else {
      const projects = await api.getProjects();
      updateProjectsGrid(projects);
    }
  }, 300);
});

// Aktualizacja siatki projektów
async function updateProjectsGrid(projects) {
  const grid = document.querySelector(".projects-grid");
  grid.innerHTML = "";

  projects.forEach((project, index) => {
    const card = document.createElement("div");
    card.className = "project-card";
    card.innerHTML = `
            <img src="${project.image}" alt="${project.title}">
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <div class="project-technologies">
                ${project.technologies
                  .map((tech) => `<span>${tech}</span>`)
                  .join("")}
            </div>
            <a href="${project.link}" class="project-link">Zobacz projekt</a>
            <button class="delete-project" data-id="${index}">Usuń projekt</button>
        `;
    grid.appendChild(card);
  });

  // Dodaj obsługę usuwania projektów
  document.querySelectorAll(".delete-project").forEach((button) => {
    button.addEventListener("click", async (e) => {
      if (confirm("Czy na pewno chcesz usunąć ten projekt?")) {
        try {
          const result = await api.deleteProject(e.target.dataset.id);
          alert(result.message);
          window.location.reload();
        } catch (error) {
          console.error("Błąd:", error);
          alert("Wystąpił błąd podczas usuwania projektu.");
        }
      }
    });
  });
}

// Wyświetlanie statystyk
async function updateStats() {
  try {
    const stats = await api.getStats();
    const statsDiv = document.createElement("div");
    statsDiv.className = "stats";
    statsDiv.innerHTML = `
            <h3>Statystyki</h3>
            <p>Liczba projektów: ${stats.total_projects}</p>
            <p>Liczba wiadomości: ${stats.total_messages}</p>
            <p>Ostatnia aktualizacja: ${stats.last_updated}</p>
        `;
    document
      .querySelector(".projects")
      .insertBefore(statsDiv, document.querySelector(".projects-grid"));
  } catch (error) {
    console.error("Błąd pobierania statystyk:", error);
  }
}

// Inicjalizacja
document.addEventListener("DOMContentLoaded", async () => {
  const projects = await api.getProjects();
  updateProjectsGrid(projects);
  updateStats();
});

// Animacja pojawiania się elementów podczas scrollowania
const observerOptions = {
  threshold: 0.1,
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("fade-in");
    }
  });
}, observerOptions);

document.querySelectorAll("section").forEach((section) => {
  observer.observe(section);
});
