document.addEventListener("DOMContentLoaded", function () {
  // Fetch the side menu content
  fetch("../static/json/projects.json")
    .then((response) => response.json())
    .then((projects) => {
      const sideMenu = document.getElementById('side-menu')
      const navElement = document.createElement('nav')
      
      // Loop over projects
      for (const project of projects) {
        const link = document.createElement('a');

        link.href = project.url;
        link.textContent = project.name;

        navElement.appendChild(link);
      }
      
      sideMenu.appendChild(navElement);
      
    })
    .catch((error) => {
      console.error("Error fetching JSON data:", error);
    });
});
