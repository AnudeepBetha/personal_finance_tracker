// Setting up CSRF token for AJAX requests
$.ajaxSetup({
    headers: {
        'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')
    }
});

// Enables edit mode for a transaction row
$(document).ready(function() {
    $(document).on('click', '.edit-icon', function() {
        let row = $(this).closest('tr');
        let id = $(this).data('id');
        let amountCell = row.find('td:nth-child(4)');
        let dateCell = row.find('td:nth-child(5)');

        let amount = amountCell.text();
        let date = dateCell.text();
        let [ month, day, year] = date.split("-");
        date = `${year}-${month}-${day}`;

        amountCell.html('<input type="text" value="' + amount + '">');
        dateCell.html('<input type="date" value="' + date + '">');

        $(this).removeClass('fas fa-pencil-alt edit-icon').addClass('fa-solid fa-check save-icon');
    });

    // Enables save mode for a transaction row
    $(document).on('click', '.save-icon', function() {
        let row = $(this).closest('tr');
        let id = $(this).data('id');
        let self = this;

        let amount = row.find('td:nth-child(4) input').val();
        let date = row.find('td:nth-child(5) input').val();
        let transactionType = row.find('.transaction-type').text(); 
        let csrfToken = $('meta[name="csrf-token"]').attr('content');


        // Make an AJAX call to save the data
        $.post(UPDATE_TRANSACTIONS_URL, {
            id: id,
            amount: amount,
            date: date,
            transaction_type: transactionType,
            // Can add other fields if needed
            csrfmiddlewaretoken: csrfToken,
        }, function(response) {
            if (response.status === 'success') {
                // Updating the row with the new data and change the icon back to "Edit"
                row.find('td:nth-child(4)').text(amount);
                row.find('td:nth-child(5)').text(formatDateToDisplay(date));

                $(self).removeClass('fa-solid fa-check save-icon').addClass('fas fa-pencil-alt edit-icon');
            } else {
                console.log('Failed to save changes. ' + response.error);
            }
        });
    });

    // Deletes a transaction row
    $(document).on('click', '.delete-icon', function() {
        let transactionId = $(this).data('id');
        console.log(this)
        $.post(DELETE_TRANSACTIONS_URL, {
            id: transactionId,
        }, function(response) {
            if (response.status === 'success') {
                // Remove the row from the table
                $(`[data-id="${transactionId}"]`).closest('tr').remove();
            } else {
                alert('Failed to delete transaction. ' + response.error);
            }
        });
    });
});

// Converts date format from YYYY-MM-DD to MM-DD-YYYY

function formatDateToDisplay(dateString) {
    let [year, month, day] = dateString.split('-');
    return `${month}-${day}-${year}`;
}