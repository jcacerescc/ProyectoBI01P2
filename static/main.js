const form = document.getElementById("upload-form");
const resultsContainer = document.getElementById("results-container");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  // Create a FormData object to store the file data
  const formData = new FormData();
  formData.append("file", form.file.files[0]);

  // Send a POST request to the server with the file data
  fetch("/predict", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      // Update the contents of the results container with the prediction results
      const html = `<p>Positive reviews: ${data.positive}</p>
                    <p>Negative reviews: ${data.negative}</p>`;
      resultsContainer.innerHTML = html;
    })
    .catch((error) => {
      console.error(error);
    });
});
