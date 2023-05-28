// Event listener for form submission
document.getElementById('upload-form').addEventListener('submit', uploadFile);

// Function to handle file upload
function uploadFile(event) {
  event.preventDefault(); // Prevent the default behavior of form submission

  const formData = new FormData();
  const fileInput = document.getElementById('pdf-file');

  // Add the selected file to the form data
  formData.append('pdf-file', fileInput.files[0]);

  // Send a POST request to the Flask route for file upload
  axios.post('/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })
    .then(response => {
      // Handle the response after file upload
      console.log(response.data);
      // ... Perform additional actions or update the UI
    })
    .catch(error => {
      console.error('Error:', error);
      // ... Handle the error if any
    });
}
