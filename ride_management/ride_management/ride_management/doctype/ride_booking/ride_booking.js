frappe.ui.form.on('Ride Booking', {
    onload: function (frm) {
        // Fetch the price_per_km from Ride App Settings
        frappe.call({
            method: 'frappe.client.get_value',
            args: {
                doctype: 'Ride App Settings',
                fieldname: 'price_per_km'
            },
            callback: function (response) {
                if (response.message) {
                    // Set the fetched price_per_km value in the Ride Booking form
                    frm.set_value('price_per_km', response.message.price_per_km);
                }
            }
        });
    }
});

frappe.ui.form.on("Ride Booking Item", {
    distance_in_km: function(frm, cdt, cdn) {
        // Get the current row
        const row = frappe.get_doc(cdt, cdn);
        const price_per_km = frm.doc.price_per_km;

        // Update the amount for the current row
        row.amount = row.distance_in_km * price_per_km;

        // Calculate total amount
        let total_amount = 0;
        frm.doc.items.forEach(item => {
            total_amount += item.amount || 0;
        });

        // Set total amount in parent document
        frm.set_value('total_amount', total_amount);

        // Refresh fields
        frm.refresh_field("items");
        frm.refresh_field("total_amount");
    }
});
