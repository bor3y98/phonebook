
    // JavaScript to handle phone number deletion
    document.addEventListener("DOMContentLoaded", function () {
        const phoneNumbersDiv = document.getElementById("phone_numbers");
        const addPhoneButton = document.getElementById("add-phone");

        // Function to handle phone number deletion
        function deletePhoneNumber(event) {
            event.preventDefault();
            const phoneNumberDiv = event.target.closest(".phone-number");
            if (phoneNumberDiv) {
                phoneNumberDiv.remove();
            }
        }

        // Attach click event handlers to delete buttons
        const deleteButtons = document.querySelectorAll(".delete-phone");
        deleteButtons.forEach(function (button) {
            button.addEventListener("click", deletePhoneNumber);
        });

        // Function to add a new phone number input field
        function addPhoneNumber() {
            const newPhoneNumberDiv = document.createElement("div");
            newPhoneNumberDiv.className = "phone-number";
            newPhoneNumberDiv.innerHTML = `
                <input type="text" name="phone_numbers" placeholder="Phone Number" required>
                <button type="button" class="delete-phone">Delete</button>
            `;
            phoneNumbersDiv.appendChild(newPhoneNumberDiv);

            // Attach a click event handler to the new delete button
            const deleteButton = newPhoneNumberDiv.querySelector(".delete-phone");
            deleteButton.addEventListener("click", deletePhoneNumber);
        }

        // Attach click event handler to the "Add Phone Number" button
        addPhoneButton.addEventListener("click", addPhoneNumber);
    });
