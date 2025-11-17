// Get elements
const allPagesCheckbox = document.getElementById('all-pages-checkbox');
const pageCheckboxes = [
    document.getElementById('page1-checkbox'),
    document.getElementById('page2-checkbox'),
    document.getElementById('page3-checkbox'),
    document.getElementById('page4-checkbox')
];

// Function to update individual checkboxes based on "All pages" checkbox
function updateIndividualCheckboxes() {
    const isChecked = allPagesCheckbox.checked;
    pageCheckboxes.forEach(checkbox => {
        checkbox.checked = isChecked;
    });
}

// Function to update "All pages" checkbox based on individual checkboxes
function updateAllPagesCheckbox() {
    const allChecked = pageCheckboxes.every(checkbox => checkbox.checked);
    const noneChecked = pageCheckboxes.every(checkbox => !checkbox.checked);

    if (allChecked) {
        allPagesCheckbox.checked = true;
        allPagesCheckbox.indeterminate = false;
    } else if (noneChecked) {
        allPagesCheckbox.checked = false;
        allPagesCheckbox.indeterminate = false;
    } else {
        allPagesCheckbox.indeterminate = true;
        allPagesCheckbox.checked = false;
    }
}

// Event listeners
allPagesCheckbox.addEventListener('change', updateIndividualCheckboxes);

pageCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', updateAllPagesCheckbox);
});

// Initial state
updateAllPagesCheckbox();
